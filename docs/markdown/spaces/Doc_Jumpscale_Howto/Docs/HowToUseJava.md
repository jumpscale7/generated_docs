How To Us Java
==============

~~~~ {.sourceCode .python}
jpackage install -n java
~~~~

or put dependency to it

when using the process manager (process.configure) make sure you export
the java\_home e.g.

~~~~ {.sourceCode .python}
cmd="export JAVA_HOME=/opt/jumpscale/apps/openjdk7/;%s/elasticsearch"%workingdir
~~~~
