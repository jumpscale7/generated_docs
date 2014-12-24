
j.tools.docker
==============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/docker/Docker.py>`_


btrfsSubvolCopy
---------------


* params: nameFrom,NameDest
* path:/lib/docker/Docker.py (line:161)


btrfsSubvolDelete
-----------------


* params: name
* path:/lib/docker/Docker.py (line:176)


btrfsSubvolExists
-----------------


* params: name
* path:/lib/docker/Docker.py (line:170)


btrfsSubvolList
---------------


* params:
* path:/lib/docker/Docker.py (line:141)


btrfsSubvolNew
--------------


* params: name
* path:/lib/docker/Docker.py (line:155)


commit
------


* params: name,imagename
* path:/lib/docker/Docker.py (line:467)


create
------


* params: name,ports,vols,volsro,stdout,base,nameserver,replace,cpu,mem
* path:/lib/docker/Docker.py (line:250)



destroy
-------


* params: name
* path:/lib/docker/Docker.py (line:450)


destroyall
----------


* params:
* path:/lib/docker/Docker.py (line:432)


execute
-------


* params: command
* path:/lib/docker/Docker.py (line:22)


exportRsync
-----------


* params: name,backupname,key
* path:/lib/docker/Docker.py (line:121)


exportTgz
---------


* params: name,backupname
* path:/lib/docker/Docker.py (line:226)


getImages
---------


* params:
* path:/lib/docker/Docker.py (line:376)


getInfo
-------


* params: name
* path:/lib/docker/Docker.py (line:79)


getIp
-----


* params: name
* path:/lib/docker/Docker.py (line:85)


getProcessList
--------------


* params: name,stdout
* path:/lib/docker/Docker.py (line:89)


last one is sum of mem & cpu


getPubPortForInternalPort
-------------------------


* params: name,port
* path:/lib/docker/Docker.py (line:391)


getSSH
------


* params: name
* path:/lib/docker/Docker.py (line:425)


importRsync
-----------


* params: backupname,name,basename,key
* path:/lib/docker/Docker.py (line:195)



importTgz
---------


* params: backupname,name
* path:/lib/docker/Docker.py (line:239)


inspect
-------


* params: name
* path:/lib/docker/Docker.py (line:73)


list
----


* params:
* path:/lib/docker/Docker.py (line:58)


return list of names


ps
--


* params:
* path:/lib/docker/Docker.py (line:67)


return detailed info


pull
----


* params: imagename
* path:/lib/docker/Docker.py (line:473)


pushSSHKey
----------


* params: name
* path:/lib/docker/Docker.py (line:399)


removeRedundantFiles
--------------------


* params: name
* path:/lib/docker/Docker.py (line:187)


setHostName
-----------


* params: name
* path:/lib/docker/Docker.py (line:380)


stop
----


* params: name
* path:/lib/docker/Docker.py (line:461)


