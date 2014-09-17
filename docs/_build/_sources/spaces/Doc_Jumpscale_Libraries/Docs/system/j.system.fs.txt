
j.system.fs
===========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/system/fs.py>`_


changeDir
---------


* params: path
* path:/core/system/fs.py (line:445)


Changes Current Directory


changeFileNames
---------------


* params: toReplace,replaceWith,pathToSearchIn,recursive,filter,minmtime,maxmtime
* path:/core/system/fs.py (line:956)



checkDirOrLink
--------------


* params: fullpath
* path:/core/system/fs.py (line:937)


check if path is dir or link to a dir


checkDirOrLinkToDir
-------------------


* params: fullpath
* path:/core/system/fs.py (line:944)


check if path is dir or link to a dir


checkDirParam
-------------


* params: path
* path:/core/system/fs.py (line:1102)


chmod
-----


* params: path,permissions
* path:/core/system/fs.py (line:692)



chown
-----


* params: path,user
* path:/core/system/fs.py (line:670)


cleanupString
-------------


* params: string,replacewith,regex
* path:/core/system/fs.py (line:53)


Remove all non-numeric or alphanumeric characters


constructDirPathFromArray
-------------------------


* params: array
* path:/core/system/fs.py (line:1793)


constructFilePathFromArray
--------------------------


* params: array
* path:/core/system/fs.py (line:1803)


convertFileDirnamesSpaceToUnderscore
------------------------------------


* params: rootdir
* path:/core/system/fs.py (line:1562)


convertFileDirnamesUnicodeToAscii
---------------------------------


* params: rootdir,spacesToUnderscore
* path:/core/system/fs.py (line:1535)


copyDirTree
-----------


* params: src,dst,keepsymlinks,eraseDestination,skipProtectedDirs,overwriteFiles,applyHrdOnDestPaths
* path:/core/system/fs.py (line:353)


Recursively copy an entire directory tree rooted at src.
The dst directory may already exist; if not,
it will be created as well as missing parent directories


copyFile
--------


* params: fileFrom,to,createDirIfNeeded,skipProtectedDirs,overwriteFile
* path:/core/system/fs.py (line:223)


Copy file

Copies the file from C{fileFrom} to the file or directory C{to}.
If C{to} is a directory, a file with the same basename as C{fileFrom} is
created (or overwritten) in the directory specified.
Permission bits are copied.



createDir
---------


* params: newdir,skipProtectedDirs
* path:/core/system/fs.py (line:318)


Create new Directory
if newdir was only given as a directory name, the new directory will be created on the default path,
if newdir was given as a complete path with the directory name, the new directory will be created in the specified path


createEmptyFile
---------------


* params: filename
* path:/core/system/fs.py (line:305)


Create an empty file


dirEqual
--------


* params: path1,path2
* path:/core/system/fs.py (line:580)


exists
------


* params: path,followlinks
* path:/core/system/fs.py (line:1031)


Check if the specified path exists


fileConvertLineEndingCRLF
-------------------------


* params: file
* path:/core/system/fs.py (line:1747)


Convert CRLF line-endings in a file to LF-only endings (
->
)




fileGetContents
---------------


* params: filename
* path:/core/system/fs.py (line:1265)


Read a file and get contents of that file


fileGetTextContents
-------------------


* params: filename
* path:/core/system/fs.py (line:1298)


Read a UTF-8 file and get contents of that file. Takes care of the BOM <BOM>(http://en.wikipedia.org/wiki/Byte_order_mark)


fileGetUncommentedContents
--------------------------


* params: filename
* path:/core/system/fs.py (line:1279)


Read a file and get uncommented contents of that file


fileSize
--------


* params: filename
* path:/core/system/fs.py (line:1349)


Get Filesize of file in bytes


find
----


* params: startDir,fileregex
* path:/core/system/fs.py (line:1763)


Search for files or folders matching a given pattern
this is a very weard function, don't use is better to use the list functions
make sure you do changedir to the starting dir first
example: find("*.pyc")


getBaseName
-----------


* params: path
* path:/core/system/fs.py (line:533)


Return the base name of pathname path.


getDirName
----------


* params: path,lastOnly,levelsUp
* path:/core/system/fs.py (line:504)


Return a directory name from pathname path.
e.g. ...getDirName("/opt/qbase/bin/something/test.py", levelsUp=0) would return something
e.g. ...getDirName("/opt/qbase/bin/something/test.py", levelsUp=1) would return bin
e.g. ...getDirName("/opt/qbase/bin/something/test.py", levelsUp=10) would raise an error


getFileExtension
----------------


* params: path
* path:/core/system/fs.py (line:662)


getParent
---------


* params: path
* path:/core/system/fs.py (line:647)


Returns the parent of the path:
/dir1/dir2/file_or_dir -> /dir1/dir2/
/dir1/dir2/            -> /dir1/


getParentDirName
----------------


* params: path
* path:/core/system/fs.py (line:614)


returns parent of path (only for dirs)
returns empty string when there is no parent


getTempFileName
---------------


* params: dir,prefix
* path:/core/system/fs.py (line:1599)


Generates a temp file for the directory specified


getTmpDirPath
-------------


* params:
* path:/core/system/fs.py (line:1572)


create a tmp dir name and makes sure the dir exists


getTmpFilePath
--------------


* params: cygwin
* path:/core/system/fs.py (line:1581)


Generate a temp file path
Located in temp dir of qbase


getcwd
------


* params:
* path:/core/system/fs.py (line:771)


get current working directory


grep
----


* params: fileregex,lineregex
* path:/core/system/fs.py (line:1775)


Search for lines matching a given regex in all files matching a regex



gunzip
------


* params: sourceFile,destFile
* path:/core/system/fs.py (line:1887)


gzip
----


* params: sourceFile,destFile
* path:/core/system/fs.py (line:1879)


hardlinkFile
------------


* params: source,destin
* path:/core/system/fs.py (line:1084)


Create a hard link pointing to source named destin. Availability: Unix.
with exactly one directory separator (os.sep) inserted between components, unless path2 is empty


isAsciiFile
-----------


* params: filename,checksize
* path:/core/system/fs.py (line:1611)


Read the first <checksize> bytes of <filename>.
Validate that only valid ascii characters (32-126), ,       ,
are
present in the file


isBinaryFile
------------


* params: filename,checksize
* path:/core/system/fs.py (line:1635)


isDir
-----


* params: path,followSoftlink
* path:/core/system/fs.py (line:1114)


Check if the specified Directory path exists


isEmptyDir
----------


* params: path
* path:/core/system/fs.py (line:1128)


Check if the specified directory path is empty


isFile
------


* params: path,followSoftlink
* path:/core/system/fs.py (line:1144)


Check if the specified file exists for the given path


isLink
------


* params: path,checkJunction
* path:/core/system/fs.py (line:1169)


Check if the specified path is a link


isMount
-------


* params: path
* path:/core/system/fs.py (line:1198)


Return true if pathname path is a mount point:
A point in a file system where a different file system has been mounted.


islocked
--------


* params: lockname,reentry
* path:/core/system/fs.py (line:109)


Check if a system-wide interprocess exclusive lock is set


joinPaths
---------


* params:
* path:/core/system/fs.py (line:477)


Join one or more path components.
If any component is an absolute path, all previous components are thrown away, and joining continues.
with exactly one directory separator (os.sep) inserted between components, unless path2 is empty.


listDirsInDir
-------------


* params: path,recursive,dirNameOnly,findDirectorySymlinks
* path:/core/system/fs.py (line:980)


Retrieves list of directories found in the specified directory


listFilesAndDirsInDir
---------------------


* params: path,recursive,filter,minmtime,maxmtime,depth,type
* path:/core/system/fs.py (line:850)


Retrieves list of files found in the specified directory


listFilesInDir
--------------


* params: path,recursive,filter,minmtime,maxmtime,depth,case_sensitivity,exclude,followSymlinks
* path:/core/system/fs.py (line:824)


Retrieves list of files found in the specified directory


listPyScriptsInDir
------------------


* params: path,recursive,filter
* path:/core/system/fs.py (line:1009)


Retrieves list of python scripts (with extension .py) in the specified directory


lock
----


* params: lockname,locktimeout,reentry
* path:/core/system/fs.py (line:61)


Take a system-wide interprocess exclusive lock. Default timeout is 60 seconds


lock_
-----


* params: lockname,locktimeout,reentry
* path:/core/system/fs.py (line:74)


Take a system-wide interprocess exclusive lock.

Works similar to j.system.fs.lock but uses return values to denote lock
success instead of raising fatal errors.

This refactoring was mainly done to make the lock implementation easier
to unit-test.


log
---


* params: msg,level,category
* path:/core/system/fs.py (line:218)


md5sum
------


* params: filename
* path:/core/system/fs.py (line:1397)


Return the hex digest of a file without loading it all into memory


move
----


* params: source,destin
* path:/core/system/fs.py (line:1022)


Main Move function
(If the specified source is a Directory....Calls moveDir function)


moveDir
-------


* params: source,destin
* path:/core/system/fs.py (line:463)


Move Directory from source to destination


moveFile
--------


* params: source,destin
* path:/core/system/fs.py (line:259)


Move a  File from source path to destination path


parsePath
---------


* params: path,baseDir,existCheck,checkIsFile
* path:/core/system/fs.py (line:715)


parse paths of form /root/tmp/33_adoc.doc into the path, priority which is numbers before _ at beginning of path
also returns filename
checks if path can be found, if not will fail
when filename="" then is directory which has been parsed
if basedir specified that part of path will be removed

example:
j.system.fs.parsePath("/opt/qbase3/apps/specs/myspecs/definitions/cloud/datacenter.txt","/opt/qbase3/apps/specs/myspecs/",existCheck=False)
priority = 0 if not specified


pathClean
---------


* params: path
* path:/core/system/fs.py (line:564)


goal is to get a equal representation in / & in relation to os.sep


pathDirClean
------------


* params: path
* path:/core/system/fs.py (line:576)


pathNormalize
-------------


* params: path,root
* path:/core/system/fs.py (line:583)


paths are made absolute & made sure they are in line with os.sep


pathRemoveDirPart
-----------------


* params: path,toremove,removeTrailingSlash
* path:/core/system/fs.py (line:596)


goal remove dirparts of a dirpath e,g, a basepath which is not needed
will look for part to remove in full path but only full dirs


pathShorten
-----------


* params: path
* path:/core/system/fs.py (line:543)


Clean path (change /var/www/../lib to /var/lib). On Windows, if the
path exists, the short path name is returned.



pathToUnicode
-------------


* params: path
* path:/core/system/fs.py (line:1809)


Convert path to unicode. Use the local filesystem encoding. Will return
path unmodified if path already is unicode.

Use this to convert paths you received from the os module to unicode.



processPathForDoubleDots
------------------------


* params: path
* path:/core/system/fs.py (line:625)


/root/somepath/.. would become /root
/root/../somepath/ would become /somepath

result will always be with / slashes


readObjectFromFile
------------------


* params: filelocation
* path:/core/system/fs.py (line:1380)


Read a object from a file(file contents in pickle format)


readlink
--------


* params: path
* path:/core/system/fs.py (line:781)


Works only for unix
Return a string representing the path to which the symbolic link points.


remove
------


* params: path
* path:/core/system/fs.py (line:287)


Remove a File


removeDir
---------


* params: path
* path:/core/system/fs.py (line:429)


Remove a Directory


removeDirTree
-------------


* params: path,onlyLogWarningOnRemoveError
* path:/core/system/fs.py (line:403)


Recursively delete a directory tree.


removeIrrelevantFiles
---------------------


* params: path,followSymlinks
* path:/core/system/fs.py (line:281)


removeLinks
-----------


* params: path
* path:/core/system/fs.py (line:798)


find all links & remove


renameDir
---------


* params: dirname,newname,overwrite
* path:/core/system/fs.py (line:1218)


Rename Directory from dirname to newname


renameFile
----------


* params: filePath,new_name
* path:/core/system/fs.py (line:274)


OBSOLETE


replaceWordsInFiles
-------------------


* params: pathToSearchIn,templateengine,recursive,filter,minmtime,maxmtime
* path:/core/system/fs.py (line:967)


apply templateengine to list of found files
te=j.codetools.templateengine.new()
te.add("name",self.jpackages.name)
te.add("description",self.jpackages.description)
te.add("version",self.jpackages.version)


statPath
--------


* params: path
* path:/core/system/fs.py (line:1207)


Perform a stat() system call on the given path


symlink
-------


* params: path,target,overwriteTarget
* path:/core/system/fs.py (line:1050)


Create a symbolic link


targzCompress
-------------


* params: sourcepath,destinationpath,followlinks,destInTar,pathRegexIncludes,pathRegexExcludes,contentRegexIncludes,contentRegexExcludes,depths,extrafiles
* path:/core/system/fs.py (line:1824)


tar.gz with this param can put something in front e.g. /qbase3/ prefix to dest in tgz
(TAR-GZ-Archive *.tar.gz)


targzUncompress
---------------


* params: sourceFile,destinationdir,removeDestinationdir
* path:/core/system/fs.py (line:1896)


compress dirname recursive


touch
-----


* params: paths,overwrite
* path:/core/system/fs.py (line:1314)


can be single path or multiple (then list)


unlink
------


* params: filename
* path:/core/system/fs.py (line:1250)


Remove the given file if it's a file or a symlink



unlinkFile
----------


* params: filename
* path:/core/system/fs.py (line:1235)


Remove the file path (only for files, not for symlinks)


unlock
------


* params: lockname
* path:/core/system/fs.py (line:139)


Unlock system-wide interprocess lock


unlock_
-------


* params: lockname
* path:/core/system/fs.py (line:147)


Unlock system-wide interprocess lock

Works similar to j.system.fs.unlock but uses return values to denote unlock
success instead of raising fatal errors.

This refactoring was mainly done to make the lock implementation easier
to unit-test.


validateFilename
----------------


* params: filename,platform
* path:/core/system/fs.py (line:1644)


Validate a filename for a given (or current) platform

Check whether a given filename is valid on a given platform, or the
current platform if no platform is specified.

Rules
=====
Generic
-------
Zero-length filenames are not allowed

Unix
----
Filenames can contain any character except 0x00. We also disallow a
forward slash ('/') in filenames.

Filenames can be up to 255 characters long.

Windows
-------
Filenames should not contain any character in the 0x00-0x1F range, '<',
'>', ':', '"', '/', '', '|', '?' or '*'. Names should not end with a
dot ('.') or a space (' ').

Several basenames are not allowed, including CON, PRN, AUX, CLOCK$,
NUL, COM1-9 <1-9> and LPT1-9 <1-9>.

Filenames can be up to 255 characters long.

Information sources
===================
Restrictions are based on information found at these URLs:


* http://en.wikipedia.org/wiki/Filename
* http://msdn.microsoft.com/en-us/library/aa365247.aspx
* http://www.boost.org/doc/libs/1_35_0/libs/filesystem/doc/portability_guide.htm
* http://blogs.msdn.com/brian_dewey/archive/2004/01/19/60263.aspx




walk
----


* params: root,recurse,pattern,return_folders,return_files,followSoftlinks,unicode
* path:/core/system/fs.py (line:1493)


This is to provide ScanDir similar function
It is going to be used wherever some one wants to list all files and subfolders
under one given directly with specific or none matchers


walkExtended
------------


* params: root,recurse,dirPattern,filePattern,followSoftLinks,dirs,files
* path:/core/system/fs.py (line:1420)


Extended Walk version: seperate dir and file pattern


General guidelines in the usage of the method be means of some examples come next. For the example in /tmp there is


* a file test.rtt
* and ./folder1/subfolder/subsubfolder/small_test/test.rtt


To find the first test you can use
j.system.fs.walkExtended('/tmp/', dirPattern="*tmp*", filePattern="*.rtt")
To find only the second one you could use
j.system.fs.walkExtended('tmp', recurse=0, dirPattern="*small_test*", filePattern="*.rtt", dirs=False)


writeFile
---------


* params: filename,contents,append
* path:/core/system/fs.py (line:1329)


Open a file and write file contents, close file afterwards


writeObjectToFile
-----------------


* params: filelocation,obj
* path:/core/system/fs.py (line:1363)


Write a object to a file(pickle format)


