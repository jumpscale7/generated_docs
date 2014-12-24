
j.system.process
================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/system/process.py>`_


appCheckActive
--------------


* params: appname
* path:/core/system/process.py (line:1788)


appGetPids
----------


* params: appname
* path:/core/system/process.py (line:1806)


appGetPidsActive
----------------


* params: appname
* path:/core/system/process.py (line:1849)


appNrInstances
--------------


* params: appname
* path:/core/system/process.py (line:1791)


appNrInstancesActive
--------------------


* params: appname
* path:/core/system/process.py (line:1794)


appsGet
-------


* params:
* path:/core/system/process.py (line:1835)


appsGetNames
------------


* params:
* path:/core/system/process.py (line:1815)


checkProcess
------------


* params: process,min
* path:/core/system/process.py (line:1646)


Check if a certain process is running on the system.
you can specify minimal running processes needed.
are trying to check



checkProcessForPid
------------------


* params: pid,process
* path:/core/system/process.py (line:1669)


Check whether a given pid actually does belong to a given process name.


checkstart
----------


* params: cmd,filterstr,nrtimes,retry
* path:/core/system/process.py (line:1544)



checkstop
---------


* params: cmd,filterstr,retry,nrinstances
* path:/core/system/process.py (line:1562)



execute
-------


* params: command,dieOnNonZeroExitCode,outputToStdout,useShell,ignoreErrorOutput
* path:/core/system/process.py (line:1300)


Executes a command, returns the exitcode and the output
if exitcode is not zero then the executed command returned with errors


executeAsync
------------


* params: command,args,printCommandToStdout,redirectStreams,argsInCommand,useShell,outputToStdout
* path:/core/system/process.py (line:1207)


Execute command asynchronous. By default, the input, output and error streams of the command will be piped to the returned Popen object. Be sure to call commands that don't expect user input, or send input to the stdin parameter of the returning Popen object.


executeCode
-----------


* params: code,params
* path:/core/system/process.py (line:1456)


execute a method (python code with def)
use params=j.core.params.get() as input


executeInSandbox
----------------


* params: command,timeout
* path:/core/system/process.py (line:1438)


Executes a command


executeIndependant
------------------


* params: cmd
* path:/core/system/process.py (line:1420)


executeScript
-------------


* params: scriptName
* path:/core/system/process.py (line:1428)


execute python script from shell/Interactive Window


executeWithoutPipe
------------------


* params: command,dieOnNonZeroExitCode,printCommandToStdout
* path:/core/system/process.py (line:1182)


Execute command without opening pipes, returns only the exitcode
This is platform independent
if exitcode is not zero then the executed command returned with errors


getDefunctProcesses
-------------------


* params:
* path:/core/system/process.py (line:1820)


getEnviron
----------


* params: pid
* path:/core/system/process.py (line:1797)


getMyProcessObject
------------------


* params:
* path:/core/system/process.py (line:1610)


getPidsByFilter
---------------


* params: filterstr
* path:/core/system/process.py (line:1529)


getPidsByPort
-------------


* params: port
* path:/core/system/process.py (line:1710)


Returns pid of the process that is listening on the given port


getProcessByPort
----------------


* params: port
* path:/core/system/process.py (line:1728)


Returns the full name of the process that is listening on the given port



getProcessObject
----------------


* params: pid
* path:/core/system/process.py (line:1613)


getProcessPid
-------------


* params: process
* path:/core/system/process.py (line:1585)


getProcessPidsFromUser
----------------------


* params: user
* path:/core/system/process.py (line:1620)


getSimularProcesses
-------------------


* params:
* path:/core/system/process.py (line:1633)


isPidAlive
----------


* params: pid
* path:/core/system/process.py (line:1505)


Checks whether this pid is alive.
For unix, a signal is sent to check that the process is alive.
For windows, the process information is retrieved and it is double checked that the process is python.exe
or pythonw.exe


kill
----


* params: pid,sig
* path:/core/system/process.py (line:19)


Kill a process with a signal


killProcessByName
-----------------


* params: name
* path:/core/system/process.py (line:1718)


killProcessByPort
-----------------


* params: port
* path:/core/system/process.py (line:1723)


killUserProcesses
-----------------


* params: user
* path:/core/system/process.py (line:1629)


run
---


* params: commandline,showOutput,captureOutput,maxSeconds,stopOnError,user,group
* path:/core/system/process.py (line:669)


Execute a command and wait for its termination

This function spawns a subprocess which executes the given command line in a
subshell. The function waits for the spawned process to terminate, or until
a time period of maxSeconds was exceeded.

When showOutput is set to True, stdin, stderr and stdout handles of the
subprocess are bound to the handles of the calling process. This can be used
to run interactive commands.

Both showOutput and captureOutput can't be True at the same time.

Any extra keyword arguments are passed to L{subprocess.Popen}. These
arguments can overwrite any argument set by this function, so setting any of
the arguments used by this function (including C{stdin}, C{stdout},
C{stderr}, C{env}, C{shell} and C{preexec_fn}) can change the behavior
of this function. This could e.g. be used to set C{cwd}.

The exit code contained in the returned tuple is the exit code of the
spawned process if equal to or larger than 0. If the subprocess was killed
while running, the exit code will be -1. If the process was stopped because
maxSeconds was exceeded, an exit code equal to -2 will be returned.

If user or group is defined (as name of number), the process will
setuid/setgid to this user and group before executing the command line,
effectively running the child process with the privileges of the provided
user and group.

Remarks:

* Don't use the '&' shell operator to run a process in the background, use

the startDaemon function instead

* Shell operators including pipes and redirects are allowed in the

command line string

* When spawning processes which generate large amounts of output, make sure

you set captureOutput to False, otherwise too much data will be buffered
in memory

* If captureOutput is set to False, the values of stdout and stderr in the

return value will be empty strings

* If stopOnError is set to True, the calling process will exit with exit

code 44 if the child process returned a non-zero exit code, or 45 if the
child process exceeds maxSeconds

allowed to run



runDaemon
---------


* params: commandline,stdout,stderr,user,group,env
* path:/core/system/process.py (line:1012)


Run an application as a background process

This function will execute the given commandline decoupled from the host
process by forking first. The stdout and stderr streams of the spawned
application can be redirected to files.

This can be compared to using

nohup myapplication -u -b 1 &

in a Bash shell.

If no stdout or stderr paths are provided, those streams are ignored.

If user or group is defined (as name of number), the daemon process will
setuid/setgid to this user and group before executing the child process,
effectively running the daemon process with the privileges of the provided
user and group.

If C{env} is provided, it will be used as environment in which the daemon
process will be executed. If it is not set, C{os.environ} will be used. Do
note C{PYTHONUNBUFFERED} and C{PYTHONPATH} will be slightly altered (in a
copy of the provided dictionary) by this function before spawning the
daemon process.




runScript
---------


* params: script,showOutput,captureOutput,maxSeconds,stopOnError
* path:/core/system/process.py (line:982)


Execute a Python script

This function executes a Python script, making sure the script output will
not be buffered.

For an overview of the parameters and function behaviour, see the
documentation of L{jumpscale.system.process.run}.






setEnvironmentVariable
----------------------


* params: varnames,varvalues
* path:/core/system/process.py (line:1696)


Set the value of the environment variables C{varnames}. Existing variable are overwritten



