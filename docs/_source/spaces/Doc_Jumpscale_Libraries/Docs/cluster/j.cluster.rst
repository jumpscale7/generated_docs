
j.cluster
=========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/remote/cluster/ClusterFactory.py>`_


create
------


* params: clustername,domainname,ipaddresses,superadminpassword,superadminpasswords
* path:/baselib/remote/cluster/ClusterFactory.py (line:47)


domainname needs to be unique
clustername is only a name which makes it easy for you to remember and used to store in config file


delete
------


* params: clustername
* path:/baselib/remote/cluster/ClusterFactory.py (line:96)


Delete a cluster with clustername from the configuration


get
---


* params: clustername,domainname
* path:/baselib/remote/cluster/ClusterFactory.py (line:30)


return cluster for specified domain or shortname,
there needs to be a cluster defined already before otherwise no nodes will be found
config file which stores this info is at $qbasedir/cfg/jsconfig/clusterconfig.cfg
only one of th 2 params is required


list
----


* params:
* path:/baselib/remote/cluster/ClusterFactory.py (line:129)


return list of clusternames


listAvahiEnabledMachines
------------------------


* params:
* path:/baselib/remote/cluster/ClusterFactory.py (line:117)


