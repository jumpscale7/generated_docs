#!/usr/bin/env jspython
from JumpScale import j
import JumpScale.baselib.git

print "UPDATING CORE..."
corecl = j.clients.git.getClient('/opt/code/github/jumpscale/jumpscale_core/')
corecl.pull()
print "UPDATED"

print "\nUPDATING DOCS..."
doccl = j.clients.git.getClient('/opt/code/github/jumpscale/jumpscale_docs/')
corecl.pull()
print "UPDATED"

print "\nUPDATING GENERATED DOCS..."
gencl = j.clients.git.getClient('/opt/code/github/jumpscale/generated_docs/')
corecl.pull()
print "UPDATED"

print "\nGenerating API docs..."
j.system.process.execute("""cd /opt/code/github/jumpscale/generated_docs/docs/;
    sphinx-apidoc -o source/API/ /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/console /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/baselib/zredisgw /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/Shell.py /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/debugger/Debugger.py /opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/core/gui/
""")
print "Generated"

print "\nConverting Confluence to RST..."
j.system.process.execute("""cd /opt/code/github/jumpscale/jumpscale_prototypes/prototypes/confluence2rst; python confluence2rst.py""")
print "Converted"


print "\nMaking HTML"
j.system.process.execute("cd /opt/code/github/jumpscale/generated_docs/docs/; make html")
print "DONE"


gencl.addRemoveFiles()
gencl.commit('auto generated docs')
gencl.push()
