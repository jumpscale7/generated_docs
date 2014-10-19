
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
* path:/baselib/startupmanager/StartupManager.py (line:841)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:845)


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
* path:/baselib/startupmanager/StartupManager.py (line:814)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:807)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:824)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:686)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:849)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:857)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:803)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:795)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:548)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:789)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:853)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:770)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:742)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:833)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:746)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:837)


