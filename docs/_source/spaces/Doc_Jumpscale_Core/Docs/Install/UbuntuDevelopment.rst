

This Explains how to manually install JumpScale on ubuntu & mint in development mode
====================================================================================


This is the non sandboxed install method.
*This is only for developers !!!!*

Tested on 13.10 & 14.04 64 bit.
does also work on mint distro 64 bit.

update your apt repository & make sure some basic requirements are met



.. code-block:: python

  apt-get update
  apt-get upgrade
  apt-get install python-git git ssh python2.7 python-requests python-apt openssl ca-certificates python-pip ipython -y


if reinstall make sure you remove old version first (see below)


<<<<<<< HEAD
to make sure you remove previous version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
=======
Install the latest trunk version from github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>>>>>>> 4bd963abac470e406b5d663d4862d5f37b0cdf1d




.. code-block:: python

  pip install https://github.com/Jumpscale/jumpscale_core/archive/master.zip


if you get a weird error please make sure that all js... files or links in /usr/local/bin/ are gone


Get the jpackage metadata
^^^^^^^^^^^^^^^^^^^^^^^^^


Run the following command:



<<<<<<< HEAD
Install the latest trunk version from github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
=======
>>>>>>> 4bd963abac470e406b5d663d4862d5f37b0cdf1d

.. code-block:: python

  jpackage mdupdate


This command may ask you for a valid github account credentials.


Install the core jpackages
^^^^^^^^^^^^^^^^^^^^^^^^^^



<<<<<<< HEAD
Get the jpackage metadata
^^^^^^^^^^^^^^^^^^^^^^^^^
=======
>>>>>>> 4bd963abac470e406b5d663d4862d5f37b0cdf1d

.. code-block:: python

  jpackage install -n base -r
  jpackage install -n core -r --debug
  jpackage install -n libs -r --debug


this will checkout the core repo and link into your environment, to make development easy.





to make sure you remove previous version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


<<<<<<< HEAD
Install the core jpackages
^^^^^^^^^^^^^^^^^^^^^^^^^^
=======
>>>>>>> 4bd963abac470e406b5d663d4862d5f37b0cdf1d


.. code-block:: python

  pip uninstall JumpScale-core


if you are not sure please do

<<<<<<< HEAD
  template:shell
  jpackage install -n base -r
  jpacakge install -n core -r --debug
  jpacakge install -n libs -r --debug
  jpacakge install -n grid -r --debug
  jpacakge install -n portal -r --debug
=======
>>>>>>> 4bd963abac470e406b5d663d4862d5f37b0cdf1d


.. code-block:: python

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

this will make sure all leftovers are gone



