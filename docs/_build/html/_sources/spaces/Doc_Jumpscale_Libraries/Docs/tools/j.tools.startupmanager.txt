
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
* path:/baselib/startupmanager/StartupManager.py (line:830)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:834)


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
* path:/baselib/startupmanager/StartupManager.py (line:804)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:798)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:813)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:686)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:838)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:846)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:794)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:786)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:548)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:780)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:842)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:761)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:742)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:822)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:746)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:826)


