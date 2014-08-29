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
   
       <title>JumpScale.baselib.lrucache package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.baselib.mailclient package" href="JumpScale.baselib.mailclient.html" />
       <link rel="prev" title="JumpScale.baselib.key_value_store package" href="JumpScale.baselib.key_value_store.html" />
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
             <a href="JumpScale.baselib.mailclient.html" title="JumpScale.baselib.mailclient package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.key_value_store.html" title="JumpScale.baselib.key_value_store package"
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
   
     <div class="section" id="jumpscale-baselib-lrucache-package">
   <h1>JumpScale.baselib.lrucache package<a class="headerlink" href="#jumpscale-baselib-lrucache-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.lrucache.LRUCache">
   <span id="jumpscale-baselib-lrucache-lrucache-module"></span><h2>JumpScale.baselib.lrucache.LRUCache module<a class="headerlink" href="#module-JumpScale.baselib.lrucache.LRUCache" title="Permalink to this headline">¶</a></h2>
   <p>a simple LRU (Least-Recently-Used) cache module</p>
   <p>This module provides very simple LRU (Least-Recently-Used) cache
   functionality.</p>
   <p>An <em>in-memory cache</em> is useful for storing the results of an
   &#8216;expensive&#8217; process (one that takes a lot of time or resources) for
   later re-use. Typical examples are accessing data from the filesystem,
   a database, or a network location. If you know you&#8217;ll need to re-read
   the data again, it can help to keep it in a cache.</p>
   <p>You <em>can</em> use a Python dictionary as a cache for some purposes.
   However, if the results you&#8217;re caching are large, or you have a lot of
   possible results, this can be impractical memory-wise.</p>
   <p>An <em>LRU cache</em>, on the other hand, only keeps _some_ of the results in
   memory, which keeps you from overusing resources. The cache is bounded
   by a maximum size; if you try to add more values to the cache, it will
   automatically discard the values that you haven&#8217;t read or written to
   in the longest time. In other words, the least-recently-used items are
   discarded. <a href="#id2"><span class="problematic" id="id3"><span id="id1"></span>[1]_</span></a></p>
   <dl class="exception">
   <dt id="JumpScale.baselib.lrucache.LRUCache.CacheKeyError">
   <em class="property">exception </em><tt class="descclassname">JumpScale.baselib.lrucache.LRUCache.</tt><tt class="descname">CacheKeyError</tt><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCache.html#CacheKeyError"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCache.CacheKeyError" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/exceptions.html#exceptions.KeyError" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">exceptions.KeyError</span></tt></a></p>
   <p>Error raised when cache requests fail</p>
   <p>When a cache record is accessed which no longer exists (or never did),
   this error is raised. To avoid it, you may want to check for the existence
   of a cache record before reading or deleting it.</p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.lrucache.LRUCache.LRUCache">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.lrucache.LRUCache.</tt><tt class="descname">LRUCache</tt><big>(</big><em>size=16</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCache.html#LRUCache"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCache.LRUCache" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.lrucache.LRUCache.LRUCache.mtime">
   <tt class="descname">mtime</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCache.html#LRUCache.mtime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCache.LRUCache.mtime" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return the last modification time for the cache record with key.
   May be useful for cache instances where the stored values can get
   &#8216;stale&#8217;, such as caching file or network resource contents.</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.lrucache.LRUCache.LRUCache.size">
   <tt class="descname">size</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCache.LRUCache.size" title="Permalink to this definition">¶</a></dt>
   <dd><p>Maximum size of the cache.
   If more than &#8216;size&#8217; elements are added to the cache,
   the least-recently-used ones will be discarded.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="data">
   <dt id="JumpScale.baselib.lrucache.LRUCache.DEFAULT_SIZE">
   <tt class="descclassname">JumpScale.baselib.lrucache.LRUCache.</tt><tt class="descname">DEFAULT_SIZE</tt><em class="property"> = 16</em><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCache.DEFAULT_SIZE" title="Permalink to this definition">¶</a></dt>
   <dd><p>Default size of a new LRUCache object, if no &#8216;size&#8217; argument is given.</p>
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.lrucache.LRUCacheFactory">
   <span id="jumpscale-baselib-lrucache-lrucachefactory-module"></span><h2>JumpScale.baselib.lrucache.LRUCacheFactory module<a class="headerlink" href="#module-JumpScale.baselib.lrucache.LRUCacheFactory" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.lrucache.LRUCacheFactory.</tt><tt class="descname">LRUCacheFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCacheFactory.html#LRUCacheFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory.getRCache">
   <tt class="descname">getRCache</tt><big>(</big><em>nritems</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCacheFactory.html#LRUCacheFactory.getRCache"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory.getRCache" title="Permalink to this definition">¶</a></dt>
   <dd><p>Least-Recently-Used (LRU) cache.
   Written by <a class="reference external" href="http://evan.prodromou.name/Software/Python/LRUCache">http://evan.prodromou.name/Software/Python/LRUCache</a></p>
   <p>Instances of this class provide a least-recently-used (LRU) cache. They
   emulate a Python mapping type. You can use an LRU cache more or less like
   a Python dictionary, with the exception that objects you put into the
   cache may be discarded before you take them out.</p>
   <p>Some example usage:</p>
   <p>cache = LRUCache(32) # new cache
   cache[&#8216;foo&#8217;] = get_file_contents(&#8216;foo&#8217;) # or whatever</p>
   <dl class="docutils">
   <dt>if &#8216;foo&#8217; in cache: # if it&#8217;s still in cache...</dt>
   <dd># use cached version
   contents = cache[&#8216;foo&#8217;]</dd>
   <dt>else:</dt>
   <dd># recalculate
   contents = get_file_contents(&#8216;foo&#8217;)
   # store in cache for next time
   cache[&#8216;foo&#8217;] = contents</dd>
   </dl>
   <p>print cache.size # Maximum size</p>
   <p>print len(cache) # 0 &lt;= len(cache) &lt;= cache.size</p>
   <p>cache.size = 10 # Auto-shrink on size assignment</p>
   <dl class="docutils">
   <dt>for i in range(50): # note: larger than cache size</dt>
   <dd>cache[i] = i</dd>
   </dl>
   <p>if 0 not in cache: print &#8216;Zero was discarded.&#8217;</p>
   <dl class="docutils">
   <dt>if 42 in cache:</dt>
   <dd>del cache[42] # Manual deletion</dd>
   <dt>for j in cache:   # iterate (in LRU order)</dt>
   <dd>print j, cache[j] # iterator produces keys, not values</dd>
   </dl>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory.getRWCache">
   <tt class="descname">getRWCache</tt><big>(</big><em>nrItemsReadCache</em>, <em>nrItemsWriteCache=50</em>, <em>maxTimeWriteCache=2000</em>, <em>writermethod=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/LRUCacheFactory.html#LRUCacheFactory.getRWCache"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.LRUCacheFactory.LRUCacheFactory.getRWCache" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.lrucache.RWCache">
   <span id="jumpscale-baselib-lrucache-rwcache-module"></span><h2>JumpScale.baselib.lrucache.RWCache module<a class="headerlink" href="#module-JumpScale.baselib.lrucache.RWCache" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.lrucache.RWCache.RWCache">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.lrucache.RWCache.</tt><tt class="descname">RWCache</tt><big>(</big><em>nrItemsReadCache</em>, <em>maxNrItemsWriteCache=50</em>, <em>maxTimeWriteCache=2000</em>, <em>writermethod=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#RWCache"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.RWCache" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.lrucache.RWCache.RWCache.flush">
   <tt class="descname">flush</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#RWCache.flush"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.RWCache.flush" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.lrucache.RWCache.RWCache.set">
   <tt class="descname">set</tt><big>(</big><em>key</em>, <em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#RWCache.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.RWCache.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.lrucache.RWCache.WCache">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.lrucache.RWCache.</tt><tt class="descname">WCache</tt><big>(</big><em>size=5000</em>, <em>writermethod=None</em>, <em>maxtime=1</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#WCache"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.WCache" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.lrucache.RWCache.WCache.flush">
   <tt class="descname">flush</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#WCache.flush"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.WCache.flush" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.lrucache.RWCache.WCache.mtime">
   <tt class="descname">mtime</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache/RWCache.html#WCache.mtime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.RWCache.WCache.mtime" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return the last modification time for the cache record with key.
   May be useful for cache instances where the stored values can get
   &#8216;stale&#8217;, such as caching file or network resource contents.</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.lrucache">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.lrucache" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.lrucache.Empty">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.lrucache.</tt><tt class="descname">Empty</tt><a class="reference internal" href="../_modules/JumpScale/baselib/lrucache.html#Empty"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.lrucache.Empty" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.lrucache package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.lrucache.LRUCache">JumpScale.baselib.lrucache.LRUCache module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.lrucache.LRUCacheFactory">JumpScale.baselib.lrucache.LRUCacheFactory module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.lrucache.RWCache">JumpScale.baselib.lrucache.RWCache module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.lrucache">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.key_value_store.html"
                           title="previous chapter">JumpScale.baselib.key_value_store package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.mailclient.html"
                           title="next chapter">JumpScale.baselib.mailclient package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.lrucache.txt"
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
             <a href="JumpScale.baselib.mailclient.html" title="JumpScale.baselib.mailclient package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.key_value_store.html" title="JumpScale.baselib.key_value_store package"
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
       <li><a href="../_sources/API/JumpScale.baselib.lrucache.txt"
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