
j.errorconditionhandler
=======================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/errorhandling/ErrorConditionHandler.py>`_


checkErrorIgnore
----------------


* params: eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:388)


escalateBugToDeveloper
----------------------


* params: errorConditionObject,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:496)


excepthook
----------


* params: ttype,pythonExceptionObject,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:356)


every fatal error in jumpscale or by python itself will result in an exception
in this function the exception is caught.
This routine will create an errorobject & escalate to the infoserver


getErrorConditionObject
-----------------------


* params: ddict,msg,msgpub,category,level,type,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:226)


returns only ErrorConditionObject which should be used in jumpscale to define an errorcondition (or potential error condition)


getErrorTraceKIS
----------------


* params: tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:446)


getFrames
---------


* params: tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:403)


getLevelName
------------


* params: level
* path:/core/errorhandling/ErrorConditionHandler.py (line:400)


halt
----


* params: msg,eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:580)


lastActionClear
---------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:490)


clear last action so is not printed when error


lastActionSet
-------------


* params: lastActionDescription
* path:/core/errorhandling/ErrorConditionHandler.py (line:484)


will remember action you are doing, this will be added to error message if filled in


parsePythonErrorObject
----------------------


* params: pythonExceptionObject,ttype,tb,level,message
* path:/core/errorhandling/ErrorConditionHandler.py (line:255)


how to use

try:
except Exception,e:
eco=j.errorconditionhandler.parsePythonErrorObject(e)

eco is jumpscale internal format for an error
next step could be to process the error objecect (eco) e.g. by eco.process()




parsepythonExceptionObject
--------------------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:353)


processPythonExceptionObject
----------------------------


* params: pythonExceptionObject,ttype,tb,level,message,sentry
* path:/core/errorhandling/ErrorConditionHandler.py (line:235)


how to use

try:
except Exception,e:
j.errorconditionhandler.processpythonExceptionObject(e)



the errorcondition is then also processed e.g. send to local logserver and/or stored locally in errordb


raiseBug
--------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,die,tags,level
* path:/core/errorhandling/ErrorConditionHandler.py (line:97)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for
level will be Critical

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


raiseCritical
-------------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,die,tags,level
* path:/core/errorhandling/ErrorConditionHandler.py (line:97)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for
level will be Critical

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


raiseInputError
---------------


* params: message,category,msgpub,die,backtrace,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:191)


raiseMonitoringError
--------------------


* params: message,category,msgpub,die,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:210)


raiseOperationalCritical
------------------------


* params: message,category,msgpub,die,tags,eco,extra
* path:/core/errorhandling/ErrorConditionHandler.py (line:136)


use this to raise an operational issue about the system


raiseOperationalWarning
-----------------------


* params: message,category,msgpub,tags,eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:181)


raisePerformanceError
---------------------


* params: message,category,msgpub,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:218)


raiseRuntimeErrorWithEco
------------------------


* params: eco,tostdout
* path:/core/errorhandling/ErrorConditionHandler.py (line:169)


raiseWarning
------------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:119)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


reRaiseECO
----------


* params: eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:341)


setExceptHook
-------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:79)


toolStripNonAsciFromText
------------------------


* params: text
* path:/core/errorhandling/ErrorConditionHandler.py (line:76)


