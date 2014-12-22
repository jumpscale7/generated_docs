
j.tools.docker.client.cookies
=============================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScale/lib/requests/cookies.py>`_


Compatibility class; is a cookielib.CookieJar, but exposes a dict interface.

This is the CookieJar we create by default for requests and sessions that
don't specify one, since some clients may expect response.cookies and
session.cookies to support dict operations.

Don't use the dict interface internally; it's just for compatibility with
with external client code. All 'requests' code should work out of the box
with externally provided instances of CookieJar, e.g., LWPCookieJar and
FileCookieJar.

Caution: dictionary operations that are normally O(1) may be O(n).

Unlike a regular CookieJar, this class is pickleable.


add_cookie_header
-----------------


* params: request
* path:/lib/requests/cookies.py (line:1312)


Add correct Cookie: header to request (urllib2.Request object).

The Cookie2 header is also added unless policy.hide_cookie2 is true.


clear
-----


* params: domain,path,name
* path:/lib/requests/cookies.py (line:1649)


Clear some cookies.

Invoking this method without arguments will clear all cookies.  If
given a single argument, only cookies belonging to that domain will be
removed.  If given two arguments, cookies belonging to the specified
path within that domain are removed.  If given three arguments, then
the cookie with the specified name, path and domain is removed.

Raises KeyError if no matching cookie exists.


clear_expired_cookies
---------------------


* params:
* path:/lib/requests/cookies.py (line:1691)


Discard all expired cookies.

You probably don't need to call this method: expired cookies are never
sent back to the server (provided you're using DefaultCookiePolicy),
this method is called by CookieJar itself every so often, and the
.save() method won't save expired cookies anyway (unless you ask
otherwise by passing a true ignore_expires argument).


clear_session_cookies
---------------------


* params:
* path:/lib/requests/cookies.py (line:1676)


Discard all session cookies.

Note that the .save() method won't save session cookies anyway, unless
you ask otherwise by passing a true ignore_discard argument.


copy
----


* params:
* path:/lib/requests/cookies.py (line:346)


Return a copy of this RequestsCookieJar.


extract_cookies
---------------


* params: response,request
* path:/lib/requests/cookies.py (line:1635)


Extract cookies from response, where allowable given the request.


get
---


* params: name,default,domain,path
* path:/lib/requests/cookies.py (line:176)


Dict-like get() that also supports optional domain and path args in
order to resolve naming collisions from using one cookie jar over
multiple domains. Caution: operation is O(n), not O(1).


get_dict
--------


* params: domain,path
* path:/lib/requests/cookies.py (line:261)


Takes as an argument an optional domain and path and returns a plain old
Python dict of name-value pairs of cookies that meet the requirements.


items
-----


* params:
* path:/lib/requests/cookies.py (line:229)


Dict-like items() that returns a list of name-value tuples from the jar.
See keys() and values(). Allows client-code to call "dict(RequestsCookieJar)
and get a vanilla python dict of key value pairs.


iteritems
---------


* params:
* path:/lib/requests/cookies.py (line:223)


Dict-like iteritems() that returns an iterator of name-value tuples from the jar.
See iterkeys() and itervalues().


iterkeys
--------


* params:
* path:/lib/requests/cookies.py (line:201)


Dict-like iterkeys() that returns an iterator of names of cookies from the jar.
See itervalues() and iteritems().


itervalues
----------


* params:
* path:/lib/requests/cookies.py (line:212)


Dict-like itervalues() that returns an iterator of values of cookies from the jar.
See iterkeys() and iteritems().


keys
----


* params:
* path:/lib/requests/cookies.py (line:207)


Dict-like keys() that returns a list of names of cookies from the jar.
See values() and items().


list_domains
------------


* params:
* path:/lib/requests/cookies.py (line:235)


Utility method to list all the domains in the jar.


list_paths
----------


* params:
* path:/lib/requests/cookies.py (line:243)


Utility method to list all the paths in the jar.


make_cookies
------------


* params: response,request
* path:/lib/requests/cookies.py (line:1555)


Return sequence of Cookie objects extracted from response object.


multiple_domains
----------------


* params:
* path:/lib/requests/cookies.py (line:251)


Returns True if there are multiple domains in the jar.
Returns False otherwise.


pop
---


* params: key,default
* path:/lib/requests/cookies.py (line:492)


D.pop(k,d <,d>) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


popitem
-------


* params:
* path:/lib/requests/cookies.py (line:506)


D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


set
---


* params: name,value
* path:/lib/requests/cookies.py (line:185)


Dict-like set() that also supports optional domain and path args in
order to resolve naming collisions from using one cookie jar over
multiple domains.


set_cookie
----------


* params: cookie
* path:/lib/requests/cookies.py (line:289)


set_cookie_if_ok
----------------


* params: cookie,request
* path:/lib/requests/cookies.py (line:1609)


Set a cookie if policy says it's OK to do so.


set_policy
----------


* params: policy
* path:/lib/requests/cookies.py (line:1225)


setdefault
----------


* params: key,default
* path:/lib/requests/cookies.py (line:552)


D.setdefault(k,d <,d>) -> D.get(k,d), also set Dk <k>=d if k not in D


update
------


* params: other
* path:/lib/requests/cookies.py (line:294)


Updates this jar with cookies from another CookieJar or dict-like


values
------


* params:
* path:/lib/requests/cookies.py (line:218)


Dict-like values() that returns a list of values of cookies from the jar.
See keys() and items().


