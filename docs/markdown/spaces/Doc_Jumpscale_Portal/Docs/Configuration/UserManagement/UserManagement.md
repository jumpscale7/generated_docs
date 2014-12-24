User Management
===============

Allow guest access
------------------

It is possible to allow guest access to certain spaces. Todo the
following has to be configured:

-   Define a acl for the guest user.

Example content of .space/acl.cfg

~~~~ {.sourceCode .python}
#rights:
##R: read
##W: write/modify
##S: sync to e.g. local PC
##A: admin rights
##*: means all rights
guest=R
admin=*
~~~~

Command-line tools
------------------

-   [jsuser](JSUser)
-   [jsgroup](JSGroup)

