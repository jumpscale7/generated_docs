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

print "\nConverting Confluence to RST..."
j.system.process.execute("""cd /opt/code/github/jumpscale/jumpscale_prototypes/prototypes/confluence2rst; python confluence2rst.py""")
print "Converted"

gencl.addRemoveFiles()
gencl.commit('auto generated docs')
gencl.push()

