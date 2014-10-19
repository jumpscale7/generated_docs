
j.packages._object.jpackage
===========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/jpackages/JPackageObject.py>`_


Data representation of a JPackage, should contain all information contained in the jpackages.cfg


addDependency
-------------


* params: domain,name,supportedplatforms,minversion,maxversion,dependencytype
* path:/baselib/jpackages/JPackageObject.py (line:534)


backup
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


buildNrIncrement
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:669)


checkExistingBlobs
------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1739)



codeCommit
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeExport
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeLink
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeUpdate
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


compile
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


configure
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


copyfiles
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


delete
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


download
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


getAppPath
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:359)


getBlobHistory
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1758)


getBlobInfo
-----------


* params: platform,ttype,active
* path:/baselib/jpackages/JPackageObject.py (line:746)



getBlobItemPaths
----------------


* params: platform,ttype,blobitempath
* path:/baselib/jpackages/JPackageObject.py (line:767)


translates the item as shown in the blobinfo to the corresponding paths (jpackageFilesPath,destpathOnSystem)


getBlobKeysActive
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1673)


getBlobPlatformTypes
--------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


getBrokenDependencies
---------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:702)


Return a list of dependencies that cannot be resolved


getCodeLocationsFromRecipe
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:802)


getCodeMgmtRecipe
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:260)


getDebugMode
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:368)


getDebugModeInJpackage
----------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:371)


getDependencies
---------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:718)


Return the dependencies for the JPackage


getDependingInstalledPackages
-----------------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:564)


Return the packages that are dependent on this packages and installed on this machine
This is a heavy operation and might take some time


getDependingPackages
--------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:574)


Return the packages that are dependent on this package
This is a heavy operation and might take some time


getHighestInstalledBuildNr
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:662)


Return the latetst installed buildnumber


getInstanceNames
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:725)


getIsPreparedForUpdatingFiles
-----------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:552)


Return true if package has been prepared


getKey
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:561)


getMetadataPathQualityLevel
---------------------------


* params: ql
* path:/baselib/jpackages/JPackageObject.py (line:684)


getPathFiles
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:618)


Return absolute pathname of the jpackages's filespath


getPathFilesPlatform
--------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:625)


Return absolute pathname of the jpackages's filespath
if not given then will be: j.system.platformtype


getPathFilesPlatformForSubDir
-----------------------------


* params: subdir
* path:/baselib/jpackages/JPackageObject.py (line:637)


Return absolute pathnames of the jpackages's filespath for platform or parent of platform if it does not exist in lowest level
if platform not given then will be: j.system.platformtype
the subdir will be used to check upon if found in one of the dirs, if never found will raise error
all matching results are returned


getPathInstance
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:606)


Return absolute pathname of the package's metadatapath


getPathMetadata
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:612)


Return absolute pathname of the package's metadatapath active instance


getPathSourceCode
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:655)


Return absolute path to where this package's source can be extracted to


getQualityLevels
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:694)


getVersionAsInt
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:597)


Translate string version representation to a number


hasModifiedFiles
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:870)


Check if files are modified in the JPackage files


hasModifiedMetaData
-------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:879)


Check if files are modified in the JPackage metadata


install
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


installDebs
-----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1093)


isInstalled
-----------


* params: instance,checkAndDie,hrdcheck
* path:/baselib/jpackages/JPackageObject.py (line:886)


Check if the JPackage is installed


isNew
-----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1247)


isPendingReconfiguration
------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1918)


Check if the JPackage needs reconfiguration


isrunning
---------


* params: dependencies,ipaddr
* path:/baselib/jpackages/JPackageObject.py (line:1054)


Check if application installed is running for jpackages


kill
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


load
----


* params: instance,force,hrddata,findDefaultInstance
* path:/baselib/jpackages/JPackageObject.py (line:201)


loadBlobStores
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:347)


loadDependencies
----------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:488)


log
---


* params: msg,category,level
* path:/baselib/jpackages/JPackageObject.py (line:122)


monitor
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


monitor_net
-----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


package
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


prepare
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


prepareForUpdatingFiles
-----------------------


* params: suppressErrors
* path:/baselib/jpackages/JPackageObject.py (line:1278)


After this command the operator can change the files of the jpackages.
Files do not aways come from code repo, they can also come from jpackages repo only


processDepCheck
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


reinstall
---------


* params: dependencies,download
* path:/baselib/jpackages/JPackageObject.py (line:1062)


Reinstall the JPackage by running its install tasklet, best not to use dependancies reinstall


removeDebugMode
---------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:409)


removeDebugModeInJpackage
-------------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:399)


reportNumbers
-------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:2005)


restart
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


restore
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


save
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


setDebugMode
------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:377)


setDebugModeInJpackage
----------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:390)


showDependencies
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1930)


Return all dependencies of the JPackage.
See also: addDependency and removeDependency


showDependingInstalledPackages
------------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1937)


Show which jpackages have this jpackages as dependency.
Do this only for the installed jpackages.


showDependingPackages
---------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1944)


Show which jpackages have this jpackages as dependency.


signalConfigurationNeeded
-------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1911)


Set in the corresponding jpackages's state file if reconfiguration is needed


start
-----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


stop
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


supportsPlatform
----------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:912)


Check if a JPackage can be installed on a platform


uninstall
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


upload
------


* params: remote,local,dependencies,onlycode
* path:/baselib/jpackages/JPackageObject.py (line:1658)


uploadExistingBlobs
-------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1680)



uploadExistingBlobsFromHistory
------------------------------


* params: blobserver
* path:/baselib/jpackages/JPackageObject.py (line:1710)



waitDown
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


waitUp
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


