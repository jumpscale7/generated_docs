
j.clients.redisworker
=====================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redisworker/RedisWorker.py>`_





checkJumpscriptQueue
--------------------


* params: jumpscript,queue
* path:/baselib/redisworker/RedisWorker.py (line:215)


this checks that jumpscripts are not executed twice when being scheduled recurring
one off jobs will always execute !!!


checkQueue
----------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:259)


deleteJob
---------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:388)


deleteJumpscripts
-----------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:145)


deleteProcessQueue
------------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:153)


deleteQueues
------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:149)


execFunction
------------


* params: method,_category,_organization,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:166)



execJobAsync
------------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:253)


execJumpscript
--------------


* params: jumpscriptid,jumpscript,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:232)



getFailedJobs
-------------


* params: queue,hoursago
* path:/baselib/redisworker/RedisWorker.py (line:349)


getJob
------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:127)


getJobLine
----------


* params: job,jobid
* path:/baselib/redisworker/RedisWorker.py (line:322)


getJumpscriptFromId
-------------------


* params: jscriptid
* path:/baselib/redisworker/RedisWorker.py (line:136)


getJumpscriptFromName
---------------------


* params: organization,name
* path:/baselib/redisworker/RedisWorker.py (line:157)


getQueuedJobs
-------------


* params: queue,asWikiTable
* path:/baselib/redisworker/RedisWorker.py (line:335)


removeJobs
----------


* params: hoursago,failed
* path:/baselib/redisworker/RedisWorker.py (line:369)


scheduleJob
-----------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:318)


useCRedis
---------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:118)


waitJob
-------


* params: job,timeout
* path:/baselib/redisworker/RedisWorker.py (line:284)


