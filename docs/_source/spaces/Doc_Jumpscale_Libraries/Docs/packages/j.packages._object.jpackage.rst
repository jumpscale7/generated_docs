
j.packages._object.jpackage
===========================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/baselib/jpackages/JPackageObject.py>`_


Data representation of a JPackage, should contain all information contained in the jpackages.cfg


addDependency
-------------


* params: domain,name,supportedplatforms,minversion,maxversion,dependencytype
* path:/baselib/jpackages/JPackageObject.py (line:542)


backup
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


buildNrIncrement
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:677)


checkExistingBlobs
------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1747)



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
* path:/baselib/jpackages/JPackageObject.py (line:367)


getBlobHistory
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1766)


getBlobInfo
-----------


* params: platform,ttype,active
* path:/baselib/jpackages/JPackageObject.py (line:754)



getBlobItemPaths
----------------


* params: platform,ttype,blobitempath
* path:/baselib/jpackages/JPackageObject.py (line:775)


translates the item as shown in the blobinfo to the corresponding paths (jpackageFilesPath,destpathOnSystem)


getBlobKeysActive
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1681)


getBlobPlatformTypes
--------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


getBrokenDependencies
---------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:710)


Return a list of dependencies that cannot be resolved


getCodeLocationsFromRecipe
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:810)


getCodeMgmtRecipe
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:268)


getDebugMode
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:376)


getDebugModeInJpackage
----------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:379)


getDependencies
---------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:726)


Return the dependencies for the JPackage


getDependingInstalledPackages
-----------------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:572)


Return the packages that are dependent on this packages and installed on this machine
This is a heavy operation and might take some time


getDependingPackages
--------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:582)


Return the packages that are dependent on this package
This is a heavy operation and might take some time


getHighestInstalledBuildNr
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:670)


Return the latetst installed buildnumber


getInstanceNames
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:733)


getIsPreparedForUpdatingFiles
-----------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:560)


Return true if package has been prepared


getKey
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:569)


getMetadataPathQualityLevel
---------------------------


* params: ql
* path:/baselib/jpackages/JPackageObject.py (line:692)


getPathFiles
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:626)


Return absolute pathname of the jpackages's filespath


getPathFilesPlatform
--------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:633)


Return absolute pathname of the jpackages's filespath
if not given then will be: j.system.platformtype


getPathFilesPlatformForSubDir
-----------------------------


* params: subdir
* path:/baselib/jpackages/JPackageObject.py (line:645)


Return absolute pathnames of the jpackages's filespath for platform or parent of platform if it does not exist in lowest level
if platform not given then will be: j.system.platformtype
the subdir will be used to check upon if found in one of the dirs, if never found will raise error
all matching results are returned


getPathInstance
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:614)


Return absolute pathname of the package's metadatapath


getPathMetadata
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:620)


Return absolute pathname of the package's metadatapath active instance


getPathSourceCode
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:663)


Return absolute path to where this package's source can be extracted to


getQualityLevels
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:702)


getVersionAsInt
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:605)


Translate string version representation to a number


hasModifiedFiles
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:878)


Check if files are modified in the JPackage files


hasModifiedMetaData
-------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:887)


Check if files are modified in the JPackage metadata


install
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


installDebs
-----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1101)


isInstalled
-----------


* params: instance,checkAndDie,hrdcheck
* path:/baselib/jpackages/JPackageObject.py (line:894)


Check if the JPackage is installed


isNew
-----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1255)


isPendingReconfiguration
------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1926)


Check if the JPackage needs reconfiguration


isrunning
---------


* params: dependencies,ipaddr
* path:/baselib/jpackages/JPackageObject.py (line:1062)


Check if application installed is running for jpackages


kill
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


load
----


* params: instance,force,hrddata,findDefaultInstance
* path:/baselib/jpackages/JPackageObject.py (line:209)


loadBlobStores
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:355)


loadDependencies
----------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:496)


log
---


* params: msg,category,level
* path:/baselib/jpackages/JPackageObject.py (line:130)


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
* path:/baselib/jpackages/JPackageObject.py (line:1286)


After this command the operator can change the files of the jpackages.
Files do not aways come from code repo, they can also come from jpackages repo only


processDepCheck
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


reinstall
---------


* params: dependencies,download
* path:/baselib/jpackages/JPackageObject.py (line:1070)


Reinstall the JPackage by running its install tasklet, best not to use dependancies reinstall


removeDebugMode
---------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:417)


removeDebugModeInJpackage
-------------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:407)


reportNumbers
-------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:2013)


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
* path:/baselib/jpackages/JPackageObject.py (line:385)


setDebugModeInJpackage
----------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:398)


showDependencies
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1938)


Return all dependencies of the JPackage.
See also: addDependency and removeDependency


showDependingInstalledPackages
------------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1945)


Show which jpackages have this jpackages as dependency.
Do this only for the installed jpackages.


showDependingPackages
---------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1952)


Show which jpackages have this jpackages as dependency.


signalConfigurationNeeded
-------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1919)


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
* path:/baselib/jpackages/JPackageObject.py (line:920)


Check if a JPackage can be installed on a platform


uninstall
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


upload
------


* params: remote,local,dependencies,onlycode
* path:/baselib/jpackages/JPackageObject.py (line:1666)


uploadExistingBlobs
-------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1688)



uploadExistingBlobsFromHistory
------------------------------


* params: blobserver
* path:/baselib/jpackages/JPackageObject.py (line:1718)



waitDown
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


waitUp
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


