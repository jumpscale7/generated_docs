
j.system.platform.diskmanager
=============================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/diskmanager/Diskmanager.py>`_


diskGetFreeRegions
------------------


* params: disk,align
* path:/lib/diskmanager/Diskmanager.py (line:123)


Get a filtered list of free regions, excluding the gaps due to partition alignment


mirrorsFind
-----------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:135)


partitionAdd
------------


* params: disk,free,align,length,fs_type,type
* path:/lib/diskmanager/Diskmanager.py (line:93)


partitionsFind
--------------


* params: mounted,ttype,ssd,prefix,minsize,maxsize,devbusy,initialize,forceinitialize
* path:/lib/diskmanager/Diskmanager.py (line:140)


looks for disks which are know to be data disks & are formatted ext4
return [`$partpath,$size,$free,$ssd <$partpath,$size,$free,$ssd>`_]


partitionsFind_Ext4Data
-----------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:278)


looks for disks which are know to be data disks & are formatted ext4
return [`$partpath,$gid,$partid,$size,$free <$partpath,$gid,$partid,$size,$free>`_]


partitionsGetMounted_Ext4Data
-----------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:300)


find disks which are mounted


partitionsMount_Ext4Data
------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:286)


partitionsUnmount_Ext4Data
--------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:293)


