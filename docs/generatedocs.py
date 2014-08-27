#!/usr/bin/env jspython
from JumpScale import j
from HTMLParser import HTMLParser
from xml.etree import cElementTree as etree
import JumpScale.baselib.git


class Parser(HTMLParser):
    def __init__(self):
      HTMLParser.__init__(self)
      self.tb = etree.TreeBuilder()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # if 'id' in attrs and attrs['id'] == 'jumpscale-api':
        self.tb.start(tag, dict(attrs)) 

    def handle_endtag(self, tag):
        self.tb.end(tag)

    def handle_data(self, data):
        self.tb.data(data)

    def close(self):
        HTMLParser.close(self)
        return self.tb.close()


print "UPDATING CORE..."
corecl = j.clients.git.getClient('/opt/code/github/jumpscale/jumpscale_core/')
corecl.pull()
print "UPDATED"

print "\nUPDATING DOCS..."
doccl = j.clients.git.getClient('/opt/code/github/jumpscale/jumpscale_docs/')
doccl.pull()
print "UPDATED"

print "\nUPDATING GENERATED DOCS..."
gencl = j.clients.git.getClient('/opt/code/github/jumpscale/generated_docs/')
gencl.pull()
print "UPDATED"

print "\nGenerating API docs..."
j.system.process.execute("""cd /opt/code/github/jumpscale/generated_docs/docs/;
    sphinx-apidoc -o _source/API/ /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/console /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/baselib/zredisgw /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/Shell.py /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/debugger/Debugger.py /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/gui/
""")

print "Generated"

print "\nConverting Confluence to RST..."
j.system.process.execute("""cd /opt/code/github/jumpscale/jumpscale_prototypes/prototypes/confluence2rst; python confluence2rst.py""")
print "Converted"

originalcontents = '***********************************\nWelcome to Jumpscale documentation!\n***********************************\n\nJumpScale Core\n##############\n.. toctree::\n   :maxdepth: 2\n   :glob:\n\n   spaces/Doc_Jumpscale_Core/Docs/index\n\n\nJumpScale How Tos\n#################\n.. toctree::\n   :maxdepth: 2\n   :glob:\n\n   spaces/Doc_Jumpscale_Howto/Docs/index\n\n\nJumpScale Portal\n################\n.. toctree::\n   :maxdepth: 2\n   :glob:\n\n   spaces/Doc_Jumpscale_Portal/index\n\n\nJumpScale Grid\n##############\n.. toctree::\n   :maxdepth: 2\n   :glob:\n\n   spaces/Doc_Jumpscale_Grid/Docs/index\n\n\nJumpScale API\n#############\n\n.. toctree::\n   :maxdepth: 3\n   :glob:\n\n   API/JumpScale\n\n\nJumpScale Development\n#####################\n.. include:: spaces/Doc_Jumpscale_Devel/Home.rst\n\nComponents and Tools\n^^^^^^^^^^^^^^^^^^^^\n\n.. toctree::\n   :maxdepth: 2\n   :glob:\n\n   spaces/Doc_Jumpscale_Devel/Docs/index\n\nIndices and tables\n==================\n\n* :ref:`genindex`\n* :ref:`modindex`\n* :ref:`search`\n\n'


j.system.fs.remove('/opt/code/github/jumpscale/generated_docs/docs/_source/index.rst')
j.system.fs.writeFile('/opt/code/github/jumpscale/generated_docs/docs/_source/index.rst', originalcontents, append=False)

print "\nBuilding..."
j.system.process.execute("cd /opt/code/github/jumpscale/generated_docs/docs/; sphinx-build _source/ _build/")
print "Built"

print "\nMaking HTML"
j.system.process.execute("cd /opt/code/github/jumpscale/generated_docs/docs/; make html")
print "DONE"


contents = j.system.fs.fileGetContents('/opt/code/github/jumpscale/generated_docs/docs/_build/html/index.html')
contents = contents.decode('utf-8')

parser = Parser()
parser.feed(contents)
root = parser.close()
div = root.find(".//div[@id='jumpscale-api']")

divcontents = '\n'
for child in div:
    divcontents += etree.tostring(child, encoding='utf-8')

divcontents = divcontents.replace('\n', '\n   ')

rstcontents = originalcontents
rstcontents = rstcontents.replace("""JumpScale API\n#############\n\n.. toctree::\n   :maxdepth: 3\n   :glob:\n\n   API/JumpScale""", '.. raw:: html\n%s' % divcontents)

j.system.fs.remove('/opt/code/github/jumpscale/generated_docs/docs/_source/index.rst')
j.system.fs.writeFile('/opt/code/github/jumpscale/generated_docs/docs/_source/index.rst', rstcontents, append=False)


j.system.fs.removeDirTree('/opt/code/github/jumpscale/generated_docs/docs/_source/API')


gencl.addRemoveFiles()
gencl.commit('auto generated docs')
gencl.push()

