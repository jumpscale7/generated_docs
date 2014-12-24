
j.application
=============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/Application.py>`_


connectRedis
------------


* params:
* path:/core/Application.py (line:50)


getAgentId
----------


* params:
* path:/core/Application.py (line:102)


getCPUUsage
-----------


* params:
* path:/core/Application.py (line:220)


try to get cpu usage, if it doesn't work will return 0
By default 0 for windows


getMemoryUsage
--------------


* params:
* path:/core/Application.py (line:244)


try to get memory usage, if it doesn't work will return 0i
By default 0 for windows


getUniqueMachineId
------------------


* params:
* path:/core/Application.py (line:269)


will look for network interface and return a hash calculated from lowest mac address from all physical nics


getWhoAmiStr
------------


* params:
* path:/core/Application.py (line:99)


initGrid
--------


* params:
* path:/core/Application.py (line:93)


initWhoAmI
----------


* params: reload
* path:/core/Application.py (line:58)


when in grid:
is gid,nid,pid


loadConfig
----------


* params:
* path:/core/Application.py (line:105)


start
-----


* params: name,appdir
* path:/core/Application.py (line:111)


Start the application

You can only stop the application with return code 0 by calling
j.Application.stop(). Don't call sys.exit yourself, don't try to run
to end-of-script, I will find you anyway!


stop
----


* params: exitcode,stop
* path:/core/Application.py (line:153)


Stop the application cleanly using a given exitcode



