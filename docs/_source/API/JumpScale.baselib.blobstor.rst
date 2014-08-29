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
   
       <title>JumpScale.baselib.blobstor package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.baselib.blobstor2 package" href="JumpScale.baselib.blobstor2.html" />
       <link rel="prev" title="JumpScale.baselib.bitbucket package" href="JumpScale.baselib.bitbucket.html" />
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
             <a href="JumpScale.baselib.blobstor2.html" title="JumpScale.baselib.blobstor2 package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.bitbucket.html" title="JumpScale.baselib.bitbucket package"
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
   
     <div class="section" id="jumpscale-baselib-blobstor-package">
   <h1>JumpScale.baselib.blobstor package<a class="headerlink" href="#jumpscale-baselib-blobstor-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.blobstor.BlobStor">
   <span id="jumpscale-baselib-blobstor-blobstor-module"></span><h2>JumpScale.baselib.blobstor.BlobStor module<a class="headerlink" href="#module-JumpScale.baselib.blobstor.BlobStor" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobMetadata">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.blobstor.BlobStor.</tt><tt class="descname">BlobMetadata</tt><big>(</big><em>content</em>, <em>hash</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobMetadata"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobMetadata" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.blobstor.BlobStor.</tt><tt class="descname">BlobStor</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor" title="Permalink to this definition">¶</a></dt>
   <dd><p>generic usable storage system for larger blobs =  a blob is e.g. a file or a directory (which is then compressed)</p>
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.checkIdentical">
   <tt class="descname">checkIdentical</tt><big>(</big><em>key</em>, <em>destination</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.checkIdentical"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.checkIdentical" title="Permalink to this definition">¶</a></dt>
   <dd><p>return True if destination is still same as on blobsystem
   else False</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.copyToOtherBlobStor">
   <tt class="descname">copyToOtherBlobStor</tt><big>(</big><em>key</em>, <em>blobstor</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.copyToOtherBlobStor"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.copyToOtherBlobStor" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.download">
   <tt class="descname">download</tt><big>(</big><em>key</em>, <em>destination</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.download" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.exists">
   <tt class="descname">exists</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks if the blobstor contains an entry for the given key</p>
   <p>&#64;param key: key to
   &#64;type key: string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.getMetadata">
   <tt class="descname">getMetadata</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.getMetadata"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.getMetadata" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.loadConfig">
   <tt class="descname">loadConfig</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.loadConfig"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.loadConfig" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStor.put">
   <tt class="descname">put</tt><big>(</big><em>path</em>, <em>type=''</em>, <em>expiration=0</em>, <em>tags=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStor.put"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStor.put" title="Permalink to this definition">¶</a></dt>
   <dd><p>put file or directory to blobstor
   &#64;param expiration in hours
   &#64;param type see: j.enumerators.BlobType....</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStorFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.blobstor.BlobStor.</tt><tt class="descname">BlobStorFactory</tt><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStorFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStorFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.get">
   <tt class="descname">get</tt><big>(</big><em>name=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStorFactory.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.log">
   <tt class="descname">log</tt><big>(</big><em>msg</em>, <em>category=''</em>, <em>level=5</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStorFactory.log"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.log" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.parse">
   <tt class="descname">parse</tt><big>(</big><em>path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobStorFactory.parse"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobStorFactory.parse" title="Permalink to this definition">¶</a></dt>
   <dd><p>Parse a blobstor description file</p>
   <p>&#64;param path: location of the description file
   &#64;type path: string
   &#64;return: parsed description
   &#64;rtype: BlobDescription</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobType">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.blobstor.BlobStor.</tt><tt class="descname">BlobType</tt><big>(</big><em>*args</em>, <em>**kwargs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStor.html#BlobType"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobType" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="JumpScale.core.baseclasses.html#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration" title="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration</span></tt></a></p>
   <p>Blob type</p>
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobType.JPACKAGE">
   <tt class="descname">JPACKAGE</tt><em class="property"> = jpackage</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobType.JPACKAGE" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobType.LOG">
   <tt class="descname">LOG</tt><em class="property"> = log</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobType.LOG" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStor.BlobType.VARIA">
   <tt class="descname">VARIA</tt><em class="property"> = varia</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStor.BlobType.VARIA" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.blobstor.BlobStorConfigManagement">
   <span id="jumpscale-baselib-blobstor-blobstorconfigmanagement-module"></span><h2>JumpScale.baselib.blobstor.BlobStorConfigManagement module<a class="headerlink" href="#module-JumpScale.baselib.blobstor.BlobStorConfigManagement" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.blobstor.BlobStorConfigManagement.</tt><tt class="descname">BlobStorConfigManagementItem</tt><big>(</big><em>configtype</em>, <em>itemname</em>, <em>params=None</em>, <em>load=True</em>, <em>partialadd=False</em>, <em>setDefaults=False</em>, <em>validate=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStorConfigManagement.html#BlobStorConfigManagementItem"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="JumpScale.core.config.html#JumpScale.core.config.IConfigBase.ConfigManagementItem" title="JumpScale.core.config.IConfigBase.ConfigManagementItem"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.config.IConfigBase.ConfigManagementItem</span></tt></a></p>
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.CONFIGTYPE">
   <tt class="descname">CONFIGTYPE</tt><em class="property"> = 'blobstor'</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.CONFIGTYPE" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.DESCRIPTION">
   <tt class="descname">DESCRIPTION</tt><em class="property"> = 'blobstor connection, key = name'</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.DESCRIPTION" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.KEYS">
   <tt class="descname">KEYS</tt><em class="property"> = {'ftp': '', 'namespace': 'j.', 'http': '', 'localpath': '', 'type': 'local'}</em><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.KEYS" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.ask">
   <tt class="descname">ask</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/blobstor/BlobStorConfigManagement.html#BlobStorConfigManagementItem.ask"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.blobstor.BlobStorConfigManagement.BlobStorConfigManagementItem.ask" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.blobstor">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.blobstor" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.blobstor package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.blobstor.BlobStor">JumpScale.baselib.blobstor.BlobStor module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.blobstor.BlobStorConfigManagement">JumpScale.baselib.blobstor.BlobStorConfigManagement module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.blobstor">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.bitbucket.html"
                           title="previous chapter">JumpScale.baselib.bitbucket package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.blobstor2.html"
                           title="next chapter">JumpScale.baselib.blobstor2 package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.blobstor.txt"
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
             <a href="JumpScale.baselib.blobstor2.html" title="JumpScale.baselib.blobstor2 package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.bitbucket.html" title="JumpScale.baselib.bitbucket package"
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
       <li><a href="../_sources/API/JumpScale.baselib.blobstor.txt"
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