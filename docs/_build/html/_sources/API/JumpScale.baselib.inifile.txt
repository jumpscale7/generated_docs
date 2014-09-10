.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.inifile package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.installtools package" href="JumpScale.baselib.installtools.html" />
       <link rel="prev" title="JumpScale.baselib.influxdb package" href="JumpScale.baselib.influxdb.html" /> 
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
             <a href="JumpScale.baselib.installtools.html" title="JumpScale.baselib.installtools package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.influxdb.html" title="JumpScale.baselib.influxdb package"
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
               
     <div class="section" id="jumpscale-baselib-inifile-package">
   <h1>JumpScale.baselib.inifile package<a class="headerlink" href="#jumpscale-baselib-inifile-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.inifile.IniFile">
   <span id="jumpscale-baselib-inifile-inifile-module"></span><h2>JumpScale.baselib.inifile.IniFile module<a class="headerlink" href="#module-JumpScale.baselib.inifile.IniFile" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.inifile.IniFile.</tt><tt class="descname">IniFile</tt><big>(</big><em>iniFile</em>, <em>create=False</em>, <em>removeWhenDereferenced=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Use with care:
   - addParam and setParam are &#8216;auto-write&#8217;
   - addSection isn&#8217;t
   - removeSection isn&#8217;t
   - removeParam isn&#8217;t</p>
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.addParam">
   <tt class="descname">addParam</tt><big>(</big><em>sectionName</em>, <em>paramName</em>, <em>newvalue</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.addParam"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.addParam" title="Permalink to this definition">¶</a></dt>
   <dd><p>Add name-value pair to section of IniFile
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter
   &#64;param newValue:    value you wish to assign to the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.addSection">
   <tt class="descname">addSection</tt><big>(</big><em>sectionName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.addSection"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.addSection" title="Permalink to this definition">¶</a></dt>
   <dd><p>Add a new section to this Inifile. If it already existed, silently pass
   &#64;param sectionName: name of the section</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.checkParam">
   <tt class="descname">checkParam</tt><big>(</big><em>sectionName</em>, <em>paramName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.checkParam"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.checkParam" title="Permalink to this definition">¶</a></dt>
   <dd><p>Boolean indicating whether parameter exists under this section in the IniFile
   &#64;param sectionName: name of the section where the param should be located
   &#64;param paramName:   name of the parameter you wish to check</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.checkSection">
   <tt class="descname">checkSection</tt><big>(</big><em>sectionName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.checkSection"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.checkSection" title="Permalink to this definition">¶</a></dt>
   <dd><p>Boolean indicating whether section exists in this IniFile
   &#64;param sectionName: name of the section</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getBooleanValue">
   <tt class="descname">getBooleanValue</tt><big>(</big><em>sectionName</em>, <em>paramName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getBooleanValue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getBooleanValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get boolean value of the specified parameter
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getContent">
   <tt class="descname">getContent</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getContent"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getContent" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get the Inifile content to a string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getFileAsDict">
   <tt class="descname">getFileAsDict</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getFileAsDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getFileAsDict" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getFloatValue">
   <tt class="descname">getFloatValue</tt><big>(</big><em>sectionName</em>, <em>paramName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getFloatValue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getFloatValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get float value of the specified parameter
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getIntValue">
   <tt class="descname">getIntValue</tt><big>(</big><em>sectionName</em>, <em>paramName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getIntValue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getIntValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get an integer value of the specified parameter
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getParams">
   <tt class="descname">getParams</tt><big>(</big><em>sectionName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getParams"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getParams" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return list of params in a certain section of this IniFile
   &#64;param sectionName: Name of the section for which you wish the param</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getSectionAsDict">
   <tt class="descname">getSectionAsDict</tt><big>(</big><em>section</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getSectionAsDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getSectionAsDict" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getSections">
   <tt class="descname">getSections</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getSections"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getSections" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return list of sections from this IniFile</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.getValue">
   <tt class="descname">getValue</tt><big>(</big><em>sectionName</em>, <em>paramName</em>, <em>raw=False</em>, <em>default=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.getValue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.getValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get value of the parameter from this IniFile
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter
   &#64;param raw:         boolean specifying whether you wish the value to be returned raw
   &#64;param default: if given and the value does not exist the default value will be given
   &#64;return: The value</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.removeParam">
   <tt class="descname">removeParam</tt><big>(</big><em>sectionName</em>, <em>paramName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.removeParam"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.removeParam" title="Permalink to this definition">¶</a></dt>
   <dd><p>Remove a param from this IniFile
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.removeSection">
   <tt class="descname">removeSection</tt><big>(</big><em>sectionName</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.removeSection"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.removeSection" title="Permalink to this definition">¶</a></dt>
   <dd><p>Remove a section from this IniFile
   &#64;param sectionName: name of the section</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.setParam">
   <tt class="descname">setParam</tt><big>(</big><em>sectionName</em>, <em>paramName</em>, <em>newvalue</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.setParam"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.setParam" title="Permalink to this definition">¶</a></dt>
   <dd><p>Add name-value pair to section of IniFile
   &#64;param sectionName: name of the section
   &#64;param paramName:   name of the parameter
   &#64;param newValue:    value you wish to assign to the parameter</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.inifile.IniFile.IniFile.write">
   <tt class="descname">write</tt><big>(</big><em>filePath=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#IniFile.write"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.IniFile.write" title="Permalink to this definition">¶</a></dt>
   <dd><p>Write the IniFile content to disk
   This completely overwrites the file
   &#64;param filePath: location where the file will be written</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.inifile.IniFile.InifileTool">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.inifile.IniFile.</tt><tt class="descname">InifileTool</tt><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#InifileTool"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.InifileTool" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="staticmethod">
   <dt id="JumpScale.baselib.inifile.IniFile.InifileTool.new">
   <em class="property">static </em><tt class="descname">new</tt><big>(</big><em>filename</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#InifileTool.new"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.InifileTool.new" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create a new INI file</p>
   <p>&#64;param filename: Filename of INI file
   &#64;type filename: string</p>
   <p>&#64;raises RuntimeError: When the provided filename exists</p>
   <p>&#64;returns: New INI file object
   &#64;rtype: jumpscale.inifile.IniFile.IniFile</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.baselib.inifile.IniFile.InifileTool.open">
   <em class="property">static </em><tt class="descname">open</tt><big>(</big><em>filename</em>, <em>createIfNonExisting=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/inifile/IniFile.html#InifileTool.open"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.inifile.IniFile.InifileTool.open" title="Permalink to this definition">¶</a></dt>
   <dd><p>Open an existing INI file</p>
   <p>&#64;param filename: Filename of INI file
   &#64;type filename: string</p>
   <p>&#64;raises RuntimeError: When the provided filename doesn&#8217;t exist</p>
   <p>&#64;returns: Opened INI file object
   &#64;rtype: jumpscale.inifile.IniFile.IniFile</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.inifile">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.inifile" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.inifile package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.inifile.IniFile">JumpScale.baselib.inifile.IniFile module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.inifile">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.influxdb.html"
                           title="previous chapter">JumpScale.baselib.influxdb package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.installtools.html"
                           title="next chapter">JumpScale.baselib.installtools package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.inifile.txt"
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
             <a href="JumpScale.baselib.installtools.html" title="JumpScale.baselib.installtools package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.influxdb.html" title="JumpScale.baselib.influxdb package"
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