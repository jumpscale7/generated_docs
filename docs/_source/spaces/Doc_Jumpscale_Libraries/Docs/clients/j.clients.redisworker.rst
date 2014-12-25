
j.clients.redisworker
=====================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redisworker/RedisWorker.py>`_





checkJumpscriptQueue
--------------------


* params: jumpscript,queue
* path:/baselib/redisworker/RedisWorker.py (line:212)


this checks that jumpscripts are not executed twice when being scheduled recurring
one off jobs will always execute !!!


checkQueue
----------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:260)


deleteJob
---------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:397)


deleteJumpscripts
-----------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:142)


deleteProcessQueue
------------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:150)


deleteQueues
------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:146)


execFunction
------------


* params: method,_category,_organization,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:163)



execJobAsync
------------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:254)


execJumpscript
--------------


* params: jumpscriptid,jumpscript,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:229)



getFailedJobs
-------------


* params: queue,hoursago
* path:/baselib/redisworker/RedisWorker.py (line:358)


getJob
------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:124)


getJobLine
----------


* params: job,jobid
* path:/baselib/redisworker/RedisWorker.py (line:331)


getJumpscriptFromId
-------------------


* params: jscriptid
* path:/baselib/redisworker/RedisWorker.py (line:133)


getJumpscriptFromName
---------------------


* params: organization,name
* path:/baselib/redisworker/RedisWorker.py (line:154)


getQueuedJobs
-------------


* params: queue,asWikiTable
* path:/baselib/redisworker/RedisWorker.py (line:344)


removeJobs
----------


* params: hoursago,failed
* path:/baselib/redisworker/RedisWorker.py (line:378)


scheduleJob
-----------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:327)


waitJob
-------


* params: job,timeout
* path:/baselib/redisworker/RedisWorker.py (line:292)


