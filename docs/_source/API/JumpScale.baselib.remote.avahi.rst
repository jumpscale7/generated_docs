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
   
       <title>JumpScale.baselib.remote.avahi package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="up" title="JumpScale.baselib.remote package" href="JumpScale.baselib.remote.html" />
       <link rel="next" title="JumpScale.baselib.remote.cluster package" href="JumpScale.baselib.remote.cluster.html" />
       <link rel="prev" title="JumpScale.baselib.remote package" href="JumpScale.baselib.remote.html" />
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
             <a href="JumpScale.baselib.remote.cluster.html" title="JumpScale.baselib.remote.cluster package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.remote.html" title="JumpScale.baselib.remote package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" >JumpScale.baselib package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.remote.html" accesskey="U">JumpScale.baselib.remote package</a> &raquo;</li>
         </ul>
       </div>
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
   
     <div class="section" id="jumpscale-baselib-remote-avahi-package">
   <h1>JumpScale.baselib.remote.avahi package<a class="headerlink" href="#jumpscale-baselib-remote-avahi-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.remote.avahi.Avahi">
   <span id="jumpscale-baselib-remote-avahi-avahi-module"></span><h2>JumpScale.baselib.remote.avahi.Avahi module<a class="headerlink" href="#module-JumpScale.baselib.remote.avahi.Avahi" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.Avahi">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.remote.avahi.Avahi.</tt><tt class="descname">Avahi</tt><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#Avahi"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.Avahi" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.Avahi.getServices">
   <tt class="descname">getServices</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#Avahi.getServices"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.Avahi.getServices" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.Avahi.registerService">
   <tt class="descname">registerService</tt><big>(</big><em>servicename</em>, <em>port</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#Avahi.registerService"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.Avahi.registerService" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.Avahi.resolveAddress">
   <tt class="descname">resolveAddress</tt><big>(</big><em>ipAddress</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#Avahi.resolveAddress"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.Avahi.resolveAddress" title="Permalink to this definition">¶</a></dt>
   <dd><p>Resolve the ip address to its hostname</p>
   <p>&#64;param ipAddress: the ip address to resolve
   &#64;type ipAddress: string</p>
   <p>&#64;return: the hostname attached to the ip address</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.AvahiService">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.remote.avahi.Avahi.</tt><tt class="descname">AvahiService</tt><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#AvahiService"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.AvahiService" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.AvahiServices">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.remote.avahi.Avahi.</tt><tt class="descname">AvahiServices</tt><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#AvahiServices"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.AvahiServices" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.AvahiServices.exists">
   <tt class="descname">exists</tt><big>(</big><em>hostname=''</em>, <em>partofname=''</em>, <em>partofdescription=''</em>, <em>port=0</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#AvahiServices.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.AvahiServices.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;return True/False,resultOfServices   #avoids having to wait twice for avahi query</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.remote.avahi.Avahi.AvahiServices.find">
   <tt class="descname">find</tt><big>(</big><em>hostname=''</em>, <em>partofname=''</em>, <em>partofdescription=''</em>, <em>port=0</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/remote/avahi/Avahi.html#AvahiServices.find"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.remote.avahi.Avahi.AvahiServices.find" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.remote.avahi">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.remote.avahi" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.remote.avahi package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.remote.avahi.Avahi">JumpScale.baselib.remote.avahi.Avahi module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.remote.avahi">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.remote.html"
                           title="previous chapter">JumpScale.baselib.remote package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.remote.cluster.html"
                           title="next chapter">JumpScale.baselib.remote.cluster package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.remote.avahi.txt"
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
             <a href="JumpScale.baselib.remote.cluster.html" title="JumpScale.baselib.remote.cluster package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.remote.html" title="JumpScale.baselib.remote package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" >JumpScale.baselib package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.remote.html" >JumpScale.baselib.remote package</a> &raquo;</li>
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
       <li><a href="../_sources/API/JumpScale.baselib.remote.avahi.txt"
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