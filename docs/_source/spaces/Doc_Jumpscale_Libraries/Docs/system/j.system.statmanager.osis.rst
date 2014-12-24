
j.system.statmanager.osis
=========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/grid/osis/OSISClientForCat.py>`_


authenticate
------------


* params: name,passwd
* path:/grid/osis/OSISClientForCat.py (line:53)


authenticates a user and returns the groups in which the user is


count
-----


* params: query
* path:/grid/osis/OSISClientForCat.py (line:67)


delete
------


* params: key
* path:/grid/osis/OSISClientForCat.py (line:118)


deleteSearch
------------


* params: query
* path:/grid/osis/OSISClientForCat.py (line:121)


demodata
--------


* params:
* path:/grid/osis/OSISClientForCat.py (line:70)


populate db with demodata


destroy
-------


* params:
* path:/grid/osis/OSISClientForCat.py (line:132)


exists
------


* params: key
* path:/grid/osis/OSISClientForCat.py (line:112)


existsIndex
-----------


* params: key,timeout
* path:/grid/osis/OSISClientForCat.py (line:115)


get
---


* params: key
* path:/grid/osis/OSISClientForCat.py (line:94)


list
----


* params: prefix
* path:/grid/osis/OSISClientForCat.py (line:136)


native
------


* params: methodname,kwargs
* path:/grid/osis/OSISClientForCat.py (line:64)


new
---


* params:
* path:/grid/osis/OSISClientForCat.py (line:59)


rebuildindex
------------


* params:
* path:/grid/osis/OSISClientForCat.py (line:76)


rebuildindex


search
------


* params: query,start,size
* path:/grid/osis/OSISClientForCat.py (line:140)


set
---


* params: obj,key,waitIndex
* path:/grid/osis/OSISClientForCat.py (line:82)


if key none then key will be given by server


simpleSearch
------------


* params: params,start,size,withguid,withtotal,sort,partials,nativequery
* path:/grid/osis/OSISClientForCat.py (line:145)


e.g. {"name":name,"country":"belgium"}


updateSearch
------------


* params: query,update
* path:/grid/osis/OSISClientForCat.py (line:124)


update is dict or text
dict e.g. {"name":aname,nr:1}  these fields will be updated then
text e.g. name:aname nr:1


