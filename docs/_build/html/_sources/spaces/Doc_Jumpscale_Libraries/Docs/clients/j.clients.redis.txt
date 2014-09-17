
j.clients.redis
===============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redis/Redis.py>`_





checkAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:105)


configureInstance
-----------------


* params: name,port,maxram,appendonly,snapshot,slave,ismaster,passwd
* path:/baselib/redis/Redis.py (line:183)


slave example: (192.168.10.10,8888,asecret)   (ip,port,secret)


deleteInstance
--------------


* params: name
* path:/baselib/redis/Redis.py (line:171)


emptyAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:116)


emptyInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:176)


getGeventRedisClient
--------------------


* params: ipaddr,port,fromcache,password
* path:/baselib/redis/Redis.py (line:74)


getGeventRedisQueue
-------------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:96)


getPort
-------


* params: name
* path:/baselib/redis/Redis.py (line:134)


getProcessPids
--------------


* params: name
* path:/baselib/redis/Redis.py (line:148)


getRedisClient
--------------


* params: ipaddr,port,password
* path:/baselib/redis/Redis.py (line:84)


getRedisQueue
-------------


* params: ipaddr,port,name,namespace
* path:/baselib/redis/Redis.py (line:90)


startInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:168)


stopInstance
------------


* params: name
* path:/baselib/redis/Redis.py (line:161)


