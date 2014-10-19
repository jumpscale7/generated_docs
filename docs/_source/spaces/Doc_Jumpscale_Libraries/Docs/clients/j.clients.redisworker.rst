
j.clients.redisworker
=====================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redisworker/RedisWorker.py>`_





checkJumpscriptQueue
--------------------


* params: jumpscript,queue
* path:/baselib/redisworker/RedisWorker.py (line:224)


this checks that jumpscripts are not executed twice when being scheduled recurring
one off jobs will always execute !!!


checkQueue
----------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:272)


deleteJob
---------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:402)


deleteJumpscripts
-----------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:154)


deleteProcessQueue
------------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:162)


deleteQueues
------------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:158)


execFunction
------------


* params: method,_category,_organization,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:175)



execJobAsync
------------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:266)


execJumpscript
--------------


* params: jumpscriptid,jumpscript,_timeout,_queue,_log,_sync
* path:/baselib/redisworker/RedisWorker.py (line:241)



getFailedJobs
-------------


* params: queue,hoursago
* path:/baselib/redisworker/RedisWorker.py (line:363)


getJob
------


* params: jobid
* path:/baselib/redisworker/RedisWorker.py (line:136)


getJobLine
----------


* params: job,jobid
* path:/baselib/redisworker/RedisWorker.py (line:336)


getJumpscriptFromId
-------------------


* params: jscriptid
* path:/baselib/redisworker/RedisWorker.py (line:145)


getJumpscriptFromName
---------------------


* params: organization,name
* path:/baselib/redisworker/RedisWorker.py (line:166)


getQueuedJobs
-------------


* params: queue,asWikiTable
* path:/baselib/redisworker/RedisWorker.py (line:349)


init
----


* params:
* path:/baselib/redisworker/RedisWorker.py (line:89)


removeJobs
----------


* params: hoursago,failed
* path:/baselib/redisworker/RedisWorker.py (line:383)


scheduleJob
-----------


* params: job
* path:/baselib/redisworker/RedisWorker.py (line:332)


useCRedis
---------


* params:
* path:/baselib/redisworker/RedisWorker.py (line:126)


waitJob
-------


* params: job,timeout
* path:/baselib/redisworker/RedisWorker.py (line:297)


