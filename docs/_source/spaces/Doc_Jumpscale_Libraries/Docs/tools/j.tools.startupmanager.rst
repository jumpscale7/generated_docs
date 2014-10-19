
j.tools.startupmanager
======================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/startupmanager/StartupManager.py>`_


addProcess
----------


* params: name,cmd,args,env,numprocesses,priority,shell,workingdir,jpackage,domain,ports,autostart,reload_signal,user,stopcmd,pid,active,check,timeoutcheck,isJSapp,upstart,processfilterstr,stats,log
* path:/baselib/startupmanager/StartupManager.py (line:572)


disableProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:844)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:848)


exists
------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:732)


existsJPackage
--------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:753)


getDomains
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:737)


getProcessDef
-------------


* params: domain,name,fromkey
* path:/baselib/startupmanager/StartupManager.py (line:695)


getProcessDefs
--------------


* params: domain,name,system
* path:/baselib/startupmanager/StartupManager.py (line:706)


getProcessDefs4JPackage
-----------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:756)


getStatus
---------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:817)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:810)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:827)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:688)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:852)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:860)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:806)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:798)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:550)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:792)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:856)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:773)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:744)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:836)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:748)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:840)


