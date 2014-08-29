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
   
       <title>JumpScale.baselib.cmdline package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.baselib.cmdutils package" href="JumpScale.baselib.cmdutils.html" />
       <link rel="prev" title="JumpScale.baselib.cloudsystemfs package" href="JumpScale.baselib.cloudsystemfs.html" />
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
             <a href="JumpScale.baselib.cmdutils.html" title="JumpScale.baselib.cmdutils package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.cloudsystemfs.html" title="JumpScale.baselib.cloudsystemfs package"
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
   
     <div class="section" id="jumpscale-baselib-cmdline-package">
   <h1>JumpScale.baselib.cmdline package<a class="headerlink" href="#jumpscale-baselib-cmdline-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.cmdline.CommandLauncher">
   <span id="jumpscale-baselib-cmdline-commandlauncher-module"></span><h2>JumpScale.baselib.cmdline.CommandLauncher module<a class="headerlink" href="#module-JumpScale.baselib.cmdline.CommandLauncher" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cmdline.CommandLauncher.</tt><tt class="descname">CommandLauncher</tt><big>(</big><em>cmd</em>, <em>workingdir</em>, <em>name=''</em>, <em>setDaemon=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cmdline/CommandLauncher.html#CommandLauncher"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/threading.html#threading.Thread" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">threading.Thread</span></tt></a></p>
   <dl class="attribute">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.cmd">
   <tt class="descname">cmd</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.cmd" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.name">
   <tt class="descname">name</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.name" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.output">
   <tt class="descname">output</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.output" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.run">
   <tt class="descname">run</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cmdline/CommandLauncher.html#CommandLauncher.run"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.run" title="Permalink to this definition">¶</a></dt>
   <dd><p>Run the command launcher</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.setDaemon">
   <tt class="descname">setDaemon</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.setDaemon" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.workingdir">
   <tt class="descname">workingdir</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cmdline.CommandLauncher.CommandLauncher.workingdir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cmdline.Options">
   <span id="jumpscale-baselib-cmdline-options-module"></span><h2>JumpScale.baselib.cmdline.Options module<a class="headerlink" href="#module-JumpScale.baselib.cmdline.Options" title="Permalink to this headline">¶</a></h2>
   <p>Generic option parser class. This class can be used
   to write code that will parse command line options for
   an application by invoking one of the standard Python
   library command argument parser modules optparse or
   getopt.</p>
   <p>To parse the arguments, call the method &#8216;parse_arguments&#8217;.
   The return value is a dictionary of the option-value pairs.</p>
   <dl class="class">
   <dt id="JumpScale.baselib.cmdline.Options.GenericOptionParser">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cmdline.Options.</tt><tt class="descname">GenericOptionParser</tt><big>(</big><em>optmap</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cmdline/Options.html#GenericOptionParser"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cmdline.Options.GenericOptionParser" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generic option parser using either C{optparse} or C{getopt}</p>
   <dl class="method">
   <dt id="JumpScale.baselib.cmdline.Options.GenericOptionParser.parse_arguments">
   <tt class="descname">parse_arguments</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cmdline/Options.html#GenericOptionParser.parse_arguments"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cmdline.Options.GenericOptionParser.parse_arguments" title="Permalink to this definition">¶</a></dt>
   <dd><p>Parse command line arguments and
   return a dictionary of option-value pairs</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="exception">
   <dt id="JumpScale.baselib.cmdline.Options.GenericOptionParserError">
   <em class="property">exception </em><tt class="descclassname">JumpScale.baselib.cmdline.Options.</tt><tt class="descname">GenericOptionParserError</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cmdline/Options.html#GenericOptionParserError"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cmdline.Options.GenericOptionParserError" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/exceptions.html#exceptions.Exception" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">exceptions.Exception</span></tt></a></p>
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cmdline">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.cmdline" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.cmdline package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cmdline.CommandLauncher">JumpScale.baselib.cmdline.CommandLauncher module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cmdline.Options">JumpScale.baselib.cmdline.Options module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cmdline">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.cloudsystemfs.html"
                           title="previous chapter">JumpScale.baselib.cloudsystemfs package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.cmdutils.html"
                           title="next chapter">JumpScale.baselib.cmdutils package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.cmdline.txt"
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
             <a href="JumpScale.baselib.cmdutils.html" title="JumpScale.baselib.cmdutils package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.cloudsystemfs.html" title="JumpScale.baselib.cloudsystemfs package"
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
       <li><a href="../_sources/API/JumpScale.baselib.cmdline.txt"
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