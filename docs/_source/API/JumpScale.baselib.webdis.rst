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
   
       <title>JumpScale.baselib.webdis package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.core package" href="JumpScale.core.html" />
       <link rel="prev" title="JumpScale.baselib.watchdog.manager package" href="JumpScale.baselib.watchdog.manager.html" />
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
             <a href="JumpScale.core.html" title="JumpScale.core package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.watchdog.manager.html" title="JumpScale.baselib.watchdog.manager package"
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
   
     <div class="section" id="jumpscale-baselib-webdis-package">
   <h1>JumpScale.baselib.webdis package<a class="headerlink" href="#jumpscale-baselib-webdis-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.webdis.Webdis">
   <span id="jumpscale-baselib-webdis-webdis-module"></span><h2>JumpScale.baselib.webdis.Webdis module<a class="headerlink" href="#module-JumpScale.baselib.webdis.Webdis" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.webdis.Webdis.</tt><tt class="descname">Webdis</tt><big>(</big><em>addr='127.0.0.1'</em>, <em>port=8889</em>, <em>timeout=10</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.blpop">
   <tt class="descname">blpop</tt><big>(</big><em>key</em>, <em>timeout='60'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.blpop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.blpop" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.delete">
   <tt class="descname">delete</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.delete"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.delete" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.execute">
   <tt class="descname">execute</tt><big>(</big><em>cmd</em>, <em>url=''</em>, <em>data=None</em>, <em>die=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.execute"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.execute" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.exists">
   <tt class="descname">exists</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.exists" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.expire">
   <tt class="descname">expire</tt><big>(</big><em>key</em>, <em>timeout</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.expire"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.expire" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.get">
   <tt class="descname">get</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hdelete">
   <tt class="descname">hdelete</tt><big>(</big><em>hkey</em>, <em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hdelete"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hdelete" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hexists">
   <tt class="descname">hexists</tt><big>(</big><em>hkey</em>, <em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hexists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hexists" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hget">
   <tt class="descname">hget</tt><big>(</big><em>hkey</em>, <em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hget"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hget" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hgetall">
   <tt class="descname">hgetall</tt><big>(</big><em>hkey</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hgetall"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hgetall" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hkeys">
   <tt class="descname">hkeys</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hkeys"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hkeys" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.hset">
   <tt class="descname">hset</tt><big>(</big><em>hkey</em>, <em>key</em>, <em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.hset"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.hset" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.incr">
   <tt class="descname">incr</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.incr"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.incr" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.incrby">
   <tt class="descname">incrby</tt><big>(</big><em>key</em>, <em>nr</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.incrby"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.incrby" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.llen">
   <tt class="descname">llen</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.llen"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.llen" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.lpop">
   <tt class="descname">lpop</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.lpop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.lpop" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.ping">
   <tt class="descname">ping</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.ping"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.ping" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.rpush">
   <tt class="descname">rpush</tt><big>(</big><em>key</em>, <em>item</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.rpush"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.rpush" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.Webdis.set">
   <tt class="descname">set</tt><big>(</big><em>key</em>, <em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#Webdis.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.Webdis.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.webdis.Webdis.WebdisFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.webdis.Webdis.</tt><tt class="descname">WebdisFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#WebdisFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.WebdisFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.WebdisFactory.check">
   <tt class="descname">check</tt><big>(</big><em>addr='127.0.0.1'</em>, <em>port=7779</em>, <em>timeout=1</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#WebdisFactory.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.WebdisFactory.check" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.WebdisFactory.get">
   <tt class="descname">get</tt><big>(</big><em>addr='127.0.0.1'</em>, <em>port=7779</em>, <em>timeout=10</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#WebdisFactory.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.WebdisFactory.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.webdis.Webdis.WebdisFactory.getByInstance">
   <tt class="descname">getByInstance</tt><big>(</big><em>instance=None</em>, <em>timeout=10</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/webdis/Webdis.html#WebdisFactory.getByInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.webdis.Webdis.WebdisFactory.getByInstance" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.webdis">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.webdis" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.webdis package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.webdis.Webdis">JumpScale.baselib.webdis.Webdis module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.webdis">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.watchdog.manager.html"
                           title="previous chapter">JumpScale.baselib.watchdog.manager package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.core.html"
                           title="next chapter">JumpScale.core package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.webdis.txt"
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
             <a href="JumpScale.core.html" title="JumpScale.core package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.watchdog.manager.html" title="JumpScale.baselib.watchdog.manager package"
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
       <li><a href="../_sources/API/JumpScale.baselib.webdis.txt"
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