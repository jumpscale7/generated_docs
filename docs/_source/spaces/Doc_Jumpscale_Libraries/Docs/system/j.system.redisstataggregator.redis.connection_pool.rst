
j.system.redisstataggregator.redis.connection_pool
==================================================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScalepython.zip//redis/connection.py>`_


Generic connection pool


disconnect
----------


* params:
* path:python.zip//redis/connection.py (line:895)


Disconnects all connections in the pool


from_url
--------


* params: cls,url,db
* path:python.zip//redis/connection.py (line:732)


Return a connection pool configured from the given URL.

For example::

redis://password <:password>@localhost:6379/0
rediss://password <:password>@localhost:6379/0
unix://password <:password>@/path/to/socket.sock?db=0

Three URL schemes are supported:
redis:// creates a normal TCP socket connection
rediss:// creates a SSL wrapped TCP socket connection
unix:// creates a Unix Domain Socket connection

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


get_connection
--------------


* params: command_name
* path:python.zip//redis/connection.py (line:870)


Get a connection from the pool


make_connection
---------------


* params:
* path:python.zip//redis/connection.py (line:880)


Create a new connection


release
-------


* params: connection
* path:python.zip//redis/connection.py (line:887)


Releases the connection back to the pool


reset
-----


* params:
* path:python.zip//redis/connection.py (line:853)


