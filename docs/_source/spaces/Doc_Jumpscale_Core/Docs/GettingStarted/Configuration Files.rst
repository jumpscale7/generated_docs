

Configuration Files
===================

These are some configuration files that might be of use:
--------------------------------------------------------

$jumpscaledir/cfg/jpackages/sources.cfg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This file is where the domains of the jpackages are defined. eg:



.. code-block:: python

  [jumpscale]                                                 
  metadatafromtgz = 0
  qualitylevel = unstable
  metadatadownload = 
  metadataupload = 
  bitbucketaccount = jumpscale
  bitbucketreponame = jp_jumpscale
  blobstorremote = jpackages_remote
  blobstorlocal = jpackages_local




$jumpscaledir/cfg/jsconfig/bitbucket.cfg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This file is where the credentials for each domain are defined. eg:



.. code-block:: python

  [jumpscale]
  login = <login>
  passwd = <password>




$jumpscaledir/cfg/jsconfig/blobstor.cfg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This file is where the configuration of the remote and local blobservers is defined. eg:



.. code-block:: python

  [jpackages_local]                                                                                                                                                
  ftp = 
  type = local
  http = 
  localpath = /opt/jpackagesftp
  namespace = jpackages
  
  [jpackages_remote]
  ftp = ftp://<login>:<password>@jpackages.vscalers.com
  type = httpftp
  http = http://jpackages.vscalers.com
  localpath = 
  namespace = jpackages




$jumpscaledir/apps/<portalapp>/cfg/portal.cfg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is where all the configurations related to a portal would be defined. eg:



.. code-block:: python

  [main]                                                                                                                                                           
  appdir = $jumpscaledir/apps/portalbase
  
  filesroot = /opt/jumpscale/var/portal/files
  
  #fs,mem,redis,arakoon is db which is attached to process of webserver
  dbtype = redis
  
  actors = *
  webserverport = 81
  pubipaddr=0.0.0.0
  
  #leave 0 if disabled (this is like secret which gives access to all)
  secret=
  
  ##authenticate params
  #redis, config or empty if e.g. only the secret
  #config is users.cfg 
  authentication = redis
  
  #groups which get access to admin features of portal
  admingroups=admin,gridadmin,superadmin

