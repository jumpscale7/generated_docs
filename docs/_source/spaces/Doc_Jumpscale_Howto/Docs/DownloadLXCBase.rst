

image location
--------------


images are on rsync server (today 16-4-2014: install.jumpscale.org)

param configured in: hrd
jssync.addr=95.85.60.252


key approach
------------


each image is uploaded to a location on rsync server prepended with this key,
this key can be a secret
in this example the key is an existing set of images underneath key:'test’

To update e.g. base image on key:test



prerequisites
=============


make sure lxc is properly installed (see `HowToUseLXCInstall <HowToUseLXCInstall>`_)

make sure jssync is installed




.. code-block:: python

  jpackage install -n jssync



download base machine
=====================




.. code-block:: python

  jsmachine importR -n base -m base -k test


(this means get image base from key:test onto local machine called  base)

machine is now under /mnt/btrfs/lxc/base/ (for these howto's we will always use /mnt/btrfs/lxc as base for lxc)

