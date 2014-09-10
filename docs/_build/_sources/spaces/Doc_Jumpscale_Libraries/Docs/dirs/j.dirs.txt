
j.dirs
======

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/Dirs.py>`_


Utility class to configure and store all relevant directory paths


addProtectedDir
---------------


* params: path,name
* path:/core/Dirs.py (line:260)


checkInProtectedDir
-------------------


* params: path
* path:/core/Dirs.py (line:293)


deployDefaultFilesInSandbox
---------------------------


* params:
* path:/core/Dirs.py (line:300)


getPathOfRunningFunction
------------------------


* params: function
* path:/core/Dirs.py (line:239)


init
----


* params: reinit
* path:/core/Dirs.py (line:196)


Initializes all the configured directories if needed

If a folder attribute is None, set its value to the corresponding
default path.



loadProtectedDirs
-----------------


* params:
* path:/core/Dirs.py (line:242)


removeProtectedDir
------------------


* params: path
* path:/core/Dirs.py (line:272)


replaceFilesDirVars
-------------------


* params: path,recursive,filter,additionalArgs
* path:/core/Dirs.py (line:179)


replaceTxtDirVars
-----------------


* params: txt,additionalArgs
* path:/core/Dirs.py (line:158)


replace $base,$vardir,$cfgdir,$bindir,$codedir,$tmpdir,$logdir,$appdir with props of this class


