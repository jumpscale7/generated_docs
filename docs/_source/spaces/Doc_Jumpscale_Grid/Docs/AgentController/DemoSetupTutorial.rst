

Demo Setup For AgentController & Agents
***************************************


This tutorial will explain how to get started with a debug environment for the agentcontroller.
This can be used to experiment with Jumpscale & the Grid & Agentcontroller Framework.


requirements
============


* ubuntu 14.04 64 bit  (it possibly works on other ubuntu versions too but is not tested)
* install jumpscale in debug mode see @todo <@todo>


install an all in 1 grid master
===============================


* a grid master has everything required to manage a grid



to start the agent




.. code-block:: python

  cd /opt/jumpscale/apps/jsagent/
  python jsagent.py





test the worker functionality on the gridmaster node itself
===========================================================




.. code-block:: python

  cd /opt/jumpscale/apps/jsagent/
  python workertest.py





.. code-block:: python

  from JumpScale import j
  
  j.application.start("jumpscale:workertest")
  
  import JumpScale.baselib.redisworker
  
  def atest(msg):
      print msg
      # raise RuntimeError("e")
      return msg
  
  w=j.clients.redisworker
  
  def test1():
      print "START"
      for i in range(10):
          job=w.execFunction( method=atest, _category='mytest', _organization='unknown', _timeout=60, _queue='default', _log=True,_sync=True, msg="this is a test")
      print job
      print "STOP"
  
  print w.getQueuedJobs()
  
  test1()
  
  j.application.stop()


here you execute a function remotely in the worker of the jsagent.
This will be executed async and result returned.
This is handy to shedule & launch long running jobs.


work with multiple agents in debug mode
=======================================


* on a new ubuntu 14.04 server where jumpscale is installed in debug mode




.. code-block:: python

  jpackage install -n jsagent


this will have installed a jsagent & the jsagent registers to the agentcontroller.

to start the agent




.. code-block:: python

  cd /opt/jumpscale/apps/jsagent/
  python jsagent.py


you can ofcourse put this agent in init.d or so
(PS on the roadmap (Q4 2014) the agent will register itself optionally in init.d and work as daemon)


visit gridportal and see the different nodes (agents)
=====================================================


//localhost:82/grid/Nodes <http://localhost:82/grid/Nodes>



jumpscripts basics
==================


goals of this section

* explain how to create a jumpscript to call jumpscripts remotely
* explain the role of the roles of agents
* create a new jumpscript & reload the jumpscript on the jsagents
* see that this jumpscript can be called
* show output of jumpscript
* show where to see it in the gridportal
* show what happens when there is an error


so basically is a demonstration of the full end2end functionality of the agentcontroller/jsagent system



recurring jumpscripts
=====================


goals this section

* expain how to create recurring jumpscripts and how they get scheduled
* show how the jumpscripts can be seen on portal
* show that from the jumpscript page you can see when & where the jumpscripts where executed
* show that if error where result is seen and how to debug (use a error generating jumpscript)









