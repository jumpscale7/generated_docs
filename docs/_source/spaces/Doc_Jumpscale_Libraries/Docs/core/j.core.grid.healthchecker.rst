
j.core.grid.healthchecker
=========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/grid/gridhealthchecker/gridhealthchecker.py>`_


checkDBs
--------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:234)


checkDisks
----------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:454)


checkDisksAllNodes
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:402)


checkElasticSearch
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:195)


checkHeartbeatsAllNodes
-----------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:358)


checkProcessManager
-------------------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:384)


Check heartbeat on specified node, see if result came in osis


checkProcessManagerAllNodes
---------------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:343)


checkRedis
----------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:276)


checkRedisAllNodes
------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:259)


checkWorkers
------------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:313)


checkWorkersAllNodes
--------------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:303)


getGID
------


* params: id
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:45)


getName
-------


* params: id
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:37)


getNodes
--------


* params: activecheck
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:120)


cache in mem
list nodes from grid
list nodes from heartbeat
if gridnodes found not in heartbeat -> error
if heartbeat nodes found not in gridnodes -> error
all the ones found in self._nids (return if populated)


getWikiStatus
-------------


* params: status
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:271)


ping
----


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:430)


pingAllNodesAsync
-----------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:421)


pingAllNodesSync
----------------


* params: clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:412)


pingasync
---------


* params: nid,clean
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:442)


runAll
------


* params:
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:143)


runAllOnNode
------------


* params: nid
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:161)


toStdout
--------


* params:
* path:/grid/gridhealthchecker/gridhealthchecker.py (line:117)


