
j.system.platform.diskmanager
=============================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/diskmanager/Diskmanager.py>`_


diskGetFreeRegions
------------------


* params: disk,align
* path:/lib/diskmanager/Diskmanager.py (line:122)


Get a filtered list of free regions, excluding the gaps due to partition alignment


mirrorsFind
-----------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:134)


partitionAdd
------------


* params: disk,free,align,length,fs_type,type
* path:/lib/diskmanager/Diskmanager.py (line:91)


partitionsFind
--------------


* params: mounted,ttype,ssd,prefix,minsize,maxsize,devbusy,initialize,forceinitialize
* path:/lib/diskmanager/Diskmanager.py (line:139)


looks for disks which are know to be data disks & are formatted ext4
return [$partpath,$size,$free,$ssd <$partpath,$size,$free,$ssd>]


partitionsFind_Ext4Data
-----------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:280)


looks for disks which are know to be data disks & are formatted ext4
return [$partpath,$gid,$partid,$size,$free <$partpath,$gid,$partid,$size,$free>]


partitionsGetMounted_Ext4Data
-----------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:302)


find disks which are mounted


partitionsMount_Ext4Data
------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:288)


partitionsUnmount_Ext4Data
--------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:295)


