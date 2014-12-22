
j.tools.docker.client
=====================

`Source <https://github.com/Jumpscale/jumpscale_core/tree/master/lib/JumpScalepython.zip//docker/client.py>`_


attach
------


* params: container,stdout,stderr,stream,logs
* path:python.zip//docker/client.py (line:331)


attach_socket
-------------


* params: container,params,ws
* path:python.zip//docker/client.py (line:363)


build
-----


* params: path,tag,quiet,fileobj,nocache,rm,stream,timeout,custom_context,encoding
* path:python.zip//docker/client.py (line:381)


close
-----


* params:
* path:python.zip//docker/client.py (line:644)


Closes all adapters and as such the session


commit
------


* params: container,repository,tag,message,author,conf
* path:python.zip//docker/client.py (line:457)


containers
----------


* params: quiet,all,trunc,latest,since,before,limit,size
* path:python.zip//docker/client.py (line:470)


copy
----


* params: container,resource
* path:python.zip//docker/client.py (line:487)


create_container
----------------


* params: image,command,hostname,user,detach,stdin_open,tty,mem_limit,ports,environment,dns,volumes,volumes_from,network_disabled,name,entrypoint,cpu_shares,working_dir,domainname,memswap_limit
* path:python.zip//docker/client.py (line:498)


create_container_from_config
----------------------------


* params: config,name
* path:python.zip//docker/client.py (line:516)


delete
------


* params: url
* path:python.zip//docker/client.py (line:522)


Sends a DELETE request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param kwargs: Optional arguments that `'request'` takes.


diff
----


* params: container
* path:python.zip//docker/client.py (line:524)


events
------


* params:
* path:python.zip//docker/client.py (line:530)


export
------


* params: container
* path:python.zip//docker/client.py (line:533)


get
---


* params: url
* path:python.zip//docker/client.py (line:461)


Sends a GET request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param kwargs: Optional arguments that `'request'` takes.


get_adapter
-----------


* params: url
* path:python.zip//docker/client.py (line:634)


Returns the appropriate connnection adapter for the given URL.


get_image
---------


* params: image
* path:python.zip//docker/client.py (line:541)


head
----


* params: url
* path:python.zip//docker/client.py (line:481)


Sends a HEAD request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param kwargs: Optional arguments that `'request'` takes.


history
-------


* params: image
* path:python.zip//docker/client.py (line:547)


images
------


* params: name,quiet,all,viz
* path:python.zip//docker/client.py (line:552)


import_image
------------


* params: src,repository,tag,image
* path:python.zip//docker/client.py (line:568)


info
----


* params:
* path:python.zip//docker/client.py (line:597)


insert
------


* params: image,url,path
* path:python.zip//docker/client.py (line:601)


inspect_container
-----------------


* params: container
* path:python.zip//docker/client.py (line:613)


inspect_image
-------------


* params: image_id
* path:python.zip//docker/client.py (line:620)


kill
----


* params: container,signal
* path:python.zip//docker/client.py (line:626)


load_image
----------


* params: data
* path:python.zip//docker/client.py (line:637)


login
-----


* params: username,password,email,registry,reauth
* path:python.zip//docker/client.py (line:641)


logs
----


* params: container,stdout,stderr,stream,timestamps
* path:python.zip//docker/client.py (line:669)


merge_environment_settings
--------------------------


* params: url,proxies,stream,verify,cert
* path:python.zip//docker/client.py (line:610)


Check the environment and merge it with some settings.


mount
-----


* params: prefix,adapter
* path:python.zip//docker/client.py (line:649)


Registers a connection adapter to a prefix.

Adapters are sorted in descending order by key length.


options
-------


* params: url
* path:python.zip//docker/client.py (line:471)


Sends a OPTIONS request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param kwargs: Optional arguments that `'request'` takes.


patch
-----


* params: url,data
* path:python.zip//docker/client.py (line:512)


Sends a PATCH request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:'Request'.
:param kwargs: Optional arguments that `'request'` takes.


ping
----


* params:
* path:python.zip//docker/client.py (line:698)


port
----


* params: container,private_port
* path:python.zip//docker/client.py (line:701)


post
----


* params: url,data,json
* path:python.zip//docker/client.py (line:491)


Sends a POST request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:'Request'.
:param json: (optional) json to send in the body of the :class:'Request'.
:param kwargs: Optional arguments that `'request'` takes.


prepare_request
---------------


* params: request
* path:python.zip//docker/client.py (line:338)


Constructs a :class:'PreparedRequest <PreparedRequest>' for
transmission and returns it. The :class:'PreparedRequest' has settings
merged from the :class:'Request <Request>' instance and those of the
:class:'Session'.

:param request: :class:'Request' instance to prepare with this
session's settings.


pull
----


* params: repository,tag,stream,insecure_registry
* path:python.zip//docker/client.py (line:716)


push
----


* params: repository,tag,stream,insecure_registry
* path:python.zip//docker/client.py (line:753)


put
---


* params: url,data
* path:python.zip//docker/client.py (line:502)


Sends a PUT request. Returns :class:'Response' object.

:param url: URL for the new :class:'Request' object.
:param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:'Request'.
:param kwargs: Optional arguments that `'request'` takes.


rebuild_auth
------------


* params: prepared_request,response
* path:python.zip//docker/client.py (line:197)


When being redirected we may want to strip authentication from the
request to avoid leaking credentials. This method intelligently removes
and reapplies authentication where possible to avoid credential loss.


rebuild_proxies
---------------


* params: prepared_request,proxies
* path:python.zip//docker/client.py (line:222)


This method re-evaluates the proxy configuration by considering the
environment variables. If we are redirected to a URL covered by
NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
proxy keys for this URL (in case they were stripped by a previous
redirect).

This method also replaces the Proxy-Authorization header where
necessary.


remove_container
----------------


* params: container,v,link,force
* path:python.zip//docker/client.py (line:787)


remove_image
------------


* params: image,force,noprune
* path:python.zip//docker/client.py (line:795)


request
-------


* params: method,url,params,data,headers,cookies,files,auth,timeout,allow_redirects,proxies,hooks,stream,verify,cert,json
* path:python.zip//docker/client.py (line:378)


Constructs a :class:'Request <Request>', prepares it and sends it.
Returns :class:'Response <Response>' object.

:param method: method for the new :class:'Request' object.
:param url: URL for the new :class:'Request' object.
:param params: (optional) Dictionary or bytes to be sent in the query
string for the :class:'Request'.
:param data: (optional) Dictionary or bytes to send in the body of the
:class:'Request'.
:param json: (optional) json to send in the body of the
:class:'Request'.
:param headers: (optional) Dictionary of HTTP Headers to send with the
:class:'Request'.
:param cookies: (optional) Dict or CookieJar object to send with the
:class:'Request'.
:param files: (optional) Dictionary of `''filename': file-like-objects'`
for multipart encoding upload.
:param auth: (optional) Auth tuple or callable to enable
Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How long to wait for the server to send
data before giving up, as a float, or a (`connect timeout, read
timeout <user/advanced.html#timeouts>`_) tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Set to True by default.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol to the URL of
the proxy.
:param stream: (optional) whether to immediately download the response
content. Defaults to `'False'`.
:param verify: (optional) if `'True'`, the SSL cert will be verified.
A CA_BUNDLE path can also be provided.
:param cert: (optional) if String, path to ssl client cert file (.pem).
If Tuple, ('cert', 'key') pair.


resize
------


* params: container,height,width
* path:python.zip//docker/client.py (line:888)


resolve_redirects
-----------------


* params: resp,req,stream,timeout,verify,cert,proxies
* path:python.zip//docker/client.py (line:89)


Receives a Response. Returns a generator of Responses.


restart
-------


* params: container,timeout
* path:python.zip//docker/client.py (line:800)


search
------


* params: term
* path:python.zip//docker/client.py (line:808)


send
----


* params: request
* path:python.zip//docker/client.py (line:531)


Send a given PreparedRequest.


start
-----


* params: container,binds,port_bindings,lxc_conf,publish_all_ports,links,privileged,dns,dns_search,volumes_from,network_mode,restart_policy,cap_add,cap_drop
* path:python.zip//docker/client.py (line:813)


stop
----


* params: container,timeout
* path:python.zip//docker/client.py (line:897)


tag
---


* params: image,repository,tag,force
* path:python.zip//docker/client.py (line:906)


top
---


* params: container
* path:python.zip//docker/client.py (line:917)


version
-------


* params:
* path:python.zip//docker/client.py (line:921)


wait
----


* params: container
* path:python.zip//docker/client.py (line:924)


