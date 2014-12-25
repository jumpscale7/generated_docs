
j.system.statmanager
====================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/statmanager/StatManager.py>`_


addInfo
-------


* params: info
* path:/baselib/statmanager/StatManager.py (line:197)


can be multi line
param:info dotnotation of info e.g. 'water.white.level.sb 10'  (as used in graphite)
result bool


addInfoLine2HistoryObj
----------------------


* params: id,value,epoch
* path:/baselib/statmanager/StatManager.py (line:162)


cleanCache
----------


* params:
* path:/baselib/statmanager/StatManager.py (line:117)


getEpoch
--------


* params:
* path:/baselib/statmanager/StatManager.py (line:132)


getFiveMinuteId
---------------


* params:
* path:/baselib/statmanager/StatManager.py (line:23)


getHeaders
----------


* params: start,stop
* path:/baselib/statmanager/StatManager.py (line:269)


getHistoryObject
----------------


* params: id
* path:/baselib/statmanager/StatManager.py (line:138)


getHourId
---------


* params:
* path:/baselib/statmanager/StatManager.py (line:29)


getInfo1h
---------


* params: id,start,stop
* path:/baselib/statmanager/StatManager.py (line:356)


return raw info (resolution is 1h)
param:id id in dot noation e.g. 'water.white.level.sb' (can be multiple use comma as separation)
param:start epoch; 0 means all
param:stop epoch; 0 means all
result list(list)


getInfo1hFromTo
---------------


* params: id,start,stop
* path:/baselib/statmanager/StatManager.py (line:316)


will not return more than 12 months of info, resolution = 1h
param:id id in dot noation e.g. 'water.white.level.sb'
param:start epoch
param:stop epoch
result dict()


getInfo5Min
-----------


* params: id,start,stop,epoch2human
* path:/baselib/statmanager/StatManager.py (line:327)


return raw info (resolution is 5min)
param:id id in dot noation e.g. 'water.white.level.sb' (can be multiple use comma as separation)
param:start epoch; 0 means all
param:stop epoch; 0 means all
result list(list)  [epoch,value <epoch,value>,epoch,value <epoch,value>,...]


getInfo5MinFromTo
-----------------


* params: id,start,stop
* path:/baselib/statmanager/StatManager.py (line:296)


will not return more than 1 month of info
param:id id in dot noation e.g. 'water.white.level.sb'
param:start epoch
param:stop epoch
result list with values


getInfoWithHeaders
------------------


* params: id,start,stop,maxvalues
* path:/baselib/statmanager/StatManager.py (line:245)


param:id id in dot noation e.g. 'water.white.level.sb'  (can be multiple use comma as separation)
param:start epoch
param:stop epoch
param:maxvalues nr of values you want to return
result list(list)


getNrItemsRow
-------------


* params: key
* path:/baselib/statmanager/StatManager.py (line:56)




getTimeStamp
------------


* params: timestamp
* path:/baselib/statmanager/StatManager.py (line:291)


listHistoryObjects
------------------


* params:
* path:/baselib/statmanager/StatManager.py (line:190)


resampleList
------------


* params: llist,nritems
* path:/baselib/statmanager/StatManager.py (line:230)


reset
-----


* params:
* path:/baselib/statmanager/StatManager.py (line:44)


save
----


* params: force
* path:/baselib/statmanager/StatManager.py (line:68)


scheduleSaveClean
-----------------


* params:
* path:/baselib/statmanager/StatManager.py (line:35)


