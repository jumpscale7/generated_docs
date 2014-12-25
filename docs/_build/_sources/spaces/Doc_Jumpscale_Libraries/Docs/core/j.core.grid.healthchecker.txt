
j.core.grid.healthchecker
=========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/grid/gridhealthchecker/gridhealthchecker.py>`_


checkDisks
----------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:415)


checkDisksAllNodes
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:363)


checkElasticSearch
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:181)


checkHeartbeatsAllNodes
-----------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:319)


checkProcessManager
-------------------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:345)


Check heartbeat on specified node, see if result came in osis


checkProcessManagerAllNodes
---------------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:304)


checkRedis
----------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:237)


checkRedisAllNodes
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:220)


checkWorkers
------------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:274)


checkWorkersAllNodes
--------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:264)


getName
-------


* params: id
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:36)


getNodes
--------


* params: activecheck
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:110)


cache in mem
list nodes from grid
list nodes from heartbeat
if gridnodes found not in heartbeat -> error
if heartbeat nodes found not in gridnodes -> error
all the ones found in self._nids (return if populated)


getWikiStatus
-------------


* params: status
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:232)


ping
----


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:391)


pingAllNodesAsync
-----------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:382)


pingAllNodesSync
----------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:373)


pingasync
---------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:403)


runAll
------


* params:
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:132)


runAllOnNode
------------


* params: nid
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:149)


toStdout
--------


* params:
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:107)


