
j.tools.startupmanager
======================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/startupmanager/StartupManager.py>`_


addProcess
----------


* params: name,cmd,args,env,numprocesses,priority,shell,workingdir,jpackage,domain,ports,autostart,reload_signal,user,stopcmd,pid,active,check,timeoutcheck,isJSapp,upstart,processfilterstr,stats,log
* path:/baselib/startupmanager/StartupManager.py (line:600)


disableProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:887)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:891)


exists
------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:775)


existsJPackage
--------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:796)


getDomains
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:780)


getProcessDef
-------------


* params: domain,name,fromkey
* path:/baselib/startupmanager/StartupManager.py (line:737)


getProcessDefs
--------------


* params: domain,name,system
* path:/baselib/startupmanager/StartupManager.py (line:748)


getProcessDefs4JPackage
-----------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:799)


getStatus
---------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:860)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:853)


installRedisSystem
------------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:563)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:870)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:730)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:895)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:903)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:849)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:841)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:556)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:835)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:899)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:816)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:787)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:879)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:791)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:883)


