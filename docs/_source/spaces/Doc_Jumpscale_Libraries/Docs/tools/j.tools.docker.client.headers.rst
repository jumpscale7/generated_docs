
j.tools.docker.client.headers
=============================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/requests/structures.py>`_


A case-insensitive `'dict'`-like object.

Implements all methods and operations of
`'collections.MutableMapping'` as well as dict's `'copy'`. Also
provides `'lower_items'`.

All keys are expected to be strings. The structure remembers the
case of the last key to be set, and `'iter(instance)'`,
`'keys()'`, `'items()'`, `'iterkeys()'`, and `'iteritems()'`
will contain case-sensitive keys. However, querying and contains
testing is case insensitive::

cid = CaseInsensitiveDict()
cid`'Accept' <'Accept'>`_ = 'application/json'
cid`'aCCEPT' <'aCCEPT'>`_ == 'application/json'  # True
list(cid) == `'Accept' <'Accept'>`_  # True

For example, `'headers`'content-encoding' <'content-encoding'>`_'` will return the
value of a `''Content-Encoding''` response header, regardless
of how the header name was originally stored.

If the constructor, `'.update'`, or equality comparison
operations are given keys that have equal `'.lower()'`s, the
behavior is undefined.


clear
-----


* params:
* path:/lib/requests/structures.py (line:518)


D.clear() -> None.  Remove all items from D.


copy
----


* params:
* path:/lib/requests/structures.py (line:82)


get
---


* params: key,default
* path:/lib/requests/structures.py (line:360)


D.get(k`,d <,d>`_) -> D`k <k>`_ if k in D, else d.  d defaults to None.


items
-----


* params:
* path:/lib/requests/structures.py (line:393)


D.items() -> list of D's (key, value) pairs, as 2-tuples


iteritems
---------


* params:
* path:/lib/requests/structures.py (line:384)


D.iteritems() -> an iterator over the (key, value) items of D


iterkeys
--------


* params:
* path:/lib/requests/structures.py (line:375)


D.iterkeys() -> an iterator over the keys of D


itervalues
----------


* params:
* path:/lib/requests/structures.py (line:379)


D.itervalues() -> an iterator over the values of D


keys
----


* params:
* path:/lib/requests/structures.py (line:389)


D.keys() -> list of D's keys


lower_items
-----------


* params:
* path:/lib/requests/structures.py (line:65)


Like iteritems(), but with all lowercase keys.


pop
---


* params: key,default
* path:/lib/requests/structures.py (line:492)


D.pop(k`,d <,d>`_) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


popitem
-------


* params:
* path:/lib/requests/structures.py (line:506)


D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


setdefault
----------


* params: key,default
* path:/lib/requests/structures.py (line:552)


D.setdefault(k`,d <,d>`_) -> D.get(k,d), also set D`k <k>`_=d if k not in D


update
------


* params:
* path:/lib/requests/structures.py (line:526)


D.update(`E,  <E, >`_**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D`k <k>`_ = E`k <k>`_
If E present and lacks .keys() method, does:     for (k, v) in E: D`k <k>`_ = v
In either case, this is followed by: for k, v in F.items(): D`k <k>`_ = v


values
------


* params:
* path:/lib/requests/structures.py (line:397)


D.values() -> list of D's values


