.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>&lt;no title&gt; &mdash; Jumpscale Doc 7.0 documentation</title>
       
       <link rel="stylesheet" href="../_static/default.css" type="text/css" />
       <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
       
       <script type="text/javascript">
         var DOCUMENTATION_OPTIONS = {
           URL_ROOT:    '../',
           VERSION:     '7.0',
           COLLAPSE_INDEX: false,
           FILE_SUFFIX: '.html',
           HAS_SOURCE:  true
         };
       </script>
       <script type="text/javascript" src="../_static/jquery.js"></script>
       <script type="text/javascript" src="../_static/underscore.js"></script>
       <script type="text/javascript" src="../_static/doctools.js"></script>
       <link rel="top" title="Jumpscale Doc 7.0 documentation" href="../index.html" /> 
     </head>
     <body>
       <div class="related">
         <h3>Navigation</h3>
         <ul>
           <li class="right" style="margin-right: 10px">
             <a href="../genindex.html" title="General Index"
                accesskey="I">index</a></li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   
       <title>JumpScale.baselib.redis package &mdash; Jumpscale Doc 7.0 documentation</title>
   
       <link rel="stylesheet" href="../_static/default.css" type="text/css" />
       <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
   
       <script type="text/javascript">
         var DOCUMENTATION_OPTIONS = {
           URL_ROOT:    '../',
           VERSION:     '7.0',
           COLLAPSE_INDEX: false,
           FILE_SUFFIX: '.html',
           HAS_SOURCE:  true
         };
       </script>
       <script type="text/javascript" src="../_static/jquery.js"></script>
       <script type="text/javascript" src="../_static/underscore.js"></script>
       <script type="text/javascript" src="../_static/doctools.js"></script>
       <link rel="top" title="Jumpscale Doc 7.0 documentation" href="../index.html" />
       <link rel="up" title="JumpScale.baselib package" href="JumpScale.baselib.html" />
       <link rel="next" title="JumpScale.baselib.redisworker package" href="JumpScale.baselib.redisworker.html" />
       <link rel="prev" title="JumpScale.baselib.platforms.ubuntu package" href="JumpScale.baselib.platforms.ubuntu.html" />
     </head>
     <body>
       <div class="related">
         <h3>Navigation</h3>
         <ul>
           <li class="right" style="margin-right: 10px">
             <a href="../genindex.html" title="General Index"
                accesskey="I">index</a></li>
           <li class="right" >
             <a href="../py-modindex.html" title="Python Module Index"
                >modules</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.redisworker.html" title="JumpScale.baselib.redisworker package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.platforms.ubuntu.html" title="JumpScale.baselib.platforms.ubuntu package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" accesskey="U">JumpScale.baselib package</a> &raquo;</li>
         </ul>
       </div>
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
   
     <div class="section" id="jumpscale-baselib-redis-package">
   <h1>JumpScale.baselib.redis package<a class="headerlink" href="#jumpscale-baselib-redis-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.redis.Redis">
   <span id="jumpscale-baselib-redis-redis-module"></span><h2>JumpScale.baselib.redis.Redis module<a class="headerlink" href="#module-JumpScale.baselib.redis.Redis" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.redis.Redis.GeventRedis">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.redis.Redis.</tt><tt class="descname">GeventRedis</tt><big>(</big><em>host='localhost'</em>, <em>port=6379</em>, <em>db=0</em>, <em>password=None</em>, <em>socket_timeout=None</em>, <em>connection_pool=None</em>, <em>charset='utf-8'</em>, <em>errors='strict'</em>, <em>decode_responses=False</em>, <em>unix_socket_path=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#GeventRedis"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.GeventRedis" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.baselib.redis.Redis.Redis" title="JumpScale.baselib.redis.Redis.Redis"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.baselib.redis.Redis.Redis</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.GeventRedis.hgetall">
   <tt class="descname">hgetall</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#GeventRedis.hgetall"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.GeventRedis.hgetall" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return a Python dict of the hash&#8217;s name/value pairs</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.redis.Redis.Redis">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.redis.Redis.</tt><tt class="descname">Redis</tt><big>(</big><em>host='localhost'</em>, <em>port=6379</em>, <em>db=0</em>, <em>password=None</em>, <em>socket_timeout=None</em>, <em>connection_pool=None</em>, <em>charset='utf-8'</em>, <em>errors='strict'</em>, <em>decode_responses=False</em>, <em>unix_socket_path=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#Redis"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.Redis" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">redis.client.Redis</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.Redis.getDict">
   <tt class="descname">getDict</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#Redis.getDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.Redis.getDict" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.Redis.hgetalldict">
   <tt class="descname">hgetalldict</tt><big>(</big><em>name</em><big>)</big><a class="headerlink" href="#JumpScale.baselib.redis.Redis.Redis.hgetalldict" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return a Python dict of the hash&#8217;s name/value pairs</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.redis.Redis.RedisDict">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.redis.Redis.</tt><tt class="descname">RedisDict</tt><big>(</big><em>client</em>, <em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisDict" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">dict</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisDict.copy">
   <tt class="descname">copy</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisDict.copy"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisDict.copy" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisDict.iteritems">
   <tt class="descname">iteritems</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisDict.iteritems"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisDict.iteritems" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisDict.keys">
   <tt class="descname">keys</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisDict.keys"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisDict.keys" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisDict.pop">
   <tt class="descname">pop</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisDict.pop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisDict.pop" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.redis.Redis.</tt><tt class="descname">RedisFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.checkAllInstances">
   <tt class="descname">checkAllInstances</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.checkAllInstances"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.checkAllInstances" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.configureInstance">
   <tt class="descname">configureInstance</tt><big>(</big><em>name</em>, <em>port</em>, <em>maxram=200</em>, <em>appendonly=True</em>, <em>snapshot=False</em>, <em>slave=()</em>, <em>ismaster=False</em>, <em>passwd=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.configureInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.configureInstance" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param maxram = MB of ram
   slave example: (192.168.10.10,8888,asecret)   (ip,port,secret)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.deleteInstance">
   <tt class="descname">deleteInstance</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.deleteInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.deleteInstance" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.emptyAllInstances">
   <tt class="descname">emptyAllInstances</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.emptyAllInstances"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.emptyAllInstances" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.emptyInstance">
   <tt class="descname">emptyInstance</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.emptyInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.emptyInstance" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getGeventRedisClient">
   <tt class="descname">getGeventRedisClient</tt><big>(</big><em>ipaddr</em>, <em>port</em>, <em>fromcache=True</em>, <em>password=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getGeventRedisClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getGeventRedisClient" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getGeventRedisQueue">
   <tt class="descname">getGeventRedisQueue</tt><big>(</big><em>ipaddr</em>, <em>port</em>, <em>name</em>, <em>namespace='queues'</em>, <em>fromcache=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getGeventRedisQueue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getGeventRedisQueue" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getPort">
   <tt class="descname">getPort</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getPort"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getPort" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getProcessPids">
   <tt class="descname">getProcessPids</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getProcessPids"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getProcessPids" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getRedisClient">
   <tt class="descname">getRedisClient</tt><big>(</big><em>ipaddr</em>, <em>port</em>, <em>password=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getRedisClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getRedisClient" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.getRedisQueue">
   <tt class="descname">getRedisQueue</tt><big>(</big><em>ipaddr</em>, <em>port</em>, <em>name</em>, <em>namespace='queues'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.getRedisQueue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.getRedisQueue" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.startInstance">
   <tt class="descname">startInstance</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.startInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.startInstance" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.redis.Redis.RedisFactory.stopInstance">
   <tt class="descname">stopInstance</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/redis/Redis.html#RedisFactory.stopInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.redis.Redis.RedisFactory.stopInstance" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.redis">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.redis" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.redis package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.redis.Redis">JumpScale.baselib.redis.Redis module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.redis">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.platforms.ubuntu.html"
                           title="previous chapter">JumpScale.baselib.platforms.ubuntu package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.redisworker.html"
                           title="next chapter">JumpScale.baselib.redisworker package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.redis.txt"
              rel="nofollow">Show Source</a></li>
     </ul>
   <div id="searchbox" style="display: none">
     <h3>Quick search</h3>
       <form class="search" action="../search.html" method="get">
         <input type="text" name="q" />
         <input type="submit" value="Go" />
         <input type="hidden" name="check_keywords" value="yes" />
         <input type="hidden" name="area" value="default" />
       </form>
       <p class="searchtip" style="font-size: 90%">
       Enter search terms or a module, class or function name.
       </p>
   </div>
   <script type="text/javascript">$('#searchbox').show(0);</script>
           </div>
         </div>
         <div class="clearer"></div>
       </div>
       <div class="related">
         <h3>Navigation</h3>
         <ul>
           <li class="right" style="margin-right: 10px">
             <a href="../genindex.html" title="General Index"
                >index</a></li>
           <li class="right" >
             <a href="../py-modindex.html" title="Python Module Index"
                >modules</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.redisworker.html" title="JumpScale.baselib.redisworker package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.platforms.ubuntu.html" title="JumpScale.baselib.platforms.ubuntu package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" >JumpScale.baselib package</a> &raquo;</li>
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.redis.txt"
              rel="nofollow">Show Source</a></li>
     </ul>
   <div id="searchbox" style="display: none">
     <h3>Quick search</h3>
       <form class="search" action="../search.html" method="get">
         <input type="text" name="q" />
         <input type="submit" value="Go" />
         <input type="hidden" name="check_keywords" value="yes" />
         <input type="hidden" name="area" value="default" />
       </form>
       <p class="searchtip" style="font-size: 90%">
       Enter search terms or a module, class or function name.
       </p>
   </div>
   <script type="text/javascript">$('#searchbox').show(0);</script>
           </div>
         </div>
         <div class="clearer"></div>
       </div>
       <div class="related">
         <h3>Navigation</h3>
         <ul>
           <li class="right" style="margin-right: 10px">
             <a href="../genindex.html" title="General Index"
                >index</a></li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>