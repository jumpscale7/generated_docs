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
   
       <title>JumpScale.baselib.vcs package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.baselib.watchdog package" href="JumpScale.baselib.watchdog.html" />
       <link rel="prev" title="JumpScale.baselib.units package" href="JumpScale.baselib.units.html" />
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
             <a href="JumpScale.baselib.watchdog.html" title="JumpScale.baselib.watchdog package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.units.html" title="JumpScale.baselib.units package"
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
   
     <div class="section" id="jumpscale-baselib-vcs-package">
   <h1>JumpScale.baselib.vcs package<a class="headerlink" href="#jumpscale-baselib-vcs-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.vcs.vcsfactory">
   <span id="jumpscale-baselib-vcs-vcsfactory-module"></span><h2>JumpScale.baselib.vcs.vcsfactory module<a class="headerlink" href="#module-JumpScale.baselib.vcs.vcsfactory" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.vcs.vcsfactory.</tt><tt class="descname">VCSClient</tt><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient.checkout">
   <tt class="descname">checkout</tt><big>(</big><em>revision</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient.checkout"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient.checkout" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient.clone">
   <tt class="descname">clone</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient.clone"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient.clone" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient.init">
   <tt class="descname">init</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient.init"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient.init" title="Permalink to this definition">¶</a></dt>
   <dd><p>Make sure repo exist clone if not existing</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient.push">
   <tt class="descname">push</tt><big>(</big><em>force=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient.push"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient.push" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSClient.update">
   <tt class="descname">update</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSClient.update"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient.update" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSConfig">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.vcs.vcsfactory.</tt><tt class="descname">VCSConfig</tt><big>(</big><em>provider</em>, <em>account</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSConfig"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSConfig" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="attribute">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSConfig.login">
   <tt class="descname">login</tt><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSConfig.login"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSConfig.login" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSConfig.passwd">
   <tt class="descname">passwd</tt><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSConfig.passwd"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSConfig.passwd" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.vcs.vcsfactory.</tt><tt class="descname">VCSFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSFactory" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSFactory.getClient">
   <tt class="descname">getClient</tt><big>(</big><em>type</em>, <em>provider</em>, <em>account</em>, <em>reponame</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSFactory.getClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSFactory.getClient" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSGITClient">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.vcs.vcsfactory.</tt><tt class="descname">VCSGITClient</tt><big>(</big><em>client</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSGITClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSGITClient" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient" title="JumpScale.baselib.vcs.vcsfactory.VCSClient"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.baselib.vcs.vcsfactory.VCSClient</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSGITClient.clone">
   <tt class="descname">clone</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSGITClient.clone"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSGITClient.clone" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSGITClient.init">
   <tt class="descname">init</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSGITClient.init"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSGITClient.init" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSGITClient.push">
   <tt class="descname">push</tt><big>(</big><em>force=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSGITClient.push"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSGITClient.push" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSGITClient.update">
   <tt class="descname">update</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSGITClient.update"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSGITClient.update" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSHGClient">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.vcs.vcsfactory.</tt><tt class="descname">VCSHGClient</tt><big>(</big><em>client</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSHGClient"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSHGClient" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.baselib.vcs.vcsfactory.VCSClient" title="JumpScale.baselib.vcs.vcsfactory.VCSClient"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.baselib.vcs.vcsfactory.VCSClient</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSHGClient.clone">
   <tt class="descname">clone</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSHGClient.clone"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSHGClient.clone" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSHGClient.init">
   <tt class="descname">init</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSHGClient.init"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSHGClient.init" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSHGClient.push">
   <tt class="descname">push</tt><big>(</big><em>force=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSHGClient.push"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSHGClient.push" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.vcs.vcsfactory.VCSHGClient.update">
   <tt class="descname">update</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/vcs/vcsfactory.html#VCSHGClient.update"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.vcs.vcsfactory.VCSHGClient.update" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.vcs">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.vcs" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.vcs package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.vcs.vcsfactory">JumpScale.baselib.vcs.vcsfactory module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.vcs">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.units.html"
                           title="previous chapter">JumpScale.baselib.units package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.watchdog.html"
                           title="next chapter">JumpScale.baselib.watchdog package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.vcs.txt"
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
             <a href="JumpScale.baselib.watchdog.html" title="JumpScale.baselib.watchdog package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.units.html" title="JumpScale.baselib.units package"
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
       <li><a href="../_sources/API/JumpScale.baselib.vcs.txt"
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