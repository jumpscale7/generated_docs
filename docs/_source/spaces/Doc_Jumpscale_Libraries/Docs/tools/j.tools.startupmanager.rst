
j.tools.startupmanager
======================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/startupmanager/StartupManager.py>`_


addProcess
----------


* params: name,cmd,args,env,numprocesses,priority,shell,workingdir,jpackage,domain,ports,autostart,reload_signal,user,stopcmd,pid,active,check,timeoutcheck,isJSapp,upstart,processfilterstr,stats,log
* path:/baselib/startupmanager/StartupManager.py (line:570)


disableProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:836)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:840)


exists
------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:730)


existsJPackage
--------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:751)


getDomains
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:735)


getProcessDef
-------------


* params: domain,name,fromkey
* path:/baselib/startupmanager/StartupManager.py (line:693)


getProcessDefs
--------------


* params: domain,name,system
* path:/baselib/startupmanager/StartupManager.py (line:704)


getProcessDefs4JPackage
-----------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:754)


getStatus
---------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:810)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:803)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:819)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:686)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:844)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:852)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:799)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:791)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:548)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:785)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:848)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:766)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:742)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:828)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:746)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:832)


