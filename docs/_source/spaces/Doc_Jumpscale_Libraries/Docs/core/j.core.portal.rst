
j.core.portal
=============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/portal/portal/PortalFactory.py>`_


getClient
---------


* params: ip,port,secret
* path:/portal/portal/PortalFactory.py (line:82)


return client to manipulate & access a running application server (out of process)
caching is done so can call this as many times as required
secret is normally configured from grid
there is normally no need to use this method, use self.getActorClient in stead


getClientByInstance
-------------------


* params: instance
* path:/portal/portal/PortalFactory.py (line:72)


getPortalConfig
---------------


* params: appname
* path:/portal/portal/PortalFactory.py (line:27)


getServer
---------


* params:
* path:/portal/portal/PortalFactory.py (line:24)


loadActorsInProcess
-------------------


* params: name
* path:/portal/portal/PortalFactory.py (line:31)


make sure all actors are loaded on j.apps...


