how to work with process manager
================================

how to install
--------------

~~~~ {.sourceCode .python}
jpackage install -n processmanager
~~~~

what does process manager do
----------------------------

-   check monitoring
-   run scheduled jobs
-   coordinate agents on local node
-   be API to local methods in process manager

some examples
-------------

check is running

~~~~ {.sourceCode .python}
jsprocess status
~~~~

to start:

~~~~ {.sourceCode .python}
jsprocess start -n processmanager
~~~~
