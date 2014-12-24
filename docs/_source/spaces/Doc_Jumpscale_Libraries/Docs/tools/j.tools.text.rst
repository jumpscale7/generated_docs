
j.tools.text
============

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/core/system/text.py>`_


addCmd
------


* params: out,entity,cmd
* path:/core/system/text.py (line:82)


addTimeHR
---------


* params: line,epoch,start
* path:/core/system/text.py (line:87)


addVal
------


* params: out,name,val,addtimehr
* path:/core/system/text.py (line:96)


ask
---


* params: content
* path:/core/system/text.py (line:118)


look for @ASK statements in text, where found replace with input from user

syntax for ask is:

descr, default & regex can be between '' if spaces inside

types are: str,float,int,bool,dropdown

retry means will keep on retrying x times until ask is done properly

dropdownvals is comma separated list of values to ask for when type dropdown



dealWithQuote
-------------


* params: text
* path:/core/system/text.py (line:544)


look for 'something,else' the comma needs to be converted to


eval
----


* params: code
* path:/core/system/text.py (line:334)



getBool
-------


* params: text
* path:/core/system/text.py (line:529)


getDict
-------


* params: text,ttype,deserialize
* path:/core/system/text.py (line:580)


keys are always treated as string


getFloat
--------


* params: text
* path:/core/system/text.py (line:513)


getInt
------


* params: text
* path:/core/system/text.py (line:497)


getList
-------


* params: text,ttype,deserialize
* path:/core/system/text.py (line:554)



getMacroCandidates
------------------


* params: txt
* path:/core/system/text.py (line:241)



hrd2machinetext
---------------


* params: value
* path:/core/system/text.py (line:420)


'something ' removes ''
all spaces & commas & : inside ' '  are converted
SPACE ->
" ->
, ->
: ->

->



isNumeric
---------


* params: txt
* path:/core/system/text.py (line:114)


machinetext2hrd
---------------


* params: value,quote
* path:/core/system/text.py (line:448)


do reverse of:
SPACE ->
" ->
, ->
: ->

->



machinetext2str
---------------


* params: value
* path:/core/system/text.py (line:479)


do reverse of:
SPACE ->
" ->
, ->
: ->

->



prefix
------


* params: prefix,txt
* path:/core/system/text.py (line:43)


prefix_remove
-------------


* params: prefix,txt,onlyPrefix
* path:/core/system/text.py (line:51)



prefix_remove_withtrailing
--------------------------


* params: prefix,txt,onlyPrefix
* path:/core/system/text.py (line:66)


there can be chars for prefix (e.g. '< :*: aline'  and this function looking for :*: would still work and ignore '< ')


pythonObjToStr
--------------


* params: text,multiline
* path:/core/system/text.py (line:370)


try to convert a python object to string representation works for None, bool, integer, float, dict, list


pythonObjToStr1line
-------------------


* params: text,quote
* path:/core/system/text.py (line:354)


replaceQuotes
-------------


* params: value,replacewith
* path:/core/system/text.py (line:442)


str2var
-------


* params: string
* path:/core/system/text.py (line:282)


convert list, dict of strings
or convert 1 string to python objects


strToPythonObj
--------------


* params: str
* path:/core/system/text.py (line:350)


toAscii
-------


* params: value,maxlen
* path:/core/system/text.py (line:21)


toStr
-----


* params: value,codec
* path:/core/system/text.py (line:12)


toUnicode
---------


* params: value,codec
* path:/core/system/text.py (line:34)


