install of agent controller
===========================

requirements
------------

-   make sure jumpscale is installed properly (see those documentation
    sections)
-   make sure osis & portal are installed (see those documentation
    sections)

install as all in 1 install
---------------------------

install modular
---------------

~~~~ {.sourceCode .python}
jpackage install -n webdis -i main

#install webdis_client
jpackage install -n webdis_client -i main --data="\
addr=127.0.0.1 #\
port=7779"

#redis for agentcontroller
jpackage install -n redis -i ac --data="\
redis.name=ac #\
redis.port=9999 #\
redis.mem=200 #\
redis.disk=1"

#agentcontroller
jpackage install -n agentcontroller -i main --data="\
osis.connection=main #\
webdis.connection=main"

#@todo complete
~~~~
