Loading and working with actors remotely
========================================

In order to be able to connect to a remote appserver, you'll have to
provide the following to the getPortalClient call:

1.  ip: the IP of the remote appserver
2.  port: the port on which Nginx is listening
3.  secret: appserver secret token

~~~~ {.sourceCode .python}
import JumpScale.portal
cl = j.core.portal.getPortalClient(ip='<REMOTE-APPSERVER-IP>', port=80, secret="1234")
ma = cl.getActor("system", "master")
ma.ping()
~~~~
