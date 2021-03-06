
j.logger.redislogging.registered_client
=======================================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/redis/Redis.py>`_


append
------


* params: key,value
* path:/baselib/redis/Redis.py (line:766)


Appends the string `'value'` to the value at `'key'`. If `'key'`
doesn't already exist, create it with a value of `'value'`.
Returns the new length of the value at `'key'`.


bgrewriteaof
------------


* params:
* path:/baselib/redis/Redis.py (line:583)


Tell the Redis server to rewrite the AOF file from data in memory.


bgsave
------


* params:
* path:/baselib/redis/Redis.py (line:587)


Tell the Redis server to save its data to disk.  Unlike save(),
this method is asynchronous and returns immediately.


bitcount
--------


* params: key,start,end
* path:/baselib/redis/Redis.py (line:774)


Returns the count of set bits in the value of `'key'`.  Optional
`'start'` and `'end'` paramaters indicate which bytes to consider


bitop
-----


* params: operation,dest
* path:/baselib/redis/Redis.py (line:788)


Perform a bitwise operation using `'operation'` between `'keys'` and
store the result in `'dest'`.


bitpos
------


* params: key,bit,start,end
* path:/baselib/redis/Redis.py (line:795)


Return the position of the first bit set to 1 or 0 in a string.
`'start'` and `'end'` difines search range. The range is interpreted
as a range of bytes and not a range of bits, so start=0 and end=2
means to look at the first three bytes.


blpop
-----


* params: keys,timeout
* path:/baselib/redis/Redis.py (line:1128)


LPOP a value off of the first non-empty list
named in the `'keys'` list.

If none of the lists in `'keys'` has a value to LPOP, then block
for `'timeout'` seconds, or until a value gets pushed on to one
of the lists.

If timeout is 0, then block indefinitely.


brpop
-----


* params: keys,timeout
* path:/baselib/redis/Redis.py (line:1148)


RPOP a value off of the first non-empty list
named in the `'keys'` list.

If none of the lists in `'keys'` has a value to LPOP, then block
for `'timeout'` seconds, or until a value gets pushed on to one
of the lists.

If timeout is 0, then block indefinitely.


brpoplpush
----------


* params: src,dst,timeout
* path:/baselib/redis/Redis.py (line:1168)


Pop a value off the tail of `'src'`, push it on the head of `'dst'`
and then return it.

This command blocks until a value is in `'src'` or until `'timeout'`
seconds elapse, whichever is first. A `'timeout'` value of 0 blocks
forever.


client_getname
--------------


* params:
* path:/baselib/redis/Redis.py (line:602)


Returns the current connection name


client_kill
-----------


* params: address
* path:/baselib/redis/Redis.py (line:594)


Disconnects the client at `'address'` (ip:port)


client_list
-----------


* params:
* path:/baselib/redis/Redis.py (line:598)


Returns a list of currently connected clients


client_setname
--------------


* params: name
* path:/baselib/redis/Redis.py (line:606)


Sets the current connection name


config_get
----------


* params: pattern
* path:/baselib/redis/Redis.py (line:610)


Return a dictionary of configuration based on the `'pattern'`


config_resetstat
----------------


* params:
* path:/baselib/redis/Redis.py (line:618)


Reset runtime statistics


config_rewrite
--------------


* params:
* path:/baselib/redis/Redis.py (line:622)


Rewrite config file with the minimal change to reflect running config


config_set
----------


* params: name,value
* path:/baselib/redis/Redis.py (line:614)


Set config item `'name'` with `'value'`


dbsize
------


* params:
* path:/baselib/redis/Redis.py (line:626)


Returns the number of keys in the current database


debug_object
------------


* params: key
* path:/baselib/redis/Redis.py (line:630)


Returns version specific meta information about a given key


decr
----


* params: name,amount
* path:/baselib/redis/Redis.py (line:815)


Decrements the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as 0 - `'amount'`


delete
------


* params:
* path:/baselib/redis/Redis.py (line:822)


Delete one or more keys specified by `'names'`


dump
----


* params: name
* path:/baselib/redis/Redis.py (line:829)


Return a serialized version of the value stored at the specified key.
If key does not exist a nil bulk reply is returned.


echo
----


* params: value
* path:/baselib/redis/Redis.py (line:634)


Echo the string back from the server


eval
----


* params: script,numkeys
* path:/baselib/redis/Redis.py (line:1890)


Execute the Lua `'script'`, specifying the `'numkeys'` the script
will touch and the key names and argument values in `'keys_and_args'`.
Returns the result of the script.

In practice, use the object returned by `'register_script'`. This
function exists purely for Redis API completion.


evalsha
-------


* params: sha,numkeys
* path:/baselib/redis/Redis.py (line:1901)


Use the `'sha'` to execute a Lua script already registered via EVAL
or SCRIPT LOAD. Specify the `'numkeys'` the script will touch and the
key names and argument values in `'keys_and_args'`. Returns the result
of the script.

In practice, use the object returned by `'register_script'`. This
function exists purely for Redis API completion.


execute_command
---------------


* params:
* path:/baselib/redis/Redis.py (line:558)


Execute a command and return a parsed response


exists
------


* params: name
* path:/baselib/redis/Redis.py (line:836)


Returns a boolean indicating whether key `'name'` exists


expire
------


* params: name,time
* path:/baselib/redis/Redis.py (line:841)


Set an expire flag on key `'name'` for `'time'` seconds. `'time'`
can be represented by an integer or a Python timedelta object.


expireat
--------


* params: name,when
* path:/baselib/redis/Redis.py (line:850)


Set an expire flag on key `'name'`. `'when'` can be represented
as an integer indicating unix time or a Python datetime object.


flushall
--------


* params:
* path:/baselib/redis/Redis.py (line:638)


Delete all keys in all databases on the current host


flushdb
-------


* params:
* path:/baselib/redis/Redis.py (line:642)


Delete all keys in the current database


from_url
--------


* params: cls,url,db
* path:/baselib/redis/Redis.py (line:365)


Return a Redis client object configured from the given URL.

For example::

redis://`:password <:password>`_@localhost:6379/0
unix://`:password <:password>`_@/path/to/socket.sock?db=0

There are several ways to specify a database number. The parse function
will return the first specified option:
1. A `'db'` querystring option, e.g. redis://localhost?db=0
2. If using the redis:// scheme, the path argument of the url, e.g.
redis://localhost/0
3. The `'db'` argument to this function.

If none of these options are specified, db=0 is used.

Any additional querystring arguments and keyword arguments will be
passed along to the ConnectionPool class's initializer. In the case
of conflicting arguments, querystring arguments always win.


get
---


* params: name
* path:/baselib/redis/Redis.py (line:859)


Return the value at key `'name'`, or None if the key doesn't exist


getDict
-------


* params: key
* path:/baselib/redis/Redis.py (line:54)


getQueue
--------


* params: name,namespace
* path:/baselib/redis/Redis.py (line:57)


getbit
------


* params: name,offset
* path:/baselib/redis/Redis.py (line:875)


Returns a boolean indicating the value of `'offset'` in `'name'`


getrange
--------


* params: key,start,end
* path:/baselib/redis/Redis.py (line:879)


Returns the substring of the string value stored at `'key'`,
determined by the offsets `'start'` and `'end'` (both are inclusive)


getset
------


* params: name,value
* path:/baselib/redis/Redis.py (line:886)


Sets the value at key `'name'` to `'value'`
and returns the old value at key `'name'` atomically.


hdel
----


* params: name
* path:/baselib/redis/Redis.py (line:1814)


Delete `'keys'` from hash `'name'`


hexists
-------


* params: name,key
* path:/baselib/redis/Redis.py (line:1818)


Returns a boolean indicating if `'key'` exists within hash `'name'`


hget
----


* params: name,key
* path:/baselib/redis/Redis.py (line:1822)


Return the value of `'key'` within the hash `'name'`


hgetall
-------


* params: name
* path:/baselib/redis/Redis.py (line:1826)


Return a Python dict of the hash's name/value pairs


hgetalldict
-----------


* params: name
* path:/baselib/redis/Redis.py (line:1826)


Return a Python dict of the hash's name/value pairs


hincrby
-------


* params: name,key,amount
* path:/baselib/redis/Redis.py (line:1830)


Increment the value of `'key'` in hash `'name'` by `'amount'`


hincrbyfloat
------------


* params: name,key,amount
* path:/baselib/redis/Redis.py (line:1834)


Increment the value of `'key'` in hash `'name'` by floating `'amount'`


hkeys
-----


* params: name
* path:/baselib/redis/Redis.py (line:1840)


Return the list of keys within hash `'name'`


hlen
----


* params: name
* path:/baselib/redis/Redis.py (line:1844)


Return the number of elements in hash `'name'`


hmget
-----


* params: name,keys
* path:/baselib/redis/Redis.py (line:1874)


Returns a list of values ordered identically to `'keys'`


hmset
-----


* params: name,mapping
* path:/baselib/redis/Redis.py (line:1862)


Set key to value within hash `'name'` for each corresponding
key and value from the `'mapping'` dict.


hscan
-----


* params: name,cursor,match,count
* path:/baselib/redis/Redis.py (line:1402)


Incrementally return key/value slices in a hash. Also return a cursor
indicating the scan position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


hscan_iter
----------


* params: name,match,count
* path:/baselib/redis/Redis.py (line:1418)


Make an iterator using the HSCAN command so that the client doesn't
need to remember the cursor position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


hset
----


* params: name,key,value
* path:/baselib/redis/Redis.py (line:1848)


Set `'key'` to `'value'` within hash `'name'`
Returns 1 if HSET created a new field, otherwise 0


hsetnx
------


* params: name,key,value
* path:/baselib/redis/Redis.py (line:1855)


Set `'key'` to `'value'` within hash `'name'` if `'key'` does not
exist.  Returns 1 if HSETNX created a field, otherwise 0.


hvals
-----


* params: name
* path:/baselib/redis/Redis.py (line:1879)


Return the list of values within hash `'name'`


incr
----


* params: name,amount
* path:/baselib/redis/Redis.py (line:893)


Increments the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as `'amount'`


incrby
------


* params: name,amount
* path:/baselib/redis/Redis.py (line:900)


Increments the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as `'amount'`


incrbyfloat
-----------


* params: name,amount
* path:/baselib/redis/Redis.py (line:910)


Increments the value at key `'name'` by floating `'amount'`.
If no key exists, the value will be initialized as `'amount'`


info
----


* params: section
* path:/baselib/redis/Redis.py (line:646)


Returns a dictionary containing information about the Redis server

The `'section'` option can be used to select a specific section
of information

The section option is not supported by older versions of Redis Server,
and will generate ResponseError


keys
----


* params: pattern
* path:/baselib/redis/Redis.py (line:917)


Returns a list of keys matching `'pattern'`


lastsave
--------


* params:
* path:/baselib/redis/Redis.py (line:661)


Return a Python datetime object representing the last time the
Redis database was saved to disk


lindex
------


* params: name,index
* path:/baselib/redis/Redis.py (line:1181)


Return the item from list `'name'` at position `'index'`

Negative indexes are supported and will return an item at the
end of the list


linsert
-------


* params: name,where,refvalue,value
* path:/baselib/redis/Redis.py (line:1190)


Insert `'value'` in list `'name'` either immediately before or after
``'where'` <`'where'`>`_ `'refvalue'`

Returns the new length of the list on success or -1 if `'refvalue'`
is not in the list.


llen
----


* params: name
* path:/baselib/redis/Redis.py (line:1200)


Return the length of the list `'name'`


lock
----


* params: name,timeout,sleep,blocking_timeout,lock_class,thread_local
* path:/baselib/redis/Redis.py (line:490)


Return a new Lock object using key `'name'` that mimics
the behavior of threading.Lock.

If specified, `'timeout'` indicates a maximum life for the lock.
By default, it will remain locked until release() is called.

`'sleep'` indicates the amount of time to sleep per loop iteration
when the lock is in blocking mode and another client is currently
holding the lock.

`'blocking_timeout'` indicates the maximum amount of time in seconds to
spend trying to acquire the lock. A value of `'None'` indicates
continue trying forever. `'blocking_timeout'` can be specified as a
float or integer, both representing the number of seconds to wait.

`'lock_class'` forces the specified lock implementation.

`'thread_local'` indicates whether the lock token is placed in
thread-local storage. By default, the token is placed in thread local
storage so that a thread only sees its token, not a token set by
another thread. Consider the following timeline:

time: 0, thread-1 acquires 'my-lock', with a timeout of 5 seconds.
thread-1 sets the token to "abc"
time: 1, thread-2 blocks trying to acquire 'my-lock' using the
Lock instance.
time: 5, thread-1 has not yet completed. redis expires the lock
key.
time: 5, thread-2 acquired 'my-lock' now that it's available.
thread-2 sets the token to "xyz"
time: 6, thread-1 finishes its work and calls release(). if the
token is *not* stored in thread local storage, then
thread-1 would see the token value as "xyz" and would be
able to successfully release the thread-2's lock.

In some use cases it's necessary to disable thread local storage. For
example, if you have code where one thread acquires a lock and passes
that lock instance to a worker thread to release later. If thread
local storage isn't disabled in this case, the worker thread won't see
the token set by the thread that acquired the lock. Our assumption
is that these cases aren't common and as such default to using
thread local storage.


lpop
----


* params: name
* path:/baselib/redis/Redis.py (line:1204)


Remove and return the first item of the list `'name'`


lpush
-----


* params: name
* path:/baselib/redis/Redis.py (line:1208)


Push `'values'` onto the head of the list `'name'`


lpushx
------


* params: name,value
* path:/baselib/redis/Redis.py (line:1212)


Push `'value'` onto the head of the list `'name'` if `'name'` exists


lrange
------


* params: name,start,end
* path:/baselib/redis/Redis.py (line:1216)


Return a slice of the list `'name'` between
position `'start'` and `'end'`

`'start'` and `'end'` can be negative numbers just like
Python slicing notation


lrem
----


* params: name,value,num
* path:/baselib/redis/Redis.py (line:1983)


Remove the first `'num'` occurrences of elements equal to `'value'`
from the list stored at `'name'`.

The `'num'` argument influences the operation in the following ways:
num > 0: Remove elements equal to value moving from head to tail.
num < 0: Remove elements equal to value moving from tail to head.
num = 0: Remove all elements equal to value.


lset
----


* params: name,index,value
* path:/baselib/redis/Redis.py (line:1238)


Set `'position'` of list `'name'` to `'value'`


ltrim
-----


* params: name,start,end
* path:/baselib/redis/Redis.py (line:1242)


Trim the list `'name'`, removing all values not within the slice
between `'start'` and `'end'`

`'start'` and `'end'` can be negative numbers just like
Python slicing notation


mget
----


* params: keys
* path:/baselib/redis/Redis.py (line:921)


Returns a list of values ordered identically to `'keys'`


move
----


* params: name,db
* path:/baselib/redis/Redis.py (line:958)


Moves the key `'name'` to a different Redis database `'db'`


mset
----


* params:
* path:/baselib/redis/Redis.py (line:928)


Sets key/values based on a mapping. Mapping can be supplied as a single
dictionary argument or as kwargs.


msetnx
------


* params:
* path:/baselib/redis/Redis.py (line:942)


Sets key/values based on a mapping if none of the keys are already set.
Mapping can be supplied as a single dictionary argument or as kwargs.
Returns a boolean indicating if the operation was successful.


object
------


* params: infotype,key
* path:/baselib/redis/Redis.py (line:668)


Return the encoding, idletime, or refcount about the key


parse_response
--------------


* params: connection,command_name
* path:/baselib/redis/Redis.py (line:575)


Parses a response from the Redis server


persist
-------


* params: name
* path:/baselib/redis/Redis.py (line:962)


Removes an expiration on `'name'`


pexpire
-------


* params: name,time
* path:/baselib/redis/Redis.py (line:966)


Set an expire flag on key `'name'` for `'time'` milliseconds.
`'time'` can be represented by an integer or a Python timedelta
object.


pexpireat
---------


* params: name,when
* path:/baselib/redis/Redis.py (line:977)


Set an expire flag on key `'name'`. `'when'` can be represented
as an integer representing unix time in milliseconds (unix time * 1000)
or a Python datetime object.


pfadd
-----


* params: name
* path:/baselib/redis/Redis.py (line:1798)


Adds the specified elements to the specified HyperLogLog.


pfcount
-------


* params: name
* path:/baselib/redis/Redis.py (line:1802)


Return the approximated cardinality of
the set observed by the HyperLogLog at key.


pfmerge
-------


* params: dest
* path:/baselib/redis/Redis.py (line:1809)


Merge N different HyperLogLogs into a single one.


ping
----


* params:
* path:/baselib/redis/Redis.py (line:672)


Ping the Redis server


pipeline
--------


* params: transaction,shard_hint
* path:/baselib/redis/Redis.py (line:1959)


Return a new pipeline object that can queue multiple commands for
later execution. `'transaction'` indicates whether all commands
should be executed atomically. Apart from making a group of operations
atomic, pipelines are useful for reducing the back-and-forth overhead
between the client and server.


psetex
------


* params: name,time_ms,value
* path:/baselib/redis/Redis.py (line:988)


Set the value of key `'name'` to `'value'` that expires in `'time_ms'`
milliseconds. `'time_ms'` can be represented by an integer or a Python
timedelta object


pttl
----


* params: name
* path:/baselib/redis/Redis.py (line:999)


Returns the number of milliseconds until the key `'name'` will expire


publish
-------


* params: channel,message
* path:/baselib/redis/Redis.py (line:1883)


Publish `'message'` on `'channel'`.
Returns the number of subscribers the message was delivered to.


pubsub
------


* params:
* path:/baselib/redis/Redis.py (line:549)


Return a Publish/Subscribe object. With this object, you can
subscribe to channels and listen for messages that get published to
them.


randomkey
---------


* params:
* path:/baselib/redis/Redis.py (line:1003)


Returns the name of a random key


register_script
---------------


* params: script
* path:/baselib/redis/Redis.py (line:1933)


Register a Lua `'script'` specifying the `'keys'` it will touch.
Returns a Script object that is callable and hides the complexity of
deal with scripts, keys, and shas. This is the preferred way to work
with Lua scripts.


rename
------


* params: src,dst
* path:/baselib/redis/Redis.py (line:1007)


Rename key `'src'` to `'dst'`


renamenx
--------


* params: src,dst
* path:/baselib/redis/Redis.py (line:1013)


Rename key `'src'` to `'dst'` if `'dst'` doesn't already exist


restore
-------


* params: name,ttl,value
* path:/baselib/redis/Redis.py (line:1017)


Create a key using the provided serialized value, previously obtained
using DUMP.


rpop
----


* params: name
* path:/baselib/redis/Redis.py (line:1252)


Remove and return the last item of the list `'name'`


rpoplpush
---------


* params: src,dst
* path:/baselib/redis/Redis.py (line:1256)


RPOP a value off of the `'src'` list and atomically LPUSH it
on to the `'dst'` list.  Returns the value.


rpush
-----


* params: name
* path:/baselib/redis/Redis.py (line:1263)


Push `'values'` onto the tail of the list `'name'`


rpushx
------


* params: name,value
* path:/baselib/redis/Redis.py (line:1267)


Push `'value'` onto the tail of the list `'name'` if `'name'` exists


sadd
----


* params: name
* path:/baselib/redis/Redis.py (line:1475)


Add `'value(s)'` to set `'name'`


save
----


* params:
* path:/baselib/redis/Redis.py (line:676)


Tell the Redis server to save its data to disk,
blocking until the save is complete


scan
----


* params: cursor,match,count
* path:/baselib/redis/Redis.py (line:1339)


Incrementally return lists of key names. Also return a cursor
indicating the scan position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


scan_iter
---------


* params: match,count
* path:/baselib/redis/Redis.py (line:1355)


Make an iterator using the SCAN command so that the client doesn't
need to remember the cursor position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


scard
-----


* params: name
* path:/baselib/redis/Redis.py (line:1479)


Return the number of elements in set `'name'`


script_exists
-------------


* params:
* path:/baselib/redis/Redis.py (line:1913)


Check if a script exists in the script cache by specifying the SHAs of
each script as `'args'`. Returns a list of boolean values indicating if
if each already script exists in the cache.


script_flush
------------


* params:
* path:/baselib/redis/Redis.py (line:1921)


Flush all scripts from the script cache


script_kill
-----------


* params:
* path:/baselib/redis/Redis.py (line:1925)


Kill the currently executing Lua script


script_load
-----------


* params: script
* path:/baselib/redis/Redis.py (line:1929)


Load a Lua `'script'` into the script cache. Returns the SHA.


sdiff
-----


* params: keys
* path:/baselib/redis/Redis.py (line:1483)


Return the difference of sets specified by `'keys'`


sdiffstore
----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1488)


Store the difference of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


sentinel
--------


* params:
* path:/baselib/redis/Redis.py (line:683)


Redis Sentinel's SENTINEL command.


sentinel_get_master_addr_by_name
--------------------------------


* params: service_name
* path:/baselib/redis/Redis.py (line:688)


Returns a (host, port) pair for the given `'service_name'`


sentinel_master
---------------


* params: service_name
* path:/baselib/redis/Redis.py (line:693)


Returns a dictionary containing the specified masters state.


sentinel_masters
----------------


* params:
* path:/baselib/redis/Redis.py (line:697)


Returns a list of dictionaries containing each master's state.


sentinel_monitor
----------------


* params: name,ip,port,quorum
* path:/baselib/redis/Redis.py (line:701)


Add a new master to Sentinel to be monitored


sentinel_remove
---------------


* params: name
* path:/baselib/redis/Redis.py (line:705)


Remove a master from Sentinel's monitoring


sentinel_sentinels
------------------


* params: service_name
* path:/baselib/redis/Redis.py (line:709)


Returns a list of sentinels for `'service_name'`


sentinel_set
------------


* params: name,option,value
* path:/baselib/redis/Redis.py (line:713)


Set Sentinel monitoring parameters for a given master


sentinel_slaves
---------------


* params: service_name
* path:/baselib/redis/Redis.py (line:717)


Returns a list of slaves for `'service_name'`


set
---


* params: name,value,ex,px,nx,xx
* path:/baselib/redis/Redis.py (line:1024)


Set the value at key `'name'` to `'value'`

`'ex'` sets an expire flag on key `'name'` for `'ex'` seconds.

`'px'` sets an expire flag on key `'name'` for `'px'` milliseconds.

`'nx'` if set to True, set the value at key `'name'` to `'value'` if it
does not already exist.

`'xx'` if set to True, set the value at key `'name'` to `'value'` if it
already exists.


set_response_callback
---------------------


* params: command,callback
* path:/baselib/redis/Redis.py (line:453)


Set a custom Response Callback


setbit
------


* params: name,offset,value
* path:/baselib/redis/Redis.py (line:1060)


Flag the `'offset'` in `'name'` as `'value'`. Returns a boolean
indicating the previous value of `'offset'`.


setex
-----


* params: name,value,time
* path:/baselib/redis/Redis.py (line:1973)


Set the value of key `'name'` to `'value'` that expires in `'time'`
seconds. `'time'` can be represented by an integer or a Python
timedelta object.


setnx
-----


* params: name,value
* path:/baselib/redis/Redis.py (line:1078)


Set the value of key `'name'` to `'value'` if key doesn't exist


setrange
--------


* params: name,offset,value
* path:/baselib/redis/Redis.py (line:1082)


Overwrite bytes in the value of `'name'` starting at `'offset'` with
`'value'`. If `'offset'` plus the length of `'value'` exceeds the
length of the original value, the new value will be larger than before.
If `'offset'` exceeds the length of the original value, null bytes
will be used to pad between the end of the previous value and the start
of what's being injected.

Returns the length of the new string.


shutdown
--------


* params:
* path:/baselib/redis/Redis.py (line:721)


Shutdown the server


sinter
------


* params: keys
* path:/baselib/redis/Redis.py (line:1496)


Return the intersection of sets specified by `'keys'`


sinterstore
-----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1501)


Store the intersection of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


sismember
---------


* params: name,value
* path:/baselib/redis/Redis.py (line:1509)


Return a boolean indicating if `'value'` is a member of set `'name'`


slaveof
-------


* params: host,port
* path:/baselib/redis/Redis.py (line:730)


Set the server to be a replicated slave of the instance identified
by the `'host'` and `'port'`. If called without arguments, the
instance is promoted to a master instead.


slowlog_get
-----------


* params: num
* path:/baselib/redis/Redis.py (line:740)


Get the entries from the slowlog. If `'num'` is specified, get the
most recent `'num'` items.


slowlog_len
-----------


* params:
* path:/baselib/redis/Redis.py (line:750)


Get the number of items in the slowlog


slowlog_reset
-------------


* params:
* path:/baselib/redis/Redis.py (line:754)


Remove all items in the slowlog


smembers
--------


* params: name
* path:/baselib/redis/Redis.py (line:1513)


Return all members of the set `'name'`


smove
-----


* params: src,dst,value
* path:/baselib/redis/Redis.py (line:1517)


Move `'value'` from set `'src'` to set `'dst'` atomically


sort
----


* params: name,start,num,by,get,desc,alpha,store,groups
* path:/baselib/redis/Redis.py (line:1271)


Sort and return the list, set or sorted set at `'name'`.

`'start'` and `'num'` allow for paging through the sorted data

`'by'` allows using an external key to weight and sort the items.
Use an "*" to indicate where in the key the item value is located

`'get'` allows for returning items from external keys rather than the
sorted data itself.  Use an "*" to indicate where int he key
the item value is located

`'desc'` allows for reversing the sort

`'alpha'` allows for sorting lexicographically rather than numerically

`'store'` allows for storing the result of the sort into
the key `'store'`

`'groups'` if set to True and if `'get'` contains at least two
elements, sort will return a list of tuples, each containing the
values fetched from the arguments to `'get'`.


spop
----


* params: name
* path:/baselib/redis/Redis.py (line:1521)


Remove and return a random member of set `'name'`


srandmember
-----------


* params: name,number
* path:/baselib/redis/Redis.py (line:1525)


If `'number'` is None, returns a random member of set `'name'`.

If `'number'` is supplied, returns a list of `'number'` random
memebers of set `'name'`. Note this is only available when running
Redis 2.6+.


srem
----


* params: name
* path:/baselib/redis/Redis.py (line:1536)


Remove `'values'` from set `'name'`


sscan
-----


* params: name,cursor,match,count
* path:/baselib/redis/Redis.py (line:1370)


Incrementally return lists of elements in a set. Also return a cursor
indicating the scan position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


sscan_iter
----------


* params: name,match,count
* path:/baselib/redis/Redis.py (line:1386)


Make an iterator using the SSCAN command so that the client doesn't
need to remember the cursor position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns


strlen
------


* params: name
* path:/baselib/redis/Redis.py (line:1095)


Return the number of bytes stored in the value of `'name'`


substr
------


* params: name,start,end
* path:/baselib/redis/Redis.py (line:1099)


Return a substring of the string at key `'name'`. `'start'` and `'end'`
are 0-based integers specifying the portion of the string to return.


sunion
------


* params: keys
* path:/baselib/redis/Redis.py (line:1540)


Return the union of sets specified by `'keys'`


sunionstore
-----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1545)


Store the union of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


time
----


* params:
* path:/baselib/redis/Redis.py (line:758)


Returns the server time as a 2-item tuple of ints:
(seconds since epoch, microseconds into this second).


transaction
-----------


* params: func
* path:/baselib/redis/Redis.py (line:471)


Convenience method for executing the callable 'func' as a transaction
while watching all keys specified in 'watches'. The 'func' callable
should expect a single argument which is a Pipeline object.


ttl
---


* params: name
* path:/baselib/redis/Redis.py (line:1106)


Returns the number of seconds until the key `'name'` will expire


type
----


* params: name
* path:/baselib/redis/Redis.py (line:1110)


Returns the type of key `'name'`


unwatch
-------


* params:
* path:/baselib/redis/Redis.py (line:1120)


Unwatches the value at key `'name'`, or None of the key doesn't exist


watch
-----


* params:
* path:/baselib/redis/Redis.py (line:1114)


Watches the values at keys `'names'`, or None if the key doesn't exist


zadd
----


* params: name
* path:/baselib/redis/Redis.py (line:1995)


NOTE: The order of arguments differs from that of the official ZADD
command. For backwards compatability, this method accepts arguments
in the form of name1, score1, name2, score2, while the official Redis
documents expects score1, name1, score2, name2.

If you're looking to use the standard syntax, consider using the
StrictRedis class. See the API Reference section of the docs for more
information.

Set any number of element-name, score pairs to the key `'name'`. Pairs
can be specified in two ways:

As *args, in the form of: name1, score1, name2, score2, ...
or as **kwargs, in the form of: name1=score1, name2=score2, ...

The following example would add four values to the 'my-key' key:
redis.zadd('my-key', 'name1', 1.1, 'name2', 2.2, name3=3.3, name4=4.4)


zcard
-----


* params: name
* path:/baselib/redis/Redis.py (line:1576)


Return the number of elements in the sorted set `'name'`


zcount
------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1580)


Returns the number of elements in the sorted set at key `'name'` with
a score between `'min'` and `'max'`.


zincrby
-------


* params: name,value,amount
* path:/baselib/redis/Redis.py (line:1587)


Increment the score of `'value'` in sorted set `'name'` by `'amount'`


zinterstore
-----------


* params: dest,keys,aggregate
* path:/baselib/redis/Redis.py (line:1591)


Intersect multiple sorted sets specified by `'keys'` into
a new sorted set, `'dest'`. Scores in the destination will be
aggregated based on the `'aggregate'`, or SUM if none is provided.


zlexcount
---------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1599)


Return the number of items in the sorted set `'name'` between the
lexicographical range `'min'` and `'max'`.


zrange
------


* params: name,start,end,desc,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1606)


Return a range of values from sorted set `'name'` between
`'start'` and `'end'` sorted in ascending order.

`'start'` and `'end'` can be negative, indicating the end of the range.

`'desc'` a boolean indicating whether to sort the results descendingly

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrangebylex
-----------


* params: name,min,max,start,num
* path:/baselib/redis/Redis.py (line:1633)


Return the lexicographical range of values from sorted set `'name'`
between `'min'` and `'max'`.

If `'start'` and `'num'` are specified, then return a slice of the
range.


zrangebyscore
-------------


* params: name,min,max,start,num,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1649)


Return a range of values from the sorted set `'name'` with scores
between `'min'` and `'max'`.

If `'start'` and `'num'` are specified, then return a slice
of the range.

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

'score_cast_func'` a callable used to cast the score return value


zrank
-----


* params: name,value
* path:/baselib/redis/Redis.py (line:1677)


Returns a 0-based value indicating the rank of `'value'` in sorted set
`'name'`


zrem
----


* params: name
* path:/baselib/redis/Redis.py (line:1684)


Remove member `'values'` from sorted set `'name'`


zremrangebylex
--------------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1688)


Remove all elements in the sorted set `'name'` between the
lexicographical range specified by `'min'` and `'max'`.

Returns the number of elements removed.


zremrangebyrank
---------------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1697)


Remove all elements in the sorted set `'name'` with ranks between
`'min'` and `'max'`. Values are 0-based, ordered from smallest score
to largest. Values can be negative indicating the highest scores.
Returns the number of elements removed


zremrangebyscore
----------------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1706)


Remove all elements in the sorted set `'name'` with scores
between `'min'` and `'max'`. Returns the number of elements removed.


zrevrange
---------


* params: name,start,end,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1713)


Return a range of values from sorted set `'name'` between
`'start'` and `'end'` sorted in descending order.

`'start'` and `'end'` can be negative, indicating the end of the range.

`'withscores'` indicates to return the scores along with the values
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrevrangebyscore
----------------


* params: name,max,min,start,num,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1735)


Return a range of values from the sorted set `'name'` with scores
between `'min'` and `'max'` in descending order.

If `'start'` and `'num'` are specified, then return a slice
of the range.

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrevrank
--------


* params: name,value
* path:/baselib/redis/Redis.py (line:1763)


Returns a 0-based value indicating the descending rank of
`'value'` in sorted set `'name'`


zscan
-----


* params: name,cursor,match,count,score_cast_func
* path:/baselib/redis/Redis.py (line:1434)


Incrementally return lists of elements in a sorted set. Also return a
cursor indicating the scan position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns

`'score_cast_func'` a callable used to cast the score return value


zscan_iter
----------


* params: name,match,count,score_cast_func
* path:/baselib/redis/Redis.py (line:1454)


Make an iterator using the ZSCAN command so that the client doesn't
need to remember the cursor position.

`'match'` allows for filtering the keys by pattern

`'count'` allows for hint the minimum number of returns

`'score_cast_func'` a callable used to cast the score return value


zscore
------


* params: name,value
* path:/baselib/redis/Redis.py (line:1770)


Return the score of element `'value'` in sorted set `'name'`


zunionstore
-----------


* params: dest,keys,aggregate
* path:/baselib/redis/Redis.py (line:1774)


Union multiple sorted sets specified by `'keys'` into
a new sorted set, `'dest'`. Scores in the destination will be
aggregated based on the `'aggregate'`, or SUM if none is provided.


