
j.system.btrfs
==============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/btrfs/BtrfsExtension.py>`_


deviceAdd
---------


* params: path,dev
* path:/lib/btrfs/BtrfsExtension.py (line:63)


Add a device to a filesystem.


deviceDelete
------------


* params: dev,path
* path:/lib/btrfs/BtrfsExtension.py (line:69)


Remove a device from a filesystem.


getSpaceUsage
-------------


* params: path
* path:/lib/btrfs/BtrfsExtension.py (line:82)


snapshotReadOnlyCreate
----------------------


* params: path,dest
* path:/lib/btrfs/BtrfsExtension.py (line:33)


Create a readonly snapshot


subvolumeCreate
---------------


* params: path,name
* path:/lib/btrfs/BtrfsExtension.py (line:40)


Create a subvolume in <dest> (or the current directory if not passed).


subvolumeDelete
---------------


* params: path,name
* path:/lib/btrfs/BtrfsExtension.py (line:47)


Delete the subvolume <name>.


subvolumeList
-------------


* params: path
* path:/lib/btrfs/BtrfsExtension.py (line:53)


List the snapshot/subvolume of a filesystem.


