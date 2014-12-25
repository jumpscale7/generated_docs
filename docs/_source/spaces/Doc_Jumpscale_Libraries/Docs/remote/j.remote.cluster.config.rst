
j.remote.cluster.config
=======================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/config/ConfigLib.py>`_


add
---


* params: itemname,params
* path:/core/config/ConfigLib.py (line:317)


Add and configure `Cluster Configuration <Cluster Configuration>`_.


addClusterNode
--------------


* params: clustername,ipaddress
* path:/core/config/ConfigLib.py (line:69)


node with $ipaddress to add to cluster with name=$clustername


configure
---------


* params: itemname,newparams
* path:/core/config/ConfigLib.py (line:457)


Reconfigure or add a `%(description)s <%(description)s>`_ non-interactively.


getConfig
---------


* params: itemname
* path:/core/config/ConfigLib.py (line:391)


Get config dictionary for a `%(description)s <%(description)s>`_


list
----


* params:
* path:/core/config/ConfigLib.py (line:379)


List all `%(description)s <%(description)s>`_s


remove
------


* params: itemname
* path:/core/config/ConfigLib.py (line:439)


Remove `%(description)s <%(description)s>`_.


review
------


* params: itemname
* path:/core/config/ConfigLib.py (line:402)


In interactive mode: modify/review configuration of `%(description)s <%(description)s>`_.
In non-interactive mode: validate configuration of `%(description)s <%(description)s>`_.


saveAll
-------


* params:
* path:/core/config/ConfigLib.py (line:386)


show
----


* params: itemnames
* path:/core/config/ConfigLib.py (line:423)


Show `%(description)s <%(description)s>`_ configuration.


