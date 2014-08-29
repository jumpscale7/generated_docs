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
   
       <title>JumpScale.grid.osismodel package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="up" title="JumpScale.grid package" href="JumpScale.grid.html" />
       <link rel="next" title="JumpScale.grid.processmanager package" href="JumpScale.grid.processmanager.html" />
       <link rel="prev" title="JumpScale.grid.osis package" href="JumpScale.grid.osis.html" />
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
             <a href="JumpScale.grid.processmanager.html" title="JumpScale.grid.processmanager package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.grid.osis.html" title="JumpScale.grid.osis package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.grid.html" accesskey="U">JumpScale.grid package</a> &raquo;</li>
         </ul>
       </div>
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
   
     <div class="section" id="jumpscale-grid-osismodel-package">
   <h1>JumpScale.grid.osismodel package<a class="headerlink" href="#jumpscale-grid-osismodel-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.grid.osismodel.OSIS">
   <span id="jumpscale-grid-osismodel-osis-module"></span><h2>JumpScale.grid.osismodel.OSIS module<a class="headerlink" href="#module-JumpScale.grid.osismodel.OSIS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS">
   <em class="property">class </em><tt class="descclassname">JumpScale.grid.osismodel.OSIS.</tt><tt class="descname">OSIS</tt><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.destroy">
   <tt class="descname">destroy</tt><big>(</big><em>appname</em>, <em>actorname='*'</em>, <em>modelname='*'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.destroy"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.destroy" title="Permalink to this definition">¶</a></dt>
   <dd><p>destroy all objects &amp; indexes with mentioned names</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.get">
   <tt class="descname">get</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>modelClass=None</em>, <em>db=None</em>, <em>index=False</em>, <em>indexer=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.getNoDB">
   <tt class="descname">getNoDB</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>modelClass=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.getNoDB"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.getNoDB" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.getRemoteOsisDB">
   <tt class="descname">getRemoteOsisDB</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>modelClass=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.getRemoteOsisDB"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.getRemoteOsisDB" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.inputNormalizeList">
   <tt class="descname">inputNormalizeList</tt><big>(</big><em>param</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.inputNormalizeList"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.inputNormalizeList" title="Permalink to this definition">¶</a></dt>
   <dd><p>comma separated string becomes list
   list gets checked, if all int then returnformat=1
   list gets checked, if all str, then returnformat=2
   &#64;return (returnformat,list)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSIS.OSIS.rebuildindex">
   <tt class="descname">rebuildindex</tt><big>(</big><em>appname</em>, <em>actorname='*'</em>, <em>modelname='*'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSIS.html#OSIS.rebuildindex"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSIS.OSIS.rebuildindex" title="Permalink to this definition">¶</a></dt>
   <dd><p>destroy all objects &amp; indexes with mentioned names</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.grid.osismodel.OSISInstance">
   <span id="jumpscale-grid-osismodel-osisinstance-module"></span><h2>JumpScale.grid.osismodel.OSISInstance module<a class="headerlink" href="#module-JumpScale.grid.osismodel.OSISInstance" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance">
   <em class="property">class </em><tt class="descclassname">JumpScale.grid.osismodel.OSISInstance.</tt><tt class="descname">OSISInstance</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>classs</em>, <em>db</em>, <em>index=False</em>, <em>indexer=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB" title="JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.checkEqualNoId">
   <tt class="descname">checkEqualNoId</tt><big>(</big><em>obj1</em>, <em>obj2</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.checkEqualNoId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.checkEqualNoId" title="Permalink to this definition">¶</a></dt>
   <dd><p>convert obj1 &amp; 2 to dict and remove id &amp; guid
   check if all other fields are equal</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.delete">
   <tt class="descname">delete</tt><big>(</big><em>guid=None</em>, <em>id=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.delete"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.delete" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.destroy">
   <tt class="descname">destroy</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.destroy"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.destroy" title="Permalink to this definition">¶</a></dt>
   <dd><p>delete objects as well as index (all)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.destroyindex">
   <tt class="descname">destroyindex</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.destroyindex"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.destroyindex" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.exists">
   <tt class="descname">exists</tt><big>(</big><em>guid=None</em>, <em>id=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.exists" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.find">
   <tt class="descname">find</tt><big>(</big><em>query</em>, <em>start=0</em>, <em>size=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.find"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.find" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.get">
   <tt class="descname">get</tt><big>(</big><em>guid=None</em>, <em>id=None</em>, <em>createIfNeeded=False</em>, <em>ignoreError=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.getNrRecords">
   <tt class="descname">getNrRecords</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.getNrRecords"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.getNrRecords" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.getguid2id">
   <tt class="descname">getguid2id</tt><big>(</big><em>id=None</em>, <em>guid=None</em>, <em>ignoreError=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.getguid2id"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.getguid2id" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param guidCheck, if used will check that the guid returned is same as referenced by id</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.link">
   <tt class="descname">link</tt><big>(</big><em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.link"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.link" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.list">
   <tt class="descname">list</tt><big>(</big><em>withcontent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.list" title="Permalink to this definition">¶</a></dt>
   <dd><p>return all object id&#8217;s stored in DB</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.new">
   <tt class="descname">new</tt><big>(</big><em>guid=None</em>, <em>id=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.new"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.new" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create new object, generate id if needed, do not store !!!</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.obj2ini">
   <tt class="descname">obj2ini</tt><big>(</big><em>fields=</em>, <span class="optional">[</span><span class="optional">]</span><em>section='main'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.obj2ini"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.obj2ini" title="Permalink to this definition">¶</a></dt>
   <dd><p>convert osis object to an inifile, only properties of root are used</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.optimize">
   <tt class="descname">optimize</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.optimize"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.optimize" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.rebuildindex">
   <tt class="descname">rebuildindex</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.rebuildindex"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.rebuildindex" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstance.set">
   <tt class="descname">set</tt><big>(</big><em>obj</em>, <em>index=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstance.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstance.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB">
   <em class="property">class </em><tt class="descclassname">JumpScale.grid.osismodel.OSISInstance.</tt><tt class="descname">OSISInstanceNoDB</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>classs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstanceNoDB"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB.new">
   <tt class="descname">new</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISInstanceNoDB.new"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB.new" title="Permalink to this definition">¶</a></dt>
   <dd><p>Create new object from class &amp; return</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance">
   <em class="property">class </em><tt class="descclassname">JumpScale.grid.osismodel.OSISInstance.</tt><tt class="descname">OSISRemoteOSISInstance</tt><big>(</big><em>appname</em>, <em>actorname</em>, <em>modelname</em>, <em>classs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB" title="JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.grid.osismodel.OSISInstance.OSISInstanceNoDB</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.delete">
   <tt class="descname">delete</tt><big>(</big><em>guid=None</em>, <em>id=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance.delete"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.delete" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.find">
   <tt class="descname">find</tt><big>(</big><em>query</em>, <em>start=0</em>, <em>size=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance.find"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.find" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.get">
   <tt class="descname">get</tt><big>(</big><em>guid=None</em>, <em>id=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.list">
   <tt class="descname">list</tt><big>(</big><em>prefix=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.list" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.set">
   <tt class="descname">set</tt><big>(</big><em>obj</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/grid/osismodel/OSISInstance.html#OSISRemoteOSISInstance.set"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.grid.osismodel.OSISInstance.OSISRemoteOSISInstance.set" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.grid.osismodel">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.grid.osismodel" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.grid.osismodel package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.grid.osismodel.OSIS">JumpScale.grid.osismodel.OSIS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.grid.osismodel.OSISInstance">JumpScale.grid.osismodel.OSISInstance module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.grid.osismodel">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.grid.osis.html"
                           title="previous chapter">JumpScale.grid.osis package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.grid.processmanager.html"
                           title="next chapter">JumpScale.grid.processmanager package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.grid.osismodel.txt"
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
             <a href="JumpScale.grid.processmanager.html" title="JumpScale.grid.processmanager package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.grid.osis.html" title="JumpScale.grid.osis package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.grid.html" >JumpScale.grid package</a> &raquo;</li>
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
       <li><a href="../_sources/API/JumpScale.grid.osismodel.txt"
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