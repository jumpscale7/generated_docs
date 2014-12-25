This Explains how to manually install JumpScale on ubuntu & mint in development mode
====================================================================================

This is the non sandboxed install method. *This is only for developers
!!!!*

Tested on 13.10 & 14.04 64 bit. does also work on mint distro 64 bit.

update your apt repository & make sure some basic requirements are met

~~~~ {.sourceCode .python}
apt-get update
apt-get upgrade
apt-get install python-git git ssh python2.7 python-requests python-apt openssl ca-certificates python-pip ipython -y
apt-get install libpython-all-dev python-redis python-hiredis fabric -y
~~~~

if reinstall make sure you remove old version first (see below)

Install the latest trunk version from github
--------------------------------------------

~~~~ {.sourceCode .python}
pip install https://github.com/Jumpscale/jumpscale_core/archive/master.zip
~~~~

if you get a weird error please make sure that all js... files or links
in /usr/local/bin/ are gone

Get the jpackage metadata
-------------------------

Run the following command:

~~~~ {.sourceCode .python}
jpackage mdupdate
~~~~

This command may ask you for a valid github account credentials.

Install the core jpackages
--------------------------

~~~~ {.sourceCode .python}
jpackage install -n base -r
jpackage install -n core -r --debug
jpackage install -n libs -r --debug
~~~~

this will checkout the core repo and link into your environment, to make
development easy.

to make sure you remove previous version
----------------------------------------

~~~~ {.sourceCode .python}
pip uninstall JumpScale-core
~~~~

if you are not sure please do

~~~~ {.sourceCode .python}
pip uninstall JumpScale-core
killall tmux  #dangerous
killall redis-server
rm -rf /usr/local/lib/python2.7/dist-packages/jumpscale*
rm -rf /usr/local/lib/python2.7/site-packages/jumpscale*
rm -rf /usr/local/lib/python2.7/dist-packages/JumpScale*
rm -rf /usr/local/lib/python2.7/site-packages/JumpScale*
rm -rf /usr/local/lib/python2.7/site-packages/JumpScale/
rm -rf /usr/local/lib/python2.7/site-packages/jumpscale/
rm -rf /usr/local/lib/python2.7/dist-packages/JumpScale/
rm -rf /usr/local/lib/python2.7/dist-packages/jumpscale/
rm -rf /opt/jumpscale
rm /usr/local/bin/js*
rm /usr/local/bin/jpack*
killall python
rm -rf /opt/sentry/
sudo stop redisac
sudo stop redisp
sudo stop redism
sudo stop redisc
killall redis-server
rm -rf /opt/redis/
apt-get update
apt-get upgrade -y
~~~~

this will make sure all leftovers are gone
