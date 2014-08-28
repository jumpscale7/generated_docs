.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.params package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.performancetrace package" href="JumpScale.baselib.performancetrace.html" />
       <link rel="prev" title="JumpScale.baselib.netconfig package" href="JumpScale.baselib.netconfig.html" /> 
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
             <a href="JumpScale.baselib.performancetrace.html" title="JumpScale.baselib.performancetrace package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.netconfig.html" title="JumpScale.baselib.netconfig package"
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
               
     <div class="section" id="jumpscale-baselib-params-package">
   <h1>JumpScale.baselib.params package<a class="headerlink" href="#jumpscale-baselib-params-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.params.Params">
   <span id="jumpscale-baselib-params-params-module"></span><h2>JumpScale.baselib.params.Params module<a class="headerlink" href="#module-JumpScale.baselib.params.Params" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.params.Params.Params">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.params.Params.</tt><tt class="descname">Params</tt><big>(</big><em>dictObject=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.expandParams">
   <tt class="descname">expandParams</tt><big>(</big><em>**kwargs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.expandParams"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.expandParams" title="Permalink to this definition">¶</a></dt>
   <dd><p>adds paramsExtra, tags &amp; params from requestContext if it exists
   returns params but not needed because params just get modified to have all these extra arguments/params as properties
   set default as params to this method e.g.
   expandParams(id=10,hight=100)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.expandParamsAsDict">
   <tt class="descname">expandParamsAsDict</tt><big>(</big><em>**kwargs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.expandParamsAsDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.expandParamsAsDict" title="Permalink to this definition">¶</a></dt>
   <dd><p>adds paramsExtra, tags &amp; params from requestContext if it exists
   return as dict</p>
   <p>for each item given as named argument check it is already in dict and if not add
   e.g. args=self.expandParamsAsDict(id=1,name=&#8221;test&#8221;)
   will return a dict with id &amp; name and these values unless if they were set in the params already
   can further use it as follows:
   params.result=infomgr.getInfoWithHeaders(<a href="#id1"><span class="problematic" id="id2">**</span></a>args)</p>
   <p>args=params.expandParamsAsDict(maxvalues=100,id=None,start=&#8221;-3d&#8221;,stop=None)</p>
   <p>args[&#8220;start&#8221;]=j.base.time.getEpochAgo(args[&#8220;start&#8221;])
   args[&#8220;stop&#8221;]=j.base.time.getEpochFuture(args[&#8220;stop&#8221;])</p>
   <p>params.result=j.apps.system.infomgr.extensions.infomgr.addInfo(<a href="#id3"><span class="problematic" id="id4">**</span></a>args)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.extend">
   <tt class="descname">extend</tt><big>(</big><em>params</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.extend"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.extend" title="Permalink to this definition">¶</a></dt>
   <dd><p>Update this Params object with the contents of the argument Params
   object</p>
   <p>&#64;param params: the Params or dict object to update from
   &#64;type params: dict or Params
   &#64;raise TypeError: if the argument is not a dict or Params object</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.get">
   <tt class="descname">get</tt><big>(</big><em>key</em>, <em>defaultvalue=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.getDict">
   <tt class="descname">getDict</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.getDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.getDict" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.getTag">
   <tt class="descname">getTag</tt><big>(</big><em>name</em>, <em>default=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.getTag"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.getTag" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.has_key">
   <tt class="descname">has_key</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.has_key"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.has_key" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.merge">
   <tt class="descname">merge</tt><big>(</big><em>otherParams</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.merge"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.merge" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.pop">
   <tt class="descname">pop</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.pop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.pop" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.Params.setDict">
   <tt class="descname">setDict</tt><big>(</big><em>dictObject</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#Params.setDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.Params.setDict" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.params.Params.ParamsFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.params.Params.</tt><tt class="descname">ParamsFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#ParamsFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.ParamsFactory" title="Permalink to this definition">¶</a></dt>
   <dd><p>This factory can create new Params objects</p>
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.ParamsFactory.get">
   <tt class="descname">get</tt><big>(</big><em>dictObject={}</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#ParamsFactory.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.ParamsFactory.get" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create and return a new Params object</p>
   <p>&#64;param dictObject when dict given then dict will be converted into params
   &#64;return: a new Params object
   &#64;rtype: Params</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.params.Params.ParamsFactory.isParams">
   <tt class="descname">isParams</tt><big>(</big><em>p</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/params/Params.html#ParamsFactory.isParams"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.params.Params.ParamsFactory.isParams" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return if the argument object is an instance of Params</p>
   <p>&#64;param p: object to check
   &#64;type p: object
   &#64;return: Whether or not <cite>p</cite> is a Params instance
   &#64;rtype: boolean</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.params">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.params" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.params package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.params.Params">JumpScale.baselib.params.Params module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.params">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.netconfig.html"
                           title="previous chapter">JumpScale.baselib.netconfig package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.performancetrace.html"
                           title="next chapter">JumpScale.baselib.performancetrace package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.params.txt"
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
             <a href="JumpScale.baselib.performancetrace.html" title="JumpScale.baselib.performancetrace package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.netconfig.html" title="JumpScale.baselib.netconfig package"
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