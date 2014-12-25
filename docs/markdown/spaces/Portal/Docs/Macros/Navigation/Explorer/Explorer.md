Explorer
========

Params
------

### path

-   Path to explore

#### Example

~~~~ {.sourceCode .python}
\{\{explorer: ppath:c:/data \}\}
~~~~

### height

-   Hight in pixels of control

#### Example

~~~~ {.sourceCode .python}
\{\{explorer: hight:400 \}\}
~~~~

### readonly

-   If files cannot be modified/uploaded
-   Remark: admin will always have right to modify & upload

#### Example

~~~~ {.sourceCode .python}
\{\{explorer: readonly \}\}
~~~~

### bucket

-   Name of bucket to show in explorer
-   Do not use bucket & path at same time

#### Example

~~~~ {.sourceCode .python}
\{\{explorer: bucket:mydocs \}\}
~~~~

Example
-------

~~~~ {.sourceCode .python}
\{\{explorer: ppath:system/system__contentmanager/ readonly height:400\}\}
~~~~
