.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.portal.docpreprocessor package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="up" title="JumpScale.portal package" href="JumpScale.portal.html" />
       <link rel="next" title="JumpScale.portal.html package" href="JumpScale.portal.html.html" />
       <link rel="prev" title="JumpScale.portal.docgenerator package" href="JumpScale.portal.docgenerator.html" /> 
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
             <a href="JumpScale.portal.html.html" title="JumpScale.portal.html package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.portal.docgenerator.html" title="JumpScale.portal.docgenerator package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.portal.html" accesskey="U">JumpScale.portal package</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <div class="section" id="jumpscale-portal-docpreprocessor-package">
   <h1>JumpScale.portal.docpreprocessor package<a class="headerlink" href="#jumpscale-portal-docpreprocessor-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.portal.docpreprocessor.DocParser">
   <span id="jumpscale-portal-docpreprocessor-docparser-module"></span><h2>JumpScale.portal.docpreprocessor.DocParser module<a class="headerlink" href="#module-JumpScale.portal.docpreprocessor.DocParser" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.docpreprocessor.DocParser.DocParser">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.docpreprocessor.DocParser.</tt><tt class="descname">DocParser</tt><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocParser.html#DocParser"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocParser.DocParser" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocParser.DocParser.addUniqueId">
   <tt class="descname">addUniqueId</tt><big>(</big><em>line</em>, <em>fullPath</em>, <em>ttype='sprint'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocParser.html#DocParser.addUniqueId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocParser.DocParser.addUniqueId" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocParser.DocParser.errorTrap">
   <tt class="descname">errorTrap</tt><big>(</big><em>msg</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocParser.html#DocParser.errorTrap"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocParser.DocParser.errorTrap" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocParser.DocParser.parseDoc">
   <tt class="descname">parseDoc</tt><big>(</big><em>doc</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocParser.html#DocParser.parseDoc"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocParser.DocParser.parseDoc" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocParser.DocParser.shortenDescr">
   <tt class="descname">shortenDescr</tt><big>(</big><em>text</em>, <em>maxnrchars=60</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocParser.html#DocParser.shortenDescr"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocParser.DocParser.shortenDescr" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.docpreprocessor.DocPreprocessor">
   <span id="jumpscale-portal-docpreprocessor-docpreprocessor-module"></span><h2>JumpScale.portal.docpreprocessor.DocPreprocessor module<a class="headerlink" href="#module-JumpScale.portal.docpreprocessor.DocPreprocessor" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.docpreprocessor.DocPreprocessor.</tt><tt class="descname">Doc</tt><big>(</big><em>docpreprocessor</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.applyParams">
   <tt class="descname">applyParams</tt><big>(</big><em>params</em>, <em>findfresh=False</em>, <em>content=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.applyParams"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.applyParams" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param params is dict with as key the name (lowercase)</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.applyTemplate">
   <tt class="descname">applyTemplate</tt><big>(</big><em>params</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.applyTemplate"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.applyTemplate" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.checkVisible">
   <tt class="descname">checkVisible</tt><big>(</big><em>visibility</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.checkVisible"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.checkVisible" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.clean">
   <tt class="descname">clean</tt><big>(</big><em>startHeading=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.clean"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.clean" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.copy">
   <tt class="descname">copy</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.copy"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.copy" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.executeMacrosDynamicWiki">
   <tt class="descname">executeMacrosDynamicWiki</tt><big>(</big><em>paramsExtra={}</em>, <em>ctx=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.executeMacrosDynamicWiki"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.executeMacrosDynamicWiki" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.executeMacrosPreprocess">
   <tt class="descname">executeMacrosPreprocess</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.executeMacrosPreprocess"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.executeMacrosPreprocess" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.findParams">
   <tt class="descname">findParams</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.findParams"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.findParams" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.fixMinHeadingLevel">
   <tt class="descname">fixMinHeadingLevel</tt><big>(</big><em>minLevel</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.fixMinHeadingLevel"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.fixMinHeadingLevel" title="Permalink to this definition">¶</a></dt>
   <dd><p>make sure min heading level is followed</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.generate2disk">
   <tt class="descname">generate2disk</tt><big>(</big><em>outpath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.generate2disk"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.generate2disk" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getHtmlBody">
   <tt class="descname">getHtmlBody</tt><big>(</big><em>paramsExtra={}</em>, <em>ctx=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.getHtmlBody"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getHtmlBody" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getPageKey">
   <tt class="descname">getPageKey</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.getPageKey"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getPageKey" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getSpaceName">
   <tt class="descname">getSpaceName</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.getSpaceName"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.getSpaceName" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.loadFromDisk">
   <tt class="descname">loadFromDisk</tt><big>(</big><em>preprocess=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.loadFromDisk"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.loadFromDisk" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.loadFromSource">
   <tt class="descname">loadFromSource</tt><big>(</big><em>preprocess=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.loadFromSource"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.loadFromSource" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.preprocess">
   <tt class="descname">preprocess</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#Doc.preprocess"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.Doc.preprocess" title="Permalink to this definition">¶</a></dt>
   <dd><p>make sure format is confluence
   execute macro&#8217;s
   fix min heading level
   clean format in preprocessing</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.docpreprocessor.DocPreprocessor.</tt><tt class="descname">DocPreprocessor</tt><big>(</big><em>contentDirs=</em>, <span class="optional">[</span><span class="optional">]</span><em>varsPath=''</em>, <em>spacename=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docAdd">
   <tt class="descname">docAdd</tt><big>(</big><em>doc</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.docAdd"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docAdd" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docExists">
   <tt class="descname">docExists</tt><big>(</big><em>docname</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.docExists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docExists" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docGet">
   <tt class="descname">docGet</tt><big>(</big><em>docname</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.docGet"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docGet" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docNew">
   <tt class="descname">docNew</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.docNew"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.docNew" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.findChildren">
   <tt class="descname">findChildren</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.findChildren"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.findChildren" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.findDocs">
   <tt class="descname">findDocs</tt><big>(</big><em>types=</em>, <span class="optional">[</span><span class="optional">]</span><em>products=</em>, <span class="optional">[</span><span class="optional">]</span><em>nameFilter=None</em>, <em>parent=None</em>, <em>filterTagsLabels=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.findDocs"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.findDocs" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.parseHtmlDoc">
   <tt class="descname">parseHtmlDoc</tt><big>(</big><em>path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.parseHtmlDoc"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.parseHtmlDoc" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.scan">
   <tt class="descname">scan</tt><big>(</big><em>path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#DocPreprocessor.scan"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.DocPreprocessor.scan" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.docpreprocessor.DocPreprocessor.</tt><tt class="descname">HeaderTools</tt><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#HeaderTools"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="staticmethod">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools.findLowestHeading">
   <em class="property">static </em><tt class="descname">findLowestHeading</tt><big>(</big><em>content</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#HeaderTools.findLowestHeading"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools.findLowestHeading" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="staticmethod">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools.getHeadnr">
   <em class="property">static </em><tt class="descname">getHeadnr</tt><big>(</big><em>line</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessor.html#HeaderTools.getHeadnr"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessor.HeaderTools.getHeadnr" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.docpreprocessor.DocPreprocessorFactory">
   <span id="jumpscale-portal-docpreprocessor-docpreprocessorfactory-module"></span><h2>JumpScale.portal.docpreprocessor.DocPreprocessorFactory module<a class="headerlink" href="#module-JumpScale.portal.docpreprocessor.DocPreprocessorFactory" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.docpreprocessor.DocPreprocessorFactory.</tt><tt class="descname">DocPreprocessorFactory</tt><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessorFactory.html#DocPreprocessorFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.generate">
   <tt class="descname">generate</tt><big>(</big><em>preprocessorobject</em>, <em>outpath='out'</em>, <em>startDoc='Home'</em>, <em>visibility=</em>, <span class="optional">[</span><span class="optional">]</span><em>reset=True</em>, <em>outputdocname=''</em>, <em>format='preprocess'</em>, <em>deepcopy=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessorFactory.html#DocPreprocessorFactory.generate"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.generate" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.generateFromDir">
   <tt class="descname">generateFromDir</tt><big>(</big><em>path</em>, <em>macrosPaths=</em>, <span class="optional">[</span><span class="optional">]</span><em>visibility=</em>, <span class="optional">[</span><span class="optional">]</span><em>cacheDir=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessorFactory.html#DocPreprocessorFactory.generateFromDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.generateFromDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param path is starting point, will look for generate.cfg &amp; params.cfg in this dir, input in these files will determine how preprocessor will work
   &#64;param macrosPaths are dirs where macro&#8217;s are they are in form of tasklets
   &#64;param cacheDir if non std caching dir override here</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.get">
   <tt class="descname">get</tt><big>(</big><em>contentDirs=</em>, <span class="optional">[</span><span class="optional">]</span><em>varsPath=''</em>, <em>spacename=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessorFactory.html#DocPreprocessorFactory.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.get" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param contentDirs are the dirs where we will load wiki files from &amp; parse</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.getMacroPath">
   <tt class="descname">getMacroPath</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/docpreprocessor/DocPreprocessorFactory.html#DocPreprocessorFactory.getMacroPath"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.docpreprocessor.DocPreprocessorFactory.DocPreprocessorFactory.getMacroPath" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.docpreprocessor">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.portal.docpreprocessor" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.portal.docpreprocessor package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.docpreprocessor.DocParser">JumpScale.portal.docpreprocessor.DocParser module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.docpreprocessor.DocPreprocessor">JumpScale.portal.docpreprocessor.DocPreprocessor module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.docpreprocessor.DocPreprocessorFactory">JumpScale.portal.docpreprocessor.DocPreprocessorFactory module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.docpreprocessor">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.portal.docgenerator.html"
                           title="previous chapter">JumpScale.portal.docgenerator package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.portal.html.html"
                           title="next chapter">JumpScale.portal.html package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.portal.docpreprocessor.txt"
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
             <a href="JumpScale.portal.html.html" title="JumpScale.portal.html package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.portal.docgenerator.html" title="JumpScale.portal.docgenerator package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.portal.html" >JumpScale.portal package</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>