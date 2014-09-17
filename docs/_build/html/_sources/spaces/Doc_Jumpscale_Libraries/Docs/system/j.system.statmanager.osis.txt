
j.system.statmanager.osis
=========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/grid/osis/OSISClientForCat.py>`_


authenticate
------------


* params: name,passwd
* path:/grid/osis/OSISClientForCat.py (line:50)


authenticates a user and returns the groups in which the user is


delete
------


* params: key
* path:/grid/osis/OSISClientForCat.py (line:111)


deleteSearch
------------


* params: query
* path:/grid/osis/OSISClientForCat.py (line:114)


demodata
--------


* params:
* path:/grid/osis/OSISClientForCat.py (line:63)


populate db with demodata


destroy
-------


* params:
* path:/grid/osis/OSISClientForCat.py (line:125)


exists
------


* params: key
* path:/grid/osis/OSISClientForCat.py (line:105)


existsIndex
-----------


* params: key,timeout
* path:/grid/osis/OSISClientForCat.py (line:108)


get
---


* params: key
* path:/grid/osis/OSISClientForCat.py (line:87)


list
----


* params: prefix
* path:/grid/osis/OSISClientForCat.py (line:129)


new
---


* params:
* path:/grid/osis/OSISClientForCat.py (line:56)


rebuildindex
------------


* params:
* path:/grid/osis/OSISClientForCat.py (line:69)


rebuildindex


search
------


* params: query,start,size
* path:/grid/osis/OSISClientForCat.py (line:133)


set
---


* params: obj,key,waitIndex
* path:/grid/osis/OSISClientForCat.py (line:75)


if key none then key will be given by server


simpleSearch
------------


* params: params,start,size,withguid,withtotal,sort,partials,nativequery
* path:/grid/osis/OSISClientForCat.py (line:138)


e.g. {"name":name,"country":"belgium"}


updateSearch
------------


* params: query,update
* path:/grid/osis/OSISClientForCat.py (line:117)


update is dict or text
dict e.g. {"name":aname,nr:1}  these fields will be updated then
text e.g. name:aname nr:1


