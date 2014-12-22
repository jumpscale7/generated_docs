
j.core.osis
===========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/grid/osis/OSISFactory.py>`_





decrypt
-------


* params: val,json
* path:/grid/osis/OSISFactory.py (line:89)


encrypt
-------


* params: obj
* path:/grid/osis/OSISFactory.py (line:76)


generateOsisModelDefaults
-------------------------


* params: namespace,specpath
* path:/grid/osis/OSISFactory.py (line:280)


getClient
---------


* params: ipaddr,port,user,passwd,ssl,gevent
* path:/grid/osis/OSISFactory.py (line:127)


getClientByInstance
-------------------


* params: instance,ssl,gevent,die
* path:/grid/osis/OSISFactory.py (line:172)


getClientForCategory
--------------------


* params: client,namespace,category
* path:/grid/osis/OSISFactory.py (line:195)


how to use

client=j.core.osis.getClientByInstance('main')
client4node=j.core.osis.getClientForCategory(client,"system","node")


getClientForNamespace
---------------------


* params: namespace,client
* path:/grid/osis/OSISFactory.py (line:190)


getLocal
--------


* params: path,overwriteHRD,overwriteImplementation,namespacename
* path:/grid/osis/OSISFactory.py (line:98)


create local instance starting from path


getModelTemplate
----------------


* params:
* path:/grid/osis/OSISFactory.py (line:292)


getOSISBaseObjectComplexType
----------------------------


* params:
* path:/grid/osis/OSISFactory.py (line:209)


getOsisBaseObjectClass
----------------------


* params:
* path:/grid/osis/OSISFactory.py (line:206)


getOsisImplementationParentClass
--------------------------------


* params: namespacename
* path:/grid/osis/OSISFactory.py (line:212)


return parent class for osis implementation (is the implementation from which each namespace & category inherits)


getOsisModelClass
-----------------


* params: namespace,category,specpath
* path:/grid/osis/OSISFactory.py (line:297)


returns class generated from spec file or from model.py file


startDaemon
-----------


* params: path,overwriteHRD,overwriteImplementation,key,port,superadminpasswd,dbconnections,hrd
* path:/grid/osis/OSISFactory.py (line:106)


start deamon


