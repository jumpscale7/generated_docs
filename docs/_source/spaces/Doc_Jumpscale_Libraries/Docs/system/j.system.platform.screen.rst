
j.system.platform.screen
========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/screen/Tmux.py>`_


attachSession
-------------


* params: sessionname,windowname,user
* path:/baselib/screen/Tmux.py (line:177)


createSession
-------------


* params: sessionname,screens,user
* path:/baselib/screen/Tmux.py (line:9)



createWindow
------------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:126)


executeInScreen
---------------


* params: sessionname,screenname,cmd,wait,cwd,env,user,tmuxuser
* path:/baselib/screen/Tmux.py (line:33)



getPid
------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:98)


getSessions
-----------


* params: user
* path:/baselib/screen/Tmux.py (line:89)


getWindows
----------


* params: session,attemps,user
* path:/baselib/screen/Tmux.py (line:112)


killSession
-----------


* params: sessionname,user
* path:/baselib/screen/Tmux.py (line:171)


killSessions
------------


* params: user
* path:/baselib/screen/Tmux.py (line:165)


killWindow
----------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:155)


logWindow
---------


* params: session,name,filename,user
* path:/baselib/screen/Tmux.py (line:136)


windowExists
------------


* params: session,name,user
* path:/baselib/screen/Tmux.py (line:143)


