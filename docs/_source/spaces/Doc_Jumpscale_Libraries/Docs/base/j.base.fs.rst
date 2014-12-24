
j.base.fs
=========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/base/FS.py>`_


copyDependencies
----------------


* params: path,dest
* path:/base/FS.py (line:106)


exists
------


* params: path
* path:/base/FS.py (line:85)


fileGetContents
---------------


* params: filename
* path:/base/FS.py (line:14)


Read a file and get contents of that file


findDependencies
----------------


* params: path,deps
* path:/base/FS.py (line:89)


isDir
-----


* params: path,followSoftlink
* path:/base/FS.py (line:24)


Check if the specified Directory path exists


isExecutable
------------


* params: path
* path:/base/FS.py (line:40)


isFile
------


* params: path,followSoftlink
* path:/base/FS.py (line:54)


Check if the specified file exists for the given path


list
----


* params: path
* path:/base/FS.py (line:70)


log
---


* params: msg
* path:/base/FS.py (line:10)


readLink
--------


* params: path
* path:/base/FS.py (line:45)


Works only for unix
Return a string representing the path to which the symbolic link points.


