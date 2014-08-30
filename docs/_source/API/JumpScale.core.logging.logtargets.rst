.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.core.logging.logtargets package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="up" title="JumpScale.core.logging package" href="JumpScale.core.logging.html" />
       <link rel="next" title="JumpScale.core.pmtypes package" href="JumpScale.core.pmtypes.html" />
       <link rel="prev" title="JumpScale.core.logging package" href="JumpScale.core.logging.html" /> 
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
             <a href="JumpScale.core.pmtypes.html" title="JumpScale.core.pmtypes package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.logging.html" title="JumpScale.core.logging package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" >JumpScale.core package</a> &raquo;</li>
             <li><a href="JumpScale.core.logging.html" accesskey="U">JumpScale.core.logging package</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <div class="section" id="jumpscale-core-logging-logtargets-package">
   <h1>JumpScale.core.logging.logtargets package<a class="headerlink" href="#jumpscale-core-logging-logtargets-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.core.logging.logtargets.LogTargetFS">
   <span id="jumpscale-core-logging-logtargets-logtargetfs-module"></span><h2>JumpScale.core.logging.logtargets.LogTargetFS module<a class="headerlink" href="#module-JumpScale.core.logging.logtargets.LogTargetFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.logging.logtargets.LogTargetFS.</tt><tt class="descname">LogTargetFS</tt><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>log to local filesystem</p>
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.checkTarget">
   <tt class="descname">checkTarget</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.checkTarget"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.checkTarget" title="Permalink to this definition">¶</a></dt>
   <dd><p>check status of target, if ok return True
   for std out always True</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.close">
   <tt class="descname">close</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.close"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.close" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.log">
   <tt class="descname">log</tt><big>(</big><em>log</em>, <em>skipQueue=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.log" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.open">
   <tt class="descname">open</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.open"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.open" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.rotate">
   <tt class="descname">rotate</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetFS.html#LogTargetFS.rotate"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetFS.LogTargetFS.rotate" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.logging.logtargets.LogTargetLogForwarder">
   <span id="jumpscale-core-logging-logtargets-logtargetlogforwarder-module"></span><h2>JumpScale.core.logging.logtargets.LogTargetLogForwarder module<a class="headerlink" href="#module-JumpScale.core.logging.logtargets.LogTargetLogForwarder" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.logging.logtargets.LogTargetLogForwarder.</tt><tt class="descname">LogTargetLogForwarder</tt><big>(</big><em>serverip='127.0.0.1'</em>, <em>port=7768</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetLogForwarder.html#LogTargetLogForwarder"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder" title="Permalink to this definition">¶</a></dt>
   <dd><p>Forwards incoming logRecords to redis</p>
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.checkTarget">
   <tt class="descname">checkTarget</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetLogForwarder.html#LogTargetLogForwarder.checkTarget"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.checkTarget" title="Permalink to this definition">¶</a></dt>
   <dd><p>check status of target, if ok return True</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.log">
   <tt class="descname">log</tt><big>(</big><em>log</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetLogForwarder.html#LogTargetLogForwarder.log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.log" title="Permalink to this definition">¶</a></dt>
   <dd><p>forward the already encoded message to the target destination</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.logECO">
   <tt class="descname">logECO</tt><big>(</big><em>eco</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetLogForwarder.html#LogTargetLogForwarder.logECO"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetLogForwarder.LogTargetLogForwarder.logECO" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="jumpscale-core-logging-logtargets-logtargetscribe-module">
   <h2>JumpScale.core.logging.logtargets.LogTargetScribe module<a class="headerlink" href="#jumpscale-core-logging-logtargets-logtargetscribe-module" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.core.logging.logtargets.LogTargetStdOut">
   <span id="jumpscale-core-logging-logtargets-logtargetstdout-module"></span><h2>JumpScale.core.logging.logtargets.LogTargetStdOut module<a class="headerlink" href="#module-JumpScale.core.logging.logtargets.LogTargetStdOut" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.logging.logtargets.LogTargetStdOut.</tt><tt class="descname">LogTargetStdOut</tt><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetStdOut.html#LogTargetStdOut"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.checkTarget">
   <tt class="descname">checkTarget</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetStdOut.html#LogTargetStdOut.checkTarget"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.checkTarget" title="Permalink to this definition">¶</a></dt>
   <dd><p>check status of target, if ok return True
   for std out always True</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.close">
   <tt class="descname">close</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetStdOut.html#LogTargetStdOut.close"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.close" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.log">
   <tt class="descname">log</tt><big>(</big><em>log</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetStdOut.html#LogTargetStdOut.log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetStdOut.LogTargetStdOut.log" title="Permalink to this definition">¶</a></dt>
   <dd><p>log to stdout use q.loghandler.reformatMessageToHR() 
   example 1|754545|performancetester|5||copy file from a to b
   &#64;param message string in format time(epoch)|source(string)|level(0-10)|tags|logmessage</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole">
   <span id="jumpscale-core-logging-logtargets-logtargettopylabslogconsole-module"></span><h2>JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole module<a class="headerlink" href="#module-JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.</tt><tt class="descname">LogTargetToJumpScaleLogConsole</tt><big>(</big><em>serverip='localhost'</em>, <em>serverport=9998</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetToPylabsLogConsole.html#LogTargetToJumpScaleLogConsole"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Forwards incoming logRecords to TCP-server</p>
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.checkTarget">
   <tt class="descname">checkTarget</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetToPylabsLogConsole.html#LogTargetToJumpScaleLogConsole.checkTarget"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.checkTarget" title="Permalink to this definition">¶</a></dt>
   <dd><p>check status of target, if ok return True
   for std out always True</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.close">
   <tt class="descname">close</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetToPylabsLogConsole.html#LogTargetToJumpScaleLogConsole.close"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.close" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.log">
   <tt class="descname">log</tt><big>(</big><em>log</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetToPylabsLogConsole.html#LogTargetToJumpScaleLogConsole.log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.log" title="Permalink to this definition">¶</a></dt>
   <dd><p>forward the already formatted message to the target destination</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.open">
   <tt class="descname">open</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/logging/logtargets/LogTargetToPylabsLogConsole.html#LogTargetToJumpScaleLogConsole.open"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole.LogTargetToJumpScaleLogConsole.open" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.logging.logtargets">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.core.logging.logtargets" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.core.logging.logtargets package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.logging.logtargets.LogTargetFS">JumpScale.core.logging.logtargets.LogTargetFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.logging.logtargets.LogTargetLogForwarder">JumpScale.core.logging.logtargets.LogTargetLogForwarder module</a></li>
   <li><a class="reference internal" href="#jumpscale-core-logging-logtargets-logtargetscribe-module">JumpScale.core.logging.logtargets.LogTargetScribe module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.logging.logtargets.LogTargetStdOut">JumpScale.core.logging.logtargets.LogTargetStdOut module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole">JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.logging.logtargets">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.core.logging.html"
                           title="previous chapter">JumpScale.core.logging package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.core.pmtypes.html"
                           title="next chapter">JumpScale.core.pmtypes package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.core.logging.logtargets.txt"
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
             <a href="JumpScale.core.pmtypes.html" title="JumpScale.core.pmtypes package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.logging.html" title="JumpScale.core.logging package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" >JumpScale.core package</a> &raquo;</li>
             <li><a href="JumpScale.core.logging.html" >JumpScale.core.logging package</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>