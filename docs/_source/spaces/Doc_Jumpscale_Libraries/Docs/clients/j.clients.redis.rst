
j.clients.redis
===============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redis/Redis.py>`_





checkAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:125)


configureInstance
-----------------


* params: name,port,maxram,appendonly,snapshot,slave,ismaster,passwd
* path:/baselib/redis/Redis.py (line:203)


slave example: (192.168.10.10,8888,asecret)   (ip,port,secret)


deleteInstance
--------------


* params: name
* path:/baselib/redis/Redis.py (line:191)


emptyAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:136)


emptyInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:196)


getByInstanceName
-----------------


* params: instance,gevent
* path:/baselib/redis/Redis.py (line:95)


getGeventRedisClient
--------------------


* params: ipaddr,port,fromcache,password
* path:/baselib/redis/Redis.py (line:77)


getGeventRedisQueue
-------------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:116)


getPort
-------


* params: name
* path:/baselib/redis/Redis.py (line:154)


getProcessPids
--------------


* params: name
* path:/baselib/redis/Redis.py (line:168)


getRedisClient
--------------


* params: ipaddr,port,password,fromcache
* path:/baselib/redis/Redis.py (line:87)


getRedisQueue
-------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:108)


startInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:188)


stopInstance
------------


* params: name
* path:/baselib/redis/Redis.py (line:181)


