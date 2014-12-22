
j.application.redis
===================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/credis/CRedis.py>`_


example for pipeline
self.execute_pipeline(('SET',"test","This Should Return"),('GET',"test"))


blpop
-----


* params: key,timeout
* path:/baselib/credis/CRedis.py (line:89)


brpoplpush
----------


* params: src,dst,timeout
* path:/baselib/credis/CRedis.py (line:143)


connect
-------


* params:
* path:/baselib/credis/CRedis.py (line:52)


delete
------


* params: key
* path:/baselib/credis/CRedis.py (line:134)


eval
----


* params: script,nrkeys
* path:/baselib/credis/CRedis.py (line:154)


evalsha
-------


* params: sha,nrkeys
* path:/baselib/credis/CRedis.py (line:151)


execute
-------


* params:
* path:/baselib/credis/CRedis.py (line:65)


exists
------


* params: key
* path:/baselib/credis/CRedis.py (line:101)


expire
------


* params: key,timeout
* path:/baselib/credis/CRedis.py (line:137)


get
---


* params: key
* path:/baselib/credis/CRedis.py (line:104)


getFallBackRedis
----------------


* params:
* path:/baselib/credis/CRedis.py (line:48)


hdel
----


* params: name
* path:/baselib/credis/CRedis.py (line:122)


hdelete
-------


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:119)


hexists
-------


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:125)


hget
----


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:113)


hgetall
-------


* params: hkey
* path:/baselib/credis/CRedis.py (line:116)


hincrby
-------


* params: name,key,amount
* path:/baselib/credis/CRedis.py (line:140)


hkeys
-----


* params: key
* path:/baselib/credis/CRedis.py (line:98)


hset
----


* params: hkey,key,value
* path:/baselib/credis/CRedis.py (line:110)


incr
----


* params: key
* path:/baselib/credis/CRedis.py (line:128)


incrby
------


* params: key,nr
* path:/baselib/credis/CRedis.py (line:131)


keys
----


* params: key
* path:/baselib/credis/CRedis.py (line:95)


llen
----


* params: key
* path:/baselib/credis/CRedis.py (line:83)


lpop
----


* params: key
* path:/baselib/credis/CRedis.py (line:92)


lrange
------


* params: name,start,end
* path:/baselib/credis/CRedis.py (line:157)


rpush
-----


* params: key,item
* path:/baselib/credis/CRedis.py (line:86)


scriptload
----------


* params: script
* path:/baselib/credis/CRedis.py (line:146)


set
---


* params: key,value
* path:/baselib/credis/CRedis.py (line:107)


