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
           <li class="right" >
             <a href="../py-modindex.html" title="Python Module Index"
                >modules</a> |</li>
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
   
       <title>JumpScale.core.pmtypes package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="up" title="JumpScale.core package" href="JumpScale.core.html" />
       <link rel="next" title="JumpScale.core.properties package" href="JumpScale.core.properties.html" />
       <link rel="prev" title="JumpScale.core.logging.logtargets package" href="JumpScale.core.logging.logtargets.html" />
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
             <a href="JumpScale.core.properties.html" title="JumpScale.core.properties package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.logging.logtargets.html" title="JumpScale.core.logging.logtargets package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" accesskey="U">JumpScale.core package</a> &raquo;</li>
         </ul>
       </div>
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
   
     <div class="section" id="jumpscale-core-pmtypes-package">
   <h1>JumpScale.core.pmtypes package<a class="headerlink" href="#jumpscale-core-pmtypes-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.CollectionTypes">
   <span id="jumpscale-core-pmtypes-collectiontypes-module"></span><h2>JumpScale.core.pmtypes.CollectionTypes module<a class="headerlink" href="#module-JumpScale.core.pmtypes.CollectionTypes" title="Permalink to this headline">¶</a></h2>
   <p>Definition of several collection types (list, dict, set,...)</p>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Dictionary">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CollectionTypes.</tt><tt class="descname">Dictionary</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#Dictionary"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Dictionary" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic dictionary type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Dictionary.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'dictionary'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Dictionary.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Dictionary.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#Dictionary.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Dictionary.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a dict</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Dictionary.get_default">
   <tt class="descname">get_default</tt><big>(</big><em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#Dictionary.get_default"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Dictionary.get_default" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.List">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CollectionTypes.</tt><tt class="descname">List</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#List"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.List" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic list type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.List.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'list'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.List.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.List.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#List.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.List.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a list</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.List.get_default">
   <tt class="descname">get_default</tt><big>(</big><em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#List.get_default"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.List.get_default" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Set">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CollectionTypes.</tt><tt class="descname">Set</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#Set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Set" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic set type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Set.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'set'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Set.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CollectionTypes.Set.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CollectionTypes.html#Set.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CollectionTypes.Set.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a set</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.CustomTypes">
   <span id="jumpscale-core-pmtypes-customtypes-module"></span><h2>JumpScale.core.pmtypes.CustomTypes module<a class="headerlink" href="#module-JumpScale.core.pmtypes.CustomTypes" title="Permalink to this headline">¶</a></h2>
   <p>Definition of several custom types (paths, ipaddress, guid,...)</p>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.DirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">DirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#DirPath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.DirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.Path" title="JumpScale.core.pmtypes.CustomTypes.Path"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.Path</span></tt></a></p>
   <p>Generic folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.DirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'dirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.DirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.DirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#DirPath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.DirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid directory path</p>
   <p>This checks whether value is a valid Path only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Duration">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">Duration</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Duration"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Duration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Duration type</p>
   <p>Can be assigned a string or a number. Will always be read as a number.</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Duration.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'duration'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Duration.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Duration.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Duration.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Duration.check" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.FilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">FilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#FilePath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.FilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.Path" title="JumpScale.core.pmtypes.CustomTypes.Path"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.Path</span></tt></a></p>
   <p>Generic file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.FilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'filepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.FilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.FilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#FilePath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.FilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid file path</p>
   <p>This checks whether value is a valid Path only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Guid">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">Guid</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Guid"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Guid" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="JumpScale.core.pmtypes.PrimitiveTypes.String"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.PrimitiveTypes.String</span></tt></a></p>
   <p>Generic GUID type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Guid.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'guid'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Guid.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Guid.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Guid.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Guid.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid GUID string</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPAddress">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">IPAddress</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPAddress"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPAddress" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="JumpScale.core.pmtypes.PrimitiveTypes.String"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.PrimitiveTypes.String</span></tt></a></p>
   <p>Generic IPv4 address type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPAddress.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'ipaddress'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPAddress.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPAddress.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPAddress.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPAddress.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid IPv4 address</p>
   <p>&#64;param value: IP address to check
   &#64;type value: string</p>
   <p>&#64;returns: Whether the provided value is a valid IPv4 address
   &#64;rtype: bool</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPPort">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">IPPort</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPPort"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPPort" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic IP port type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPPort.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'ipport'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPPort.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPPort.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPPort.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPPort.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check if the value is a valid port
   We just check if the value a single port or a range
   Values must be between 0 and 65535</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">IPv4AddressRange</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPv4AddressRange"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic IPv4 address range type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'ipaddressrange'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#IPv4AddressRange.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.IPv4AddressRange.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check if the value is a valid IPv4AddressRange
   We just check if the value is a instance of a IPv4Range</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Path">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">Path</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Path"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Path" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="JumpScale.core.pmtypes.PrimitiveTypes.String"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.PrimitiveTypes.String</span></tt></a></p>
   <p>Generic path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Path.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'path'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Path.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.Path.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#Path.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.Path.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid path</p>
   <p>This checks whether value is a valid string only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixDirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">UnixDirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#UnixDirPath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixDirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.DirPath" title="JumpScale.core.pmtypes.CustomTypes.DirPath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.DirPath</span></tt></a></p>
   <p>Generic Unix folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixDirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'unixdirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixDirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixDirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#UnixDirPath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixDirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid UNIX directory path</p>
   <p>This checks whether value is a valid DirPath which starts and stops
   with &#8216;/&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixFilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">UnixFilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#UnixFilePath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixFilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.FilePath" title="JumpScale.core.pmtypes.CustomTypes.FilePath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.FilePath</span></tt></a></p>
   <p>Generic Unix file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixFilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'unixfilepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixFilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.UnixFilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#UnixFilePath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.UnixFilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid UNIX file path</p>
   <p>This checks whether value is a valid FilePath which starts with &#8216;/&#8217; and
   does not end with &#8216;/&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsDirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">WindowsDirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#WindowsDirPath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsDirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.DirPath" title="JumpScale.core.pmtypes.CustomTypes.DirPath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.DirPath</span></tt></a></p>
   <p>Generic Windows folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsDirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'windowsdirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsDirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsDirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#WindowsDirPath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsDirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid Windows directory path</p>
   <p>This checks whether value is a valid DirPath which starts with &#8216;/&#8217; or
   &#8216;&#8217;, optionally prepended with a drive name, and ends with &#8216;/&#8217; or
   &#8216;&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsFilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.CustomTypes.</tt><tt class="descname">WindowsFilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#WindowsFilePath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsFilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.FilePath" title="JumpScale.core.pmtypes.CustomTypes.FilePath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.FilePath</span></tt></a></p>
   <p>Generic Windows file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsFilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'windowsfilepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsFilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.CustomTypes.WindowsFilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/CustomTypes.html#WindowsFilePath.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.CustomTypes.WindowsFilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid Windows file path</p>
   <p>This checks whether value is a valid FilePath which starts with &#8216;/&#8217; or
   &#8216;&#8217;, optionally prepended with a drive name, and not ends with &#8216;/&#8217; or
   &#8216;&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.GenericTypes">
   <span id="jumpscale-core-pmtypes-generictypes-module"></span><h2>JumpScale.core.pmtypes.GenericTypes module<a class="headerlink" href="#module-JumpScale.core.pmtypes.GenericTypes" title="Permalink to this headline">¶</a></h2>
   <p>Some jumpscale descriptor types acting as generics</p>
   <p>The types defined in this module are no real descriptors, it are functions
   which generate descriptor types on-the-fly. The end-user syntax remains
   the same:</p>
   <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">MyType</span><span class="p">:</span> <span class="k">pass</span>
   <span class="gp">...</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">JumpScale.core.baseclasses</span> <span class="kn">import</span> <span class="n">BaseType</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">(</span><span class="n">BaseType</span><span class="p">):</span>
   <span class="gp">... </span>    <span class="n">mt</span> <span class="o">=</span> <span class="n">j</span><span class="o">.</span><span class="n">basetype</span><span class="o">.</span><span class="n">object</span><span class="p">(</span><span class="n">MyType</span><span class="p">)</span>
   <span class="gp">...</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="n">instance</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">instance</span><span class="o">.</span><span class="n">mt</span>
   <span class="go">None</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="n">instance</span><span class="o">.</span><span class="n">mt</span> <span class="o">=</span> <span class="n">MyType</span><span class="p">()</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="n">instance</span><span class="o">.</span><span class="n">mt</span> <span class="o">=</span> <span class="s">&#39;String is no MyType&#39;</span>
   <span class="go">------------------------------------------------------------</span>
   <span class="gt">Traceback (most recent call last):</span>
       <span class="o">...</span>
   <span class="gr">&lt;type &#39;exceptions.ValueError&#39;&gt;</span>: <span class="n">mt property of MyClass should be a valid MyTypeType, &#39;String is no MyType&#39; is not</span>
   </pre></div>
   </div>
   <dl class="function">
   <dt id="JumpScale.core.pmtypes.GenericTypes.Enumeration">
   <tt class="descclassname">JumpScale.core.pmtypes.GenericTypes.</tt><tt class="descname">Enumeration</tt><big>(</big><em>enumerationtype</em>, <em>**kwargs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/GenericTypes.html#Enumeration"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.GenericTypes.Enumeration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generic descriptor generator for custom enumeration types</p>
   <p>You should be aware this is, unlike non-generic basetypes, a function
   generating a class instance, not a class.</p>
   <p>&#64;param enumerationtype: Type of which values should be instances
   &#64;type enumerationtype: Subclass of L{jumpscale.baseclasses.BaseEnumeration.BaseEnumeration}
   &#64;param kwargs: Kwargs sent to L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;returns: An instance of a custom descriptor class
   &#64;rtype: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;see: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.pmtypes.GenericTypes.Object">
   <tt class="descclassname">JumpScale.core.pmtypes.GenericTypes.</tt><tt class="descname">Object</tt><big>(</big><em>type_</em>, <em>**kwargs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/GenericTypes.html#Object"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.GenericTypes.Object" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generic descriptor generator for custom object types</p>
   <p>You should be aware this is, unlike non-generic basetypes, a function
   generating a class instance, not a class.</p>
   <p>&#64;param <a href="#id1"><span class="problematic" id="id2">type_</span></a>: Type of which values should be instances
   &#64;type <a href="#id3"><span class="problematic" id="id4">type_</span></a>: class or type
   &#64;param kwargs: Kwargs sent to L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;returns: An instance of a custom descriptor class
   &#64;rtype: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;see: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.IPAddress">
   <span id="jumpscale-core-pmtypes-ipaddress-module"></span><h2>JumpScale.core.pmtypes.IPAddress module<a class="headerlink" href="#module-JumpScale.core.pmtypes.IPAddress" title="Permalink to this headline">¶</a></h2>
   <p>IP address and related classes</p>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.IPAddress.IPv4Address">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.IPAddress.</tt><tt class="descname">IPv4Address</tt><big>(</big><em>ip</em>, <em>netmask=None</em>, <em>gateway=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/IPAddress.html#IPv4Address"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.IPAddress.IPv4Address" title="Permalink to this definition">¶</a></dt>
   <dd><p>Representation of a standard IPv4 address</p>
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.IPAddress.IPv4Address.fromCIDR">
   <em class="property">classmethod </em><tt class="descname">fromCIDR</tt><big>(</big><em>cidrAddress</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/IPAddress.html#IPv4Address.fromCIDR"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.IPAddress.IPv4Address.fromCIDR" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create an IPv4Address instance from a CIDR address like
   &#8216;192.168.2.253/16&#8217;</p>
   <p>&#64;param cidrAddress: CIDR address
   &#64;type cidrAddress: string
   &#64;return: IP address with the correct IP and netmask
   &#64;rtype: IPv4Address</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.IPAddress.IPv4Range">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.IPAddress.</tt><tt class="descname">IPv4Range</tt><big>(</big><em>fromIp=None</em>, <em>toIp=None</em>, <em>netIp=None</em>, <em>netMask=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/IPAddress.html#IPv4Range"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.IPAddress.IPv4Range" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.IPAddress.IPv4Range.convertNetmask">
   <em class="property">static </em><tt class="descname">convertNetmask</tt><big>(</big><em>netmask</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/IPAddress.html#IPv4Range.convertNetmask"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.IPAddress.IPv4Range.convertNetmask" title="Permalink to this definition">¶</a></dt>
   <dd><p>Convert a netmask to it&#8217;s integer representation</p>
   <p>This can convert (eg) 255.255.255.0 to 24.</p>
   <p>&#64;param netmask: Netmask to convert
   &#64;type netmask: IPv4Address or string or int</p>
   <p>&#64;returns: Integer representation of the netmask
   &#64;rtype: number</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.IPAddress.IPv4Range.fromCIDR">
   <em class="property">classmethod </em><tt class="descname">fromCIDR</tt><big>(</big><em>cidrAddress</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/IPAddress.html#IPv4Range.fromCIDR"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.IPAddress.IPv4Range.fromCIDR" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create an IPv4Range instance from a CIDR address like
   &#8216;192.168.2.253/16&#8217;</p>
   <p>&#64;param cidrAddress: CIDR address
   &#64;type cidrAddress: string
   &#64;return: IP range with the correct fromIPP and toIP
   &#64;rtype: IPv4Range</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.PrimitiveTypes">
   <span id="jumpscale-core-pmtypes-primitivetypes-module"></span><h2>JumpScale.core.pmtypes.PrimitiveTypes module<a class="headerlink" href="#module-JumpScale.core.pmtypes.PrimitiveTypes" title="Permalink to this headline">¶</a></h2>
   <p>Definition of several primitive type properties (integer, string,...)</p>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.PrimitiveTypes.</tt><tt class="descname">Boolean</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Boolean"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic boolean type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'boolean'</em><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Boolean.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a boolean</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Boolean.checkString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean.fromString">
   <em class="property">static </em><tt class="descname">fromString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Boolean.fromString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean.fromString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Boolean.toString">
   <em class="property">static </em><tt class="descname">toString</tt><big>(</big><em>boolean</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Boolean.toString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Boolean.toString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Float">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.PrimitiveTypes.</tt><tt class="descname">Float</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Float"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Float" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic float type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Float.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'float'</em><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Float.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Float.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Float.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Float.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a float</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Float.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Float.checkString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Float.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Integer">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.PrimitiveTypes.</tt><tt class="descname">Integer</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Integer"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Integer" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic integer type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Integer.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'integer'</em><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Integer.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Integer.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Integer.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Integer.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is an integer</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.Integer.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#Integer.checkString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.Integer.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.String">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.PrimitiveTypes.</tt><tt class="descname">String</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#String"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic string type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.String.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'string'</em><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.String.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.String.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#String.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.String.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a string</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.String.fromString">
   <em class="property">static </em><tt class="descname">fromString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#String.fromString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.String.fromString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.PrimitiveTypes.String.toString">
   <em class="property">static </em><tt class="descname">toString</tt><big>(</big><em>v</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/PrimitiveTypes.html#String.toString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.PrimitiveTypes.String.toString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes.base">
   <span id="jumpscale-core-pmtypes-base-module"></span><h2>JumpScale.core.pmtypes.base module<a class="headerlink" href="#module-JumpScale.core.pmtypes.base" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.base.BaseType">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.base.</tt><tt class="descname">BaseType</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/base.html#BaseType"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Base class for all defined types</p>
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.base.BaseType.checkString">
   <em class="property">classmethod </em><tt class="descname">checkString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/base.html#BaseType.checkString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.base.BaseType.constructor_args">
   <tt class="descname">constructor_args</tt><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType.constructor_args" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.base.BaseType.fromString">
   <em class="property">classmethod </em><tt class="descname">fromString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/base.html#BaseType.fromString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType.fromString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.pmtypes.base.BaseType.get_default">
   <tt class="descname">get_default</tt><big>(</big><em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/base.html#BaseType.get_default"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType.get_default" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get default value for descriptor attribute</p>
   <p>&#64;returns: Default value
   &#64;rtype: object</p>
   <p>&#64;raises RuntimeError: If the (generated or constant) default value is not valid for this type</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.base.BaseType.toString">
   <em class="property">classmethod </em><tt class="descname">toString</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/pmtypes/base.html#BaseType.toString"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.pmtypes.base.BaseType.toString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.pmtypes">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.core.pmtypes" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.IPv4Address">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">IPv4Address</tt><big>(</big><em>ip</em>, <em>netmask=None</em>, <em>gateway=None</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.IPv4Address" title="Permalink to this definition">¶</a></dt>
   <dd><p>Representation of a standard IPv4 address</p>
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.IPv4Address.fromCIDR">
   <em class="property">classmethod </em><tt class="descname">fromCIDR</tt><big>(</big><em>cidrAddress</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.IPv4Address.fromCIDR" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create an IPv4Address instance from a CIDR address like
   &#8216;192.168.2.253/16&#8217;</p>
   <p>&#64;param cidrAddress: CIDR address
   &#64;type cidrAddress: string
   &#64;return: IP address with the correct IP and netmask
   &#64;rtype: IPv4Address</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.IPv4Range">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">IPv4Range</tt><big>(</big><em>fromIp=None</em>, <em>toIp=None</em>, <em>netIp=None</em>, <em>netMask=None</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.IPv4Range" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.IPv4Range.convertNetmask">
   <em class="property">static </em><tt class="descname">convertNetmask</tt><big>(</big><em>netmask</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.IPv4Range.convertNetmask" title="Permalink to this definition">¶</a></dt>
   <dd><p>Convert a netmask to it&#8217;s integer representation</p>
   <p>This can convert (eg) 255.255.255.0 to 24.</p>
   <p>&#64;param netmask: Netmask to convert
   &#64;type netmask: IPv4Address or string or int</p>
   <p>&#64;returns: Integer representation of the netmask
   &#64;rtype: number</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.pmtypes.IPv4Range.fromCIDR">
   <em class="property">classmethod </em><tt class="descname">fromCIDR</tt><big>(</big><em>cidrAddress</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.IPv4Range.fromCIDR" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create an IPv4Range instance from a CIDR address like
   &#8216;192.168.2.253/16&#8217;</p>
   <p>&#64;param cidrAddress: CIDR address
   &#64;type cidrAddress: string
   &#64;return: IP range with the correct fromIPP and toIP
   &#64;rtype: IPv4Range</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Boolean">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Boolean</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic boolean type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Boolean.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'boolean'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Boolean.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a boolean</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Boolean.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>s</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Boolean.fromString">
   <em class="property">static </em><tt class="descname">fromString</tt><big>(</big><em>s</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean.fromString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Boolean.toString">
   <em class="property">static </em><tt class="descname">toString</tt><big>(</big><em>boolean</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Boolean.toString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Integer">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Integer</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Integer" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic integer type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Integer.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'integer'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Integer.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Integer.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Integer.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is an integer</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Integer.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>s</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Integer.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Float">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Float</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Float" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic float type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Float.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'float'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Float.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Float.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Float.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a float</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Float.checkString">
   <em class="property">static </em><tt class="descname">checkString</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Float.checkString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.String">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">String</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.String" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic string type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.String.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'string'</em><a class="headerlink" href="#JumpScale.core.pmtypes.String.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.String.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.String.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a string</p>
   </dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.String.fromString">
   <em class="property">static </em><tt class="descname">fromString</tt><big>(</big><em>s</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.String.fromString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.String.toString">
   <em class="property">static </em><tt class="descname">toString</tt><big>(</big><em>v</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.String.toString" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.List">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">List</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.List" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic list type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.List.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'list'</em><a class="headerlink" href="#JumpScale.core.pmtypes.List.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.List.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.List.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a list</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.pmtypes.List.get_default">
   <tt class="descname">get_default</tt><big>(</big><em>obj</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.List.get_default" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Set">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Set</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Set" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic set type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Set.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'set'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Set.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Set.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Set.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a set</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Dictionary">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Dictionary</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Dictionary" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.base.BaseType" title="JumpScale.core.pmtypes.base.BaseType"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.base.BaseType</span></tt></a></p>
   <p>Generic dictionary type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Dictionary.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'dictionary'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Dictionary.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Dictionary.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Dictionary.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a dict</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.pmtypes.Dictionary.get_default">
   <tt class="descname">get_default</tt><big>(</big><em>obj</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Dictionary.get_default" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Guid">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Guid</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Guid" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="JumpScale.core.pmtypes.PrimitiveTypes.String"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.PrimitiveTypes.String</span></tt></a></p>
   <p>Generic GUID type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Guid.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'guid'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Guid.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Guid.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Guid.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid GUID string</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.Path">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Path</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Path" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.PrimitiveTypes.String" title="JumpScale.core.pmtypes.PrimitiveTypes.String"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.PrimitiveTypes.String</span></tt></a></p>
   <p>Generic path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.Path.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'path'</em><a class="headerlink" href="#JumpScale.core.pmtypes.Path.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.Path.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Path.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid path</p>
   <p>This checks whether value is a valid string only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.DirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">DirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.DirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.Path" title="JumpScale.core.pmtypes.CustomTypes.Path"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.Path</span></tt></a></p>
   <p>Generic folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.DirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'dirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.DirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.DirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.DirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid directory path</p>
   <p>This checks whether value is a valid Path only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.FilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">FilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.FilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.Path" title="JumpScale.core.pmtypes.CustomTypes.Path"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.Path</span></tt></a></p>
   <p>Generic file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.FilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'filepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.FilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.FilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.FilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid file path</p>
   <p>This checks whether value is a valid Path only.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.UnixDirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">UnixDirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.UnixDirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.DirPath" title="JumpScale.core.pmtypes.CustomTypes.DirPath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.DirPath</span></tt></a></p>
   <p>Generic Unix folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.UnixDirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'unixdirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.UnixDirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.UnixDirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.UnixDirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid UNIX directory path</p>
   <p>This checks whether value is a valid DirPath which starts and stops
   with &#8216;/&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.UnixFilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">UnixFilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.UnixFilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.FilePath" title="JumpScale.core.pmtypes.CustomTypes.FilePath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.FilePath</span></tt></a></p>
   <p>Generic Unix file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.UnixFilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'unixfilepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.UnixFilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.UnixFilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.UnixFilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid UNIX file path</p>
   <p>This checks whether value is a valid FilePath which starts with &#8216;/&#8217; and
   does not end with &#8216;/&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.WindowsDirPath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">WindowsDirPath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsDirPath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.DirPath" title="JumpScale.core.pmtypes.CustomTypes.DirPath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.DirPath</span></tt></a></p>
   <p>Generic Windows folder path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.WindowsDirPath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'windowsdirpath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsDirPath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.WindowsDirPath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsDirPath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid Windows directory path</p>
   <p>This checks whether value is a valid DirPath which starts with &#8216;/&#8217; or
   &#8216;&#8217;, optionally prepended with a drive name, and ends with &#8216;/&#8217; or
   &#8216;&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.pmtypes.WindowsFilePath">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">WindowsFilePath</tt><big>(</big><em>default=&lt;object object at 0x2adfbac58fb0&gt;</em>, <em>check=None</em>, <em>doc=None</em>, <em>allow_none=False</em>, <em>flag_dirty=False</em>, <em>fset=None</em>, <em>readonly=False</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsFilePath" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.pmtypes.CustomTypes.FilePath" title="JumpScale.core.pmtypes.CustomTypes.FilePath"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.pmtypes.CustomTypes.FilePath</span></tt></a></p>
   <p>Generic Windows file path type</p>
   <dl class="attribute">
   <dt id="JumpScale.core.pmtypes.WindowsFilePath.NAME">
   <tt class="descname">NAME</tt><em class="property"> = 'windowsfilepath'</em><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsFilePath.NAME" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.core.pmtypes.WindowsFilePath.check">
   <em class="property">static </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.WindowsFilePath.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether provided value is a valid Windows file path</p>
   <p>This checks whether value is a valid FilePath which starts with &#8216;/&#8217; or
   &#8216;&#8217;, optionally prepended with a drive name, and not ends with &#8216;/&#8217; or
   &#8216;&#8217;.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.pmtypes.Object">
   <tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Object</tt><big>(</big><em>type_</em>, <em>**kwargs</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Object" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generic descriptor generator for custom object types</p>
   <p>You should be aware this is, unlike non-generic basetypes, a function
   generating a class instance, not a class.</p>
   <p>&#64;param <a href="#id5"><span class="problematic" id="id6">type_</span></a>: Type of which values should be instances
   &#64;type <a href="#id7"><span class="problematic" id="id8">type_</span></a>: class or type
   &#64;param kwargs: Kwargs sent to L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;returns: An instance of a custom descriptor class
   &#64;rtype: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;see: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.pmtypes.Enumeration">
   <tt class="descclassname">JumpScale.core.pmtypes.</tt><tt class="descname">Enumeration</tt><big>(</big><em>enumerationtype</em>, <em>**kwargs</em><big>)</big><a class="headerlink" href="#JumpScale.core.pmtypes.Enumeration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generic descriptor generator for custom enumeration types</p>
   <p>You should be aware this is, unlike non-generic basetypes, a function
   generating a class instance, not a class.</p>
   <p>&#64;param enumerationtype: Type of which values should be instances
   &#64;type enumerationtype: Subclass of L{jumpscale.baseclasses.BaseEnumeration.BaseEnumeration}
   &#64;param kwargs: Kwargs sent to L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;returns: An instance of a custom descriptor class
   &#64;rtype: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   <p>&#64;see: L{jumpscale.pmtypes.base.BaseType.__init__}</p>
   </dd></dl>
   
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.core.pmtypes package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.CollectionTypes">JumpScale.core.pmtypes.CollectionTypes module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.CustomTypes">JumpScale.core.pmtypes.CustomTypes module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.GenericTypes">JumpScale.core.pmtypes.GenericTypes module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.IPAddress">JumpScale.core.pmtypes.IPAddress module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.PrimitiveTypes">JumpScale.core.pmtypes.PrimitiveTypes module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes.base">JumpScale.core.pmtypes.base module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.pmtypes">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.core.logging.logtargets.html"
                           title="previous chapter">JumpScale.core.logging.logtargets package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.core.properties.html"
                           title="next chapter">JumpScale.core.properties package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.core.pmtypes.txt"
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
             <a href="JumpScale.core.properties.html" title="JumpScale.core.properties package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.logging.logtargets.html" title="JumpScale.core.logging.logtargets package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.core.html" >JumpScale.core package</a> &raquo;</li>
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
       <li><a href="../_sources/API/JumpScale.core.pmtypes.txt"
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
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>