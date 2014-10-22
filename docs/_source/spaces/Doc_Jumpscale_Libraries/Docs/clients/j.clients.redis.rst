
j.clients.redis
===============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redis/Redis.py>`_





checkAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:109)


configureInstance
-----------------


* params: name,port,maxram,appendonly,snapshot,slave,ismaster,passwd
* path:/baselib/redis/Redis.py (line:187)


slave example: (192.168.10.10,8888,asecret)   (ip,port,secret)


deleteInstance
--------------


* params: name
* path:/baselib/redis/Redis.py (line:175)


emptyAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:120)


emptyInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:180)


getGeventRedisClient
--------------------


* params: ipaddr,port,fromcache,password
* path:/baselib/redis/Redis.py (line:74)


getGeventRedisQueue
-------------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:100)


getPort
-------


* params: name
* path:/baselib/redis/Redis.py (line:138)


getProcessPids
--------------


* params: name
* path:/baselib/redis/Redis.py (line:152)


getRedisClient
--------------


* params: ipaddr,port,password,fromcache
* path:/baselib/redis/Redis.py (line:84)


getRedisQueue
-------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:92)


startInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:172)


stopInstance
------------


* params: name
* path:/baselib/redis/Redis.py (line:165)


