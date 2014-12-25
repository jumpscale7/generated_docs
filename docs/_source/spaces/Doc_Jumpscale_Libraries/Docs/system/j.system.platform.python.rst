
j.system.platform.python
========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/jpackages/PythonPackage.py>`_


check
-----


* params:
* path:/baselib/jpackages/PythonPackage.py (line:41)


clearcache
----------


* params:
* path:/baselib/jpackages/PythonPackage.py (line:11)


copyLibToLocalSitePackagesDir
-----------------------------


* params: path,remove
* path:/baselib/jpackages/PythonPackage.py (line:122)


copy library to python.paths.local.sitepackages config param in main jumpscale hrd
eg. for ubuntu is: /usr/local/lib/python2.7/site-packages/
does this for 1 lib, so the dir needs to be the library by itself


copyLibsToLocalSitePackagesDir
------------------------------


* params: rootpath,remove
* path:/baselib/jpackages/PythonPackage.py (line:113)


list all files and dirs in specified path and for each one call
self.copyLibToLocalSitePackagesDir


getSitePackagePathLocal
-----------------------


* params:
* path:/baselib/jpackages/PythonPackage.py (line:104)


install
-------


* params: name,version,latest
* path:/baselib/jpackages/PythonPackage.py (line:44)


list
----


* params:
* path:/baselib/jpackages/PythonPackage.py (line:94)


remove
------


* params: names,clearcache
* path:/baselib/jpackages/PythonPackage.py (line:53)


will look in all possible python paths & remove the python lib


