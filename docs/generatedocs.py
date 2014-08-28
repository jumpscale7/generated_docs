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

j.system.fs.removeDirTree('/opt/code/github/jumpscale/generated_docs/docs/_source/API')

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

for module in j.system.fs.listFilesInDir('/opt/code/github/jumpscale/generated_docs/docs/_build/html/API', recursive=False, filter='*.html'):
    basepath = "/opt/code/github/jumpscale/generated_docs/docs/_source/API"
    basename = j.system.fs.getBaseName(module).replace('.html', '.rst')
    contents = j.system.fs.fileGetContents(module)
    contents = '.. raw:: html\n%s' % contents
    contents = contents.replace('\n', '\n   ')
    newpath = j.system.fs.joinPaths(basepath, basename)
    j.system.fs.remove(newpath)
    j.system.fs.writeFile(newpath, contents)


defaultcss = '/*\n * default.css_t\n * ~~~~~~~~~~~~~\n *\n * Sphinx stylesheet -- default theme.\n *\n * :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.\n * :license: BSD, see LICENSE for details.\n *\n */\n\n@import url("basic.css");\n\n/* -- page layout ----------------------------------------------------------- */\n\nbody {\n    font-family: sans-serif;\n    font-size: 100%;\n    background-color: #11303d;\n    color: #000;\n    margin: 0;\n    padding: 0;\n}\n\ndiv.document {\n    background-color: #1c4e63;\n}\n\ndiv.documentwrapper {\n    float: left;\n    width: 100%;\n}\n\ndiv.bodywrapper {\n    margin-left: 0px;\n    margin: 0 0 0 230px;\n}\n\ndiv.body {\n    background-color: #ffffff;\n    color: #000000;\n    padding: 0 20px 30px 20px;\n}\n\ndiv.footer {\n    color: #ffffff;\n    width: 100%;\n    padding: 9px 0 9px 0;\n    text-align: center;\n    font-size: 75%;\n}\n\ndiv.footer a {\n    color: #ffffff;\n    text-decoration: underline;\n}\n\ndiv.related {\n    display: none;\n}\n\ndiv.related a {\n    display: none;\n}\n\ndiv.sphinxsidebar {\n    display: none;\n}\n\ndiv.sphinxsidebar h3 {\n    display: none;\n}\n\ndiv.sphinxsidebar h3 a {\n    display: none;\n}\n\ndiv.sphinxsidebar h4 {\n    display: none;\n}\n\ndiv.sphinxsidebar p {\n    display: none;\n}\n\ndiv.sphinxsidebar p.topless {\n    display: none;\n}\n\ndiv.sphinxsidebar ul {\n    display: none;\n}\n\ndiv.sphinxsidebar a {\n    display: none;\n}\n\ndiv.sphinxsidebar input {\n    display: none;\n}\n\ndiv.bodywrapper {\n    width: 0 px;\n    margin-left: 0%;\n    font-size: 90%;\n}\n\n\n\n/* -- hyperlink styles ------------------------------------------------------ */\n\na {\n    color: #355f7c;\n    text-decoration: none;\n}\n\na:visited {\n    color: #355f7c;\n    text-decoration: none;\n}\n\na:hover {\n    text-decoration: underline;\n}\n\n\n\n/* -- body styles ----------------------------------------------------------- */\n\ndiv.body h1,\ndiv.body h2,\ndiv.body h3,\ndiv.body h4,\ndiv.body h5,\ndiv.body h6 {\n    font-family: \'Trebuchet MS\', sans-serif;\n    background-color: #f2f2f2;\n    font-weight: normal;\n    color: #20435c;\n    border-bottom: 1px solid #ccc;\n    margin: 20px -20px 10px -20px;\n    padding: 3px 0 3px 10px;\n}\n\ndiv.body h1 { margin-top: 0; font-size: 200%; }\ndiv.body h2 { font-size: 160%; }\ndiv.body h3 { font-size: 140%; }\ndiv.body h4 { font-size: 120%; }\ndiv.body h5 { font-size: 110%; }\ndiv.body h6 { font-size: 100%; }\n\na.headerlink {\n    color: #c60f0f;\n    font-size: 0.8em;\n    padding: 0 4px 0 4px;\n    text-decoration: none;\n}\n\na.headerlink:hover {\n    background-color: #c60f0f;\n    color: white;\n}\n\ndiv.body p, div.body dd, div.body li {\n    text-align: justify;\n    line-height: 130%;\n}\n\ndiv.admonition p.admonition-title + p {\n    display: inline;\n}\n\ndiv.admonition p {\n    margin-bottom: 5px;\n}\n\ndiv.admonition pre {\n    margin-bottom: 5px;\n}\n\ndiv.admonition ul, div.admonition ol {\n    margin-bottom: 5px;\n}\n\ndiv.note {\n    background-color: #eee;\n    border: 1px solid #ccc;\n}\n\ndiv.seealso {\n    background-color: #ffc;\n    border: 1px solid #ff6;\n}\n\ndiv.topic {\n    background-color: #eee;\n}\n\ndiv.warning {\n    background-color: #ffe4e4;\n    border: 1px solid #f66;\n}\n\np.admonition-title {\n    display: inline;\n}\n\np.admonition-title:after {\n    content: ":";\n}\n\npre {\n    padding: 5px;\n    background-color: #eeffcc;\n    color: #333333;\n    line-height: 120%;\n    border: 1px solid #ac9;\n    border-left: none;\n    border-right: none;\n}\n\ntt {\n    background-color: #ecf0f3;\n    padding: 0 1px 0 1px;\n    font-size: 0.95em;\n}\n\nth {\n    background-color: #ede;\n}\n\n.warning tt {\n    background: #efc2c2;\n}\n\n.note tt {\n    background: #d6d6d6;\n}\n\n.viewcode-back {\n    font-family: sans-serif;\n}\n\ndiv.viewcode-block:target {\n    background-color: #f4debf;\n    border-top: 1px solid #ac9;\n    border-bottom: 1px solid #ac9;\n}'

j.system.fs.writeFile('/opt/code/github/jumpscale/generated_docs/docs/_source/_static/default.css', defaultcss)



gencl.addRemoveFiles()
gencl.commit('auto generated docs')
gencl.push()

