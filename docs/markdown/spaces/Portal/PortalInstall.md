Installing the Portal
=====================

The JumpScale portal requires the JumpScale framework to be installed.
So if you didn't do so [install JumpScale](UbuntuManual).

~~~~ {.sourceCode .python}
jpackage install -n base -r

#install mail client
jpackage install -n mailclient -r --data="\
mail.relay.addr=smtp.mandrillapp.com #\
mail.relay.port=587 #\
mail.relay.ssl=1 #\
mail.relay.username=support@mothersip1.com #\
mail.relay.passwd=RVPrWxhyFF7I1s0GGtxt9Q"

#install mongodb (if local install)
jpackage install -n mongodb -i main -r --data="\
mongodb.host=127.0.0.1 #\
mongodb.port=27017 #\
mongodb.replicaset= #\
mongodb.name=main"

#install mongodb client
jpackage install -n mongodb_client -i main -r --data="\
mongodb.client.addr=localhost #\
mongodb.client.port=27017 #\
mongodb.client.login= #\
mongodb.client.passwd="

#install osis (if local install)
jpackage install -n osis -i main -r --data="\
osis.key= #\
osis.connection=mongodb:main #\
osis.superadmin.passwd=rooter"

#install osis (if local install and no influxdb)
jpackage install -n osis -i main -r --data="\
osis.key= #\
osis.connection=mongodb:main#\
osis.superadmin.passwd=rooter"


#install osis client (if remote install, then no mongodb client nor server required)
jpackage install -n osis_client -i main -r --data="\
osis.client.addr=localhost #\
osis.client.port=5544 #\
osis.client.login=root #\
osis.client.passwd=rooter"

#create admin user for e.g. portal
jsuser set --hrd="\
user.name=admin #\
user.domain=incubaid.com #\
user.passwd=admin #\
user.roles=admin #\
user.active=1 #\
user.description= #\
user.emails=kristof@incubaid.com #\
user.xmpp= #\
user.mobile=+??? #\
user.authkeys=2354345345,436346346 #\
user.groups=admin"

#install portal (depends on osis)
jpackage install -n portal -i main -r --data="\
portal.port=82 #\
portal.ipaddr=localhost #\
portal.admin.passwd=js007 #\
portal.name=cloudrobot #\
osis.connection=main"


#install portal for jumpscale docs
jpackage install -n docs_jumpscale -i main -r --data="\
osis.connection=main"
~~~~

Start the portal by starting the necessary processes:

~~~~ {.sourceCode .python}
jsprocess start
~~~~
