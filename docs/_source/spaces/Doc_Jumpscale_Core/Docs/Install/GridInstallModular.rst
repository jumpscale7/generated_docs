


How to install a grid in a modular way
**************************************


All of these sections assume you already have jumpscale + base installed


Mongodb
=======




.. code-block:: python

  jpackage install -n mongodb -i main -r --data="\
  mongodb.host=127.0.0.1 #\
  mongodb.port=27017 #\
  mongodb.replicaset= #\
  mongodb.name=main"




Influxdb
========


* OSIS populates influxdb for statistics of the grid.




.. code-block:: python

  jpackage install -n influxdb -i main -r --data="influxdb.seedservers:"



OSIS
====


* requires mongodb_client
* requires influxdb_client




.. code-block:: python

  #mongodb_client
  jpackage install -n mongodb_client -i main -r --data="\
  mongodb.client.addr=localhost #\
  mongodb.client.port=27017 #\
  mongodb.client.login= #\
  mongodb.client.passwd="
  
  #influxdb_client
  jpackage install -n influxdb_client -i main -r --data="\
  influxdb.client.addr=localhost #\
  influxdb.client.port=8086 #\
  influxdb.client.login=root #\
  influxdb.client.passwd=root"
  
  #osis
  jpackage install -n osis -i main -r --data="\
  osis.key= #\
  osis.connection=mongodb:main influxdb:main #\
  osis.superadmin.passwd=rooter"



AgentController
===============


* requires osis_client (osis does not need to run on same node)
* required webdisclient typicly webdis runs on AC
* all process managers connect to the agentcontroller




.. code-block:: python

  #osis_client
  jpackage install -n osis_client -i main -r --data="\
  osis.client.addr=localhost #\
  osis.client.port=5544 #\
  osis.client.login=root #\
  osis.client.passwd=rooter"
  
  #webdis
  jpackage install -n webdis -i main
  
  #webdis_client
  jpackage install -n webdis_client -i main --data="\
  addr=127.0.0.1 #\
  port=7779"
  
  #agentcontroller
  jpackage install -n agentcontroller -i main --data="\
  osis.connection=main #\
  webdis.connection=main"





GridPortal
----------


* runs on any node & talks to OSIS & the AgentController
* requires osis_client




.. code-block:: python

  #install portal
  jpackage install -n portal -i main -r --data="\
  portal.port=82 #\
  portal.ipaddr=localhost #\
  portal.admin.passwd=rooter #\
  portal.name=main #\
  osis.connection=main"
  
  #gridportal
  jpackage install -n grid_portal -i main -r --data="\
  portal.instance=main"




Jsagent
=======


* on each node
* monitors node and installs agent to execute jumpscripts on node

* requires agentcontroller_client, webdis_client, osis_client (osis client is only needed for monitoring)




.. code-block:: python

  #webdis_client
  jpackage install -n webdis_client -i main --data="\
  addr=127.0.0.1 #\
  port=7779"
  
  #osis_client
  jpackage install -n osis_client -i main -r --data="\
  osis.client.addr=localhost #\
  osis.client.port=5544 #\
  osis.client.login=root #\
  osis.client.passwd=rooter"
  
  #agentcontrolller client
  jpackage install -n agentcontroller_client -i main --data="\
  agentcontroller.client.addr=127.0.0.1 #\
  agentcontroller.client.login=node #\
  agentcontroller.client.port=4444"
  
  #Jsagent
  jpackage install -n jsagent -i main



