.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.stataggregator package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.statmanager package" href="JumpScale.baselib.statmanager.html" />
       <link rel="prev" title="JumpScale.baselib.startupmanager package" href="JumpScale.baselib.startupmanager.html" /> 
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
             <a href="JumpScale.baselib.statmanager.html" title="JumpScale.baselib.statmanager package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.startupmanager.html" title="JumpScale.baselib.startupmanager package"
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
               
     <div class="section" id="jumpscale-baselib-stataggregator-package">
   <h1>JumpScale.baselib.stataggregator package<a class="headerlink" href="#jumpscale-baselib-stataggregator-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.stataggregator.StatAggregator">
   <span id="jumpscale-baselib-stataggregator-stataggregator-module"></span><h2>JumpScale.baselib.stataggregator.StatAggregator module<a class="headerlink" href="#module-JumpScale.baselib.stataggregator.StatAggregator" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.stataggregator.StatAggregator.</tt><tt class="descname">Stat</tt><big>(</big><em>period=3600</em>, <em>memonly=False</em>, <em>percent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat.clean">
   <tt class="descname">clean</tt><big>(</big><em>now</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat.clean"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat.clean" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat.dump">
   <tt class="descname">dump</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat.dump"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat.dump" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat.getAvgMax">
   <tt class="descname">getAvgMax</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat.getAvgMax"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat.getAvgMax" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;return (avg,max)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat.load">
   <tt class="descname">load</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat.load"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat.load" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.Stat.set">
   <tt class="descname">set</tt><big>(</big><em>now</em>, <em>val</em>, <em>remember=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#Stat.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.stataggregator.StatAggregator.</tt><tt class="descname">StatAggregator</tt><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.clean">
   <tt class="descname">clean</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.clean"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.clean" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.delete">
   <tt class="descname">delete</tt><big>(</big><em>prefix</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.delete"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.delete" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.get">
   <tt class="descname">get</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.getAvgMax">
   <tt class="descname">getAvgMax</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.getAvgMax"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.getAvgMax" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.getTime">
   <tt class="descname">getTime</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.getTime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.getTime" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.list">
   <tt class="descname">list</tt><big>(</big><em>prefix=''</em>, <em>memonly=False</em>, <em>avgmax=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.list" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.loadStat">
   <tt class="descname">loadStat</tt><big>(</big><em>key=None</em>, <em>data=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.loadStat"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.loadStat" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.registerStats">
   <tt class="descname">registerStats</tt><big>(</big><em>key</em>, <em>ttype='N'</em>, <em>memonly=False</em>, <em>percent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.registerStats"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.registerStats" title="Permalink to this definition">¶</a></dt>
   <dd><p>type is N or D (D from diff)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.send2carbon">
   <tt class="descname">send2carbon</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.send2carbon"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.send2carbon" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.send2log">
   <tt class="descname">send2log</tt><big>(</big><em>name</em>, <em>key</em>, <em>val</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.send2log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.send2log" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.set">
   <tt class="descname">set</tt><big>(</big><em>key</em>, <em>val</em>, <em>ttype='N'</em>, <em>remember=True</em>, <em>memonly=False</em>, <em>percent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatAggregator.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatAggregator.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.stataggregator.StatAggregator.</tt><tt class="descname">StatDiffPerSec</tt><big>(</big><em>period=3600</em>, <em>memonly=False</em>, <em>percent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatDiffPerSec"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.baselib.stataggregator.StatAggregator.Stat" title="JumpScale.baselib.stataggregator.StatAggregator.Stat"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.baselib.stataggregator.StatAggregator.Stat</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec.getAvgMax">
   <tt class="descname">getAvgMax</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatDiffPerSec.getAvgMax"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec.getAvgMax" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;return (avg,max)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec.set">
   <tt class="descname">set</tt><big>(</big><em>now</em>, <em>val</em>, <em>remember=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/StatAggregator.html#StatDiffPerSec.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.StatAggregator.StatDiffPerSec.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.stataggregator.redisstataggregator">
   <span id="jumpscale-baselib-stataggregator-redisstataggregator-module"></span><h2>JumpScale.baselib.stataggregator.redisstataggregator module<a class="headerlink" href="#module-JumpScale.baselib.stataggregator.redisstataggregator" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.stataggregator.redisstataggregator.</tt><tt class="descname">RedisStatAggregator</tt><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/redisstataggregator.html#RedisStatAggregator"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator.popStats">
   <tt class="descname">popStats</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/redisstataggregator.html#RedisStatAggregator.popStats"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator.popStats" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator.pushStats">
   <tt class="descname">pushStats</tt><big>(</big><em>key</em>, <em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/stataggregator/redisstataggregator.html#RedisStatAggregator.pushStats"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.stataggregator.redisstataggregator.RedisStatAggregator.pushStats" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.stataggregator">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.stataggregator" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.stataggregator package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.stataggregator.StatAggregator">JumpScale.baselib.stataggregator.StatAggregator module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.stataggregator.redisstataggregator">JumpScale.baselib.stataggregator.redisstataggregator module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.stataggregator">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.startupmanager.html"
                           title="previous chapter">JumpScale.baselib.startupmanager package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.statmanager.html"
                           title="next chapter">JumpScale.baselib.statmanager package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.stataggregator.txt"
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
             <a href="JumpScale.baselib.statmanager.html" title="JumpScale.baselib.statmanager package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.startupmanager.html" title="JumpScale.baselib.startupmanager package"
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