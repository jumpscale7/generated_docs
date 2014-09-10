
j.packages
==========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/jpackages/JPackageClient.py>`_


checkJpackagesExistsOnRemoteBlobStor
------------------------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:1186)


checkProtectedDirs
------------------


* params: redo,checkInteractive
* path:/baselib/jpackages/JPackageClient.py (line:107)


recreate the config file for protected dirs (means directories linked to code repo's)
by executing this command you are sure that no development data will be overwritten


create
------


* params: domain,name,version,description,supportedPlatforms
* path:/baselib/jpackages/JPackageClient.py (line:163)


Creates a new jpackages4, this includes all standard tasklets, a config file and a description.wiki file


disableDebugMetaData
--------------------


* params: qualitylevel,domain
* path:/baselib/jpackages/JPackageClient.py (line:789)


enableConsoleLogging
--------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:90)


exists
------


* params: domain,name,version
* path:/baselib/jpackages/JPackageClient.py (line:306)


Checks whether the jpackages's metadata path is currently present on your system


find
----


* params: domain,name,version,platform,onlyone,installed,instance,expandInstances,interactive
* path:/baselib/jpackages/JPackageClient.py (line:530)



findByName
----------


* params: name
* path:/baselib/jpackages/JPackageClient.py (line:519)


name is part of jpackage, if none found return None, if more than 1 found raise error, name is part of name


findNewest
----------


* params: domain,name,minversion,maxversion,platform,returnNoneIfNotFound
* path:/baselib/jpackages/JPackageClient.py (line:467)


Find the newest jpackages which matches the criteria
If more than 1 jpackages matches -> error
If no jpackages match and not returnNoneIfNotFound -> error


get
---


* params: domain,name,version,instance
* path:/baselib/jpackages/JPackageClient.py (line:286)


Returns a jpackages


getActionNamesClass
-------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:273)


these actions can be applied on jpackage without knowing the jpackage instance


getActionNamesInstance
----------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:280)


getDataPath
-----------


* params: domain,name,version
* path:/baselib/jpackages/JPackageClient.py (line:434)


Returns the filesdatapath for the provided jpackages


getDebugPackages
----------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:320)


Returns a list of all currently installed packages on your system


getDomainNames
--------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:359)


Returns a list of all domains present in the sources.cfg file


getDomainObject
---------------


* params: domain,qualityLevel
* path:/baselib/jpackages/JPackageClient.py (line:345)


Get provided domain as an object


getInstalledPackages
--------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:313)


Returns a list of all currently installed packages on your system


getJPActionsPath
----------------


* params: domain,name,instance,fromtmp
* path:/baselib/jpackages/JPackageClient.py (line:374)


Returns the metadatapath for the provided jpackages
if fromtmp is True, then tmp directorypath will be returned



getJPActiveHRDPath
------------------


* params: domain,name,instance,fromtmp
* path:/baselib/jpackages/JPackageClient.py (line:407)


Returns the metadatapath for the provided jpackages
if fromtmp is True, then tmp directorypath will be returned



getJPActiveInstancePath
-----------------------


* params: domain,name,instance,fromtmp
* path:/baselib/jpackages/JPackageClient.py (line:390)


Returns the metadatapath for the provided jpackages in active mode



getJPackageMetadataScanner
--------------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:95)


returns tool which can be  used to scan the jpackages repo's and manipulate them


getJPackageObjects
------------------


* params: platform,domain
* path:/baselib/jpackages/JPackageClient.py (line:686)


Returns a list of jpackages objects for specified platform & domain


getMetaTarPath
--------------


* params: domainName
* path:/baselib/jpackages/JPackageClient.py (line:443)


Returns the metatarsdatapath for the provided domain


getMetadataPath
---------------


* params: domain,name,version
* path:/baselib/jpackages/JPackageClient.py (line:423)


Returns the metadatapath for the provided jpackages for active state



getPackagesWithBrokenDependencies
---------------------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:700)


getPendingReconfigurationPackages
---------------------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:334)


Returns a List of all jpackages that are pending for configuration


getTypePath
-----------


* params: ttype,relativepath,jp
* path:/baselib/jpackages/JPackageClient.py (line:214)


linkMetaData
------------


* params: domain
* path:/baselib/jpackages/JPackageClient.py (line:750)


Does an link of the meta information repo for each domain


log
---


* params: msg,category,level
* path:/baselib/jpackages/JPackageClient.py (line:81)


makeDependencyGraph
-------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:1084)


Creates a graphical visualization of all dependencies between the JPackackages of all domains.
This helps to quickly view and debug the dependencies and avoid errors.
The target audience are the developers of accross groups and domains that depend on each others packages.

The graph can be found here:
/opt/qbase5/var/jpackages/metadata/dependencyGraph.png

Notes:
The graph omits the constraints, such as version numbers and platform.

For completeness, a second graph is created that shows packages without andy dependencies (both ways).
See: dependencyGraph_singleNodes.png


mergeMetaData
-------------


* params: domain,commitMessage
* path:/baselib/jpackages/JPackageClient.py (line:821)


Does an update of the meta information repo for each domain


mergeMetaDataAll
----------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:731)


Tries to merge the metadata information of all jpackages with info on remote repo.
This used to be called updateJPackage list


metadataCreateQualityLevel
--------------------------


* params: domain,qualityLevelFrom,qualityLevelTo,force,link
* path:/baselib/jpackages/JPackageClient.py (line:874)


Create a quality level starting from the qualitylevelFrom e.g. unstable to beta


metadataDeleteQualityLevel
--------------------------


* params: domain,qualityLevel
* path:/baselib/jpackages/JPackageClient.py (line:856)


Delete a quality level


pm_getJPackageConfig
--------------------


* params: jpackagesMDPath
* path:/baselib/jpackages/JPackageClient.py (line:1081)


publish
-------


* params: commitMessage,domain
* path:/baselib/jpackages/JPackageClient.py (line:935)


Publishes all domains' bundles & metadata (if no domain specified)


publishAll
----------


* params: commitMessage
* path:/baselib/jpackages/JPackageClient.py (line:948)


Publish metadata & bundles for all domains, for more informartion see publishDomain


publishDomain
-------------


* params: domain,commitMessage
* path:/baselib/jpackages/JPackageClient.py (line:958)


Publish metadata & bundles for a domain.
To publish a domain means to make your local changes to the corresponding domain available to other users.
A domain can be changed in the following ways: a new package is created in it, a package in it is modified, a package in it is deleted.
To make the changes available to others the new metadata is uploaded to the mercurial servers and for the packages whos files
have been modified,
new bundles are created and uploaded to the blobstor server


publishMetaDataAsTarGz
----------------------


* params: domain,qualityLevel
* path:/baselib/jpackages/JPackageClient.py (line:913)


Compresses the meta data of a domain into a tar and upload that tar to the bundleUpload server.
After this the that uptain there metadata as a tar can download the latest metadata.


reloadconfig
------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:139)


Reload all jpackages config data from disk


reportError
-----------


* params: msg
* path:/baselib/jpackages/JPackageClient.py (line:78)


runConfigurationPending
-----------------------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:1003)


switchMetaData
--------------


* params: toQualitylevel,domain,disableDebug
* path:/baselib/jpackages/JPackageClient.py (line:765)


updateAll
---------


* params:
* path:/baselib/jpackages/JPackageClient.py (line:708)


Updates all installed jpackages to the latest builds.
The latest meta information is retrieved from the repository and based on this information,
The install packages that have a buildnr that has been outdated our reinstall, thust updating them to the latest build.


updateMetaData
--------------


* params: domain,force
* path:/baselib/jpackages/JPackageClient.py (line:806)


Does an update of the meta information repo for each domain


updateMetaDataAll
-----------------


* params: force
* path:/baselib/jpackages/JPackageClient.py (line:722)


Updates the metadata information of all jpackages
This used to be called updateJPackage list


updateMetaDataForDomain
-----------------------


* params: domainName
* path:/baselib/jpackages/JPackageClient.py (line:739)


Updates the meta information of specific domain
This used to be called updateJPackage list


uploadLocalJpackagesToBlobStor
------------------------------


* params: blobservername,history
* path:/baselib/jpackages/JPackageClient.py (line:1178)


