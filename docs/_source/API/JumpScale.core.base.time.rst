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
   
       <title>JumpScale.core.base.time package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="up" title="JumpScale.core.base package" href="JumpScale.core.base.html" />
       <link rel="next" title="JumpScale.core.baseclasses package" href="JumpScale.core.baseclasses.html" />
       <link rel="prev" title="JumpScale.core.base.idgenerator package" href="JumpScale.core.base.idgenerator.html" />
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
             <a href="JumpScale.core.baseclasses.html" title="JumpScale.core.baseclasses package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.base.idgenerator.html" title="JumpScale.core.base.idgenerator package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" >JumpScale.core package</a> &raquo;</li>
             <li><a href="JumpScale.core.base.html" accesskey="U">JumpScale.core.base package</a> &raquo;</li>
         </ul>
       </div>
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
   
     <div class="section" id="jumpscale-core-base-time-package">
   <h1>JumpScale.core.base.time package<a class="headerlink" href="#jumpscale-core-base-time-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.core.base.time.Time">
   <span id="jumpscale-core-base-time-time-module"></span><h2>JumpScale.core.base.time.Time module<a class="headerlink" href="#module-JumpScale.core.base.time.Time" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.base.time.Time.Time">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.base.time.Time.</tt><tt class="descname">Time</tt><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time" title="Permalink to this definition">¶</a></dt>
   <dd><p>generic provider of time functions
   lives at j.base.time</p>
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.HRDatetoEpoch">
   <tt class="descname">HRDatetoEpoch</tt><big>(</big><em>datestr</em>, <em>local=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.HRDatetoEpoch"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.HRDatetoEpoch" title="Permalink to this definition">¶</a></dt>
   <dd><p>convert string date to epoch
   Date needs to be formatted as 16/06/1988</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.epoch2HRDate">
   <tt class="descname">epoch2HRDate</tt><big>(</big><em>epoch</em>, <em>local=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.epoch2HRDate"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.epoch2HRDate" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.epoch2HRDateTime">
   <tt class="descname">epoch2HRDateTime</tt><big>(</big><em>epoch</em>, <em>local=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.epoch2HRDateTime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.epoch2HRDateTime" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.epoch2HRTime">
   <tt class="descname">epoch2HRTime</tt><big>(</big><em>epoch</em>, <em>local=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.epoch2HRTime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.epoch2HRTime" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.fiveMinuteIdToEpoch">
   <tt class="descname">fiveMinuteIdToEpoch</tt><big>(</big><em>fiveMinuteId</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.fiveMinuteIdToEpoch"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.fiveMinuteIdToEpoch" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.formatTime">
   <tt class="descname">formatTime</tt><big>(</big><em>epoch</em>, <em>formatstr='%Y/%m/%d %H:%M:%S'</em>, <em>local=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.formatTime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.formatTime" title="Permalink to this definition">¶</a></dt>
   <dd><p>Returns a formatted time string representing the current time</p>
   <p>See <a class="reference external" href="http://docs.python.org/lib/module-time.html#l2h-2826">http://docs.python.org/lib/module-time.html#l2h-2826</a> for an
   overview of available formatting options.</p>
   <p>&#64;param format: Format string
   &#64;type format: string</p>
   <p>&#64;returns: Formatted current time
   &#64;rtype: string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.get5MinuteId">
   <tt class="descname">get5MinuteId</tt><big>(</big><em>epoch=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.get5MinuteId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.get5MinuteId" title="Permalink to this definition">¶</a></dt>
   <dd><p>is # 5 min from jan 1 2010</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getDayId">
   <tt class="descname">getDayId</tt><big>(</big><em>epoch=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getDayId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getDayId" title="Permalink to this definition">¶</a></dt>
   <dd><p>is # day from jan 1 2010</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getEpochAgo">
   <tt class="descname">getEpochAgo</tt><big>(</big><em>txt</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getEpochAgo"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getEpochAgo" title="Permalink to this definition">¶</a></dt>
   <dd><p>only supported now is -3m, -3d and -3h  (ofcourse 3 can be any int)
   and an int which would be just be returned
   means 3 days ago 3 hours ago
   if 0 or &#8216;&#8217; then is now</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getEpochFuture">
   <tt class="descname">getEpochFuture</tt><big>(</big><em>txt</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getEpochFuture"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getEpochFuture" title="Permalink to this definition">¶</a></dt>
   <dd><p>only supported now is +3d and +3h  (ofcourse 3 can be any int)
   +3d means 3 days in future
   and an int which would be just be returned
   if txt==None or 0 then will be 1 day ago</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getHourId">
   <tt class="descname">getHourId</tt><big>(</big><em>epoch=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getHourId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getHourId" title="Permalink to this definition">¶</a></dt>
   <dd><p>is # hour from jan 1 2010</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getLocalTimeHR">
   <tt class="descname">getLocalTimeHR</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getLocalTimeHR"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getLocalTimeHR" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get the current local date and time in a human-readable form</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getLocalTimeHRForFilesystem">
   <tt class="descname">getLocalTimeHRForFilesystem</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getLocalTimeHRForFilesystem"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getLocalTimeHRForFilesystem" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getMinuteId">
   <tt class="descname">getMinuteId</tt><big>(</big><em>epoch=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getMinuteId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getMinuteId" title="Permalink to this definition">¶</a></dt>
   <dd><p>is # min from jan 1 2010</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getTimeEpoch">
   <tt class="descname">getTimeEpoch</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getTimeEpoch"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getTimeEpoch" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get epoch timestamp (number of seconds passed since January 1, 1970)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.base.time.Time.Time.getTimeEpochBin">
   <tt class="descname">getTimeEpochBin</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/base/time/Time.html#Time.getTimeEpochBin"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.base.time.Time.Time.getTimeEpochBin" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get epoch timestamp (number of seconds passed since January 1, 1970)</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.base.time">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.core.base.time" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.core.base.time package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.base.time.Time">JumpScale.core.base.time.Time module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.base.time">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.core.base.idgenerator.html"
                           title="previous chapter">JumpScale.core.base.idgenerator package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.core.baseclasses.html"
                           title="next chapter">JumpScale.core.baseclasses package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.core.base.time.txt"
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
             <a href="JumpScale.core.baseclasses.html" title="JumpScale.core.baseclasses package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.base.idgenerator.html" title="JumpScale.core.base.idgenerator package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" >JumpScale.core package</a> &raquo;</li>
             <li><a href="JumpScale.core.base.html" >JumpScale.core.base package</a> &raquo;</li>
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
       <li><a href="../_sources/API/JumpScale.core.base.time.txt"
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