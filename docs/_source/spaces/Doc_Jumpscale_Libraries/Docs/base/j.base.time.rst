
j.base.time
===========

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/base/time/Time.py>`_


generic provider of time functions
lives at j.base.time


HRDatetoEpoch
-------------


* params: datestr,local
* path:/core/base/time/Time.py (line:164)


convert string date to epoch
Date needs to be formatted as 16/06/1988


epoch2HRDate
------------


* params: epoch,local
* path:/core/base/time/Time.py (line:86)


epoch2HRDateTime
----------------


* params: epoch,local
* path:/core/base/time/Time.py (line:89)


epoch2HRTime
------------


* params: epoch,local
* path:/core/base/time/Time.py (line:92)


fiveMinuteIdToEpoch
-------------------


* params: fiveMinuteId
* path:/core/base/time/Time.py (line:113)


formatTime
----------


* params: epoch,formatstr,local
* path:/core/base/time/Time.py (line:65)


Returns a formatted time string representing the current time

See http://docs.python.org/lib/module-time.html#l2h-2826 for an
overview of available formatting options.




get5MinuteId
------------


* params: epoch
* path:/core/base/time/Time.py (line:116)


is # 5 min from jan 1 2010


getDayId
--------


* params: epoch
* path:/core/base/time/Time.py (line:122)


is # day from jan 1 2010


getDeltaTime
------------


* params: txt
* path:/core/base/time/Time.py (line:128)


only supported now is -3m, -3d and -3h  (ofcourse 3 can be any int)
and an int which would be just be returned
means 3 days ago 3 hours ago
if 0 or '' then is now


getEpochAgo
-----------


* params: txt
* path:/core/base/time/Time.py (line:142)


only supported now is -3m, -3d and -3h  (ofcourse 3 can be any int)
and an int which would be just be returned
means 3 days ago 3 hours ago
if 0 or '' then is now


getEpochFuture
--------------


* params: txt
* path:/core/base/time/Time.py (line:153)


only supported now is +3d and +3h  (ofcourse 3 can be any int)
+3d means 3 days in future
and an int which would be just be returned
if txt==None or 0 then will be 1 day ago


getHourId
---------


* params: epoch
* path:/core/base/time/Time.py (line:107)


is # hour from jan 1 2010


getLocalTimeHR
--------------


* params:
* path:/core/base/time/Time.py (line:55)


Get the current local date and time in a human-readable form


getLocalTimeHRForFilesystem
---------------------------


* params:
* path:/core/base/time/Time.py (line:61)


getMinuteId
-----------


* params: epoch
* path:/core/base/time/Time.py (line:96)


is # min from jan 1 2010


getSecondsInHR
--------------


* params: seconds
* path:/core/base/time/Time.py (line:31)


getTimeEpoch
------------


* params:
* path:/core/base/time/Time.py (line:20)


Get epoch timestamp (number of seconds passed since January 1, 1970)


getTimeEpochBin
---------------


* params:
* path:/core/base/time/Time.py (line:48)


Get epoch timestamp (number of seconds passed since January 1, 1970)


