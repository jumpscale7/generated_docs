
Distributed Work Controller
***************************

Introduction.
=============


JumpScale provides the capability to execute tasks on x number of nodes.

Those tasks can be executed in different ways

* async, task is executed in a `worker <workers>`_
* sync, task is executed in the `processmanager <processmanager>`_
* on interval, task is executed either in the `processmanager <processmanager>`_ or `worker <workers>`_ on the specified interval


Architecture
============


Components
==========


* `Agentcontroller <Agentcontroller>`_
* `ProcessManager <ProcessManager>`_
* `Worker <Worker>`_


How To
======


* `Schedule work using agentcontroller <ScheduleWork>`_
