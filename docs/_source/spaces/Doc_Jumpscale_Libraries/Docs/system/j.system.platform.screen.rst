
j.system.platform.screen
========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/screen/Tmux.py>`_


attachSession
-------------


* params: sessionname,windowname,user
* path:/baselib/screen/Tmux.py (line:176)


createSession
-------------


* params: sessionname,screens,user
* path:/baselib/screen/Tmux.py (line:9)



createWindow
------------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:125)


executeInScreen
---------------


* params: sessionname,screenname,cmd,wait,cwd,env,user,tmuxuser
* path:/baselib/screen/Tmux.py (line:33)



getPid
------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:97)


getSessions
-----------


* params: user
* path:/baselib/screen/Tmux.py (line:88)


getWindows
----------


* params: session,attemps,user
* path:/baselib/screen/Tmux.py (line:111)


killSession
-----------


* params: sessionname,user
* path:/baselib/screen/Tmux.py (line:170)


killSessions
------------


* params: user
* path:/baselib/screen/Tmux.py (line:164)


killWindow
----------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:154)


logWindow
---------


* params: session,name,filename,user
* path:/baselib/screen/Tmux.py (line:135)


windowExists
------------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:142)


