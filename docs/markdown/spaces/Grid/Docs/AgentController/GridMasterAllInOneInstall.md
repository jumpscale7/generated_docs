~~~~ {.sourceCode .python}
jpackage install -n grid_master_singlenode -r --debug
~~~~

When you are asked about the portal, make sure that you select the same
value entered during [portal
installation](/doc_jumpscale_core/UbuntuDevelopment) This will install
all required packages on 1 node

-   gridportal
-   osis
-   influxdb & mongodb (databases behind osis)
-   the agent controller
-   the jsagent (connecting to the agentcontroller)

