.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.portal.html package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.portal.macrolib package" href="JumpScale.portal.macrolib.html" />
       <link rel="prev" title="JumpScale.portal.docpreprocessor package" href="JumpScale.portal.docpreprocessor.html" /> 
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
             <a href="JumpScale.portal.macrolib.html" title="JumpScale.portal.macrolib package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.portal.docpreprocessor.html" title="JumpScale.portal.docpreprocessor package"
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
               
     <div class="section" id="jumpscale-portal-html-package">
   <h1>JumpScale.portal.html package<a class="headerlink" href="#jumpscale-portal-html-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.portal.html.BootStrapForm">
   <span id="jumpscale-portal-html-bootstrapform-module"></span><h2>JumpScale.portal.html.BootStrapForm module<a class="headerlink" href="#module-JumpScale.portal.html.BootStrapForm" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.html.BootStrapForm.BootStrapForm">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.BootStrapForm.</tt><tt class="descname">BootStrapForm</tt><big>(</big><em>page</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#BootStrapForm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.BootStrapForm" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.BootStrapForm.addForm">
   <tt class="descname">addForm</tt><big>(</big><em>form</em>, <em>postBackUrl=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#BootStrapForm.addForm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.BootStrapForm.addForm" title="Permalink to this definition">¶</a></dt>
   <dd><p>actor is required if you want to remember position of e.g. a specific object property to a form name</p>
   <p>if postBackUrl==&#8221;&#8221; then will be /wiki/model_$appname_$actorname/$modelname/set
   the post is done by using all args &amp; the caching key (under cachekey)
   get params will be:</p>
   <blockquote>
   <div><ul class="simple">
   <li>cachekey</li>
   </ul>
   </div></blockquote>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.BootStrapForm.getForm">
   <tt class="descname">getForm</tt><big>(</big><em>name=''</em>, <em>actor=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#BootStrapForm.getForm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.BootStrapForm.getForm" title="Permalink to this definition">¶</a></dt>
   <dd><p>actor is required if you want to remember position of e.g. a specific object property to a form name</p>
   <p>how to use:
   actor=j.apps.system.usermanager</p>
   <p>user=actor.model_user_new()
   user.name=&#8221;removeme&#8221;
   guid=actor.model_user_set(user)</p>
   <p>modifier=j.html.getPageModifierBootstrapForm(page)
   form=modifier.getForm(actor=actor)
   form.addTextInput(&#8220;name&#8221;,reference=form.getReference(user,&#8221;name&#8221;),default=&#8221;&#8221;,help=&#8221;&#8221;)
   # form.addTextInput(&#8220;name&#8221;,reference=form.getReference(user,&#8221;name&#8221;),default=&#8221;&#8221;,help=&#8221;&#8221;)
   params.page=modifier.addForm(form)</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.html.BootStrapForm.Form">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.BootStrapForm.</tt><tt class="descname">Form</tt><big>(</big><em>formname=''</em>, <em>actor=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#Form"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.Form" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.Form.addSaveButton">
   <tt class="descname">addSaveButton</tt><big>(</big><em>postBackUrl</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#Form.addSaveButton"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.Form.addSaveButton" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.Form.addSelectFromList">
   <tt class="descname">addSelectFromList</tt><big>(</big><em>label</em>, <em>llist</em>, <em>multiple=False</em>, <em>name=''</em>, <em>reference=None</em>, <em>default=''</em>, <em>help=''</em>, <em>classs='input=xlarge'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#Form.addSelectFromList"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.Form.addSelectFromList" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.Form.addTextInput">
   <tt class="descname">addTextInput</tt><big>(</big><em>label</em>, <em>name=''</em>, <em>reference=None</em>, <em>default=''</em>, <em>help=''</em>, <em>classs='input-xlarge'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#Form.addTextInput"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.Form.addTextInput" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.Form.getReference">
   <tt class="descname">getReference</tt><big>(</big><em>obj</em>, <em>reference</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#Form.getReference"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.Form.getReference" title="Permalink to this definition">¶</a></dt>
   <dd><p>example:
   user=j.apps.system.usermanager.model_user_new()
   getReference(user,&#8221;name&#8221;)
   getReference(user,&#8221;contacts[1].tel&#8221;) #means in list first element with property tel</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.html.BootStrapForm.References">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.BootStrapForm.</tt><tt class="descname">References</tt><big>(</big><em>actor</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#References"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.References" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.References.addReference">
   <tt class="descname">addReference</tt><big>(</big><em>obj</em>, <em>reference</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#References.addReference"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.References.addReference" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.References.getNextId">
   <tt class="descname">getNextId</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#References.getNextId"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.References.getNextId" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.BootStrapForm.References.save">
   <tt class="descname">save</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/BootStrapForm.html#References.save"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.BootStrapForm.References.save" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.html.GridDataTables">
   <span id="jumpscale-portal-html-griddatatables-module"></span><h2>JumpScale.portal.html.GridDataTables module<a class="headerlink" href="#module-JumpScale.portal.html.GridDataTables" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.GridDataTables.</tt><tt class="descname">GridDataTables</tt><big>(</big><em>page</em>, <em>online=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.addSearchOptions">
   <tt class="descname">addSearchOptions</tt><big>(</big><em>tableid='.dataTable'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.addSearchOptions"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.addSearchOptions" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.addSorting">
   <tt class="descname">addSorting</tt><big>(</big><em>tableid='.dataTable'</em>, <em>columnindx=0</em>, <em>order='asc'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.addSorting"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.addSorting" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.addTableForModel">
   <tt class="descname">addTableForModel</tt><big>(</big><em>namespace</em>, <em>category</em>, <em>fieldids</em>, <em>fieldnames=None</em>, <em>fieldvalues=None</em>, <em>filters=None</em>, <em>nativequery=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.addTableForModel"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.addTableForModel" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param namespace: namespace of the model
   &#64;param cateogry: cateogry of the model
   &#64;param fieldids: list of str pointing to the fields of the dataset
   &#64;param fieldnames: list of str showed in the table header if ommited fieldids will be used
   &#64;param fieldvalues: list of items resprenting the value of the data can be a callback</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.addTableFromData">
   <tt class="descname">addTableFromData</tt><big>(</big><em>data</em>, <em>fieldnames</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.addTableFromData"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.addTableFromData" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.addTableFromURL">
   <tt class="descname">addTableFromURL</tt><big>(</big><em>url</em>, <em>fieldnames</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.addTableFromURL"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.addTableFromURL" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.makeTime">
   <tt class="descname">makeTime</tt><big>(</big><em>row</em>, <em>field</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.makeTime"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.makeTime" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.GridDataTables.GridDataTables.prepare4DataTables">
   <tt class="descname">prepare4DataTables</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/GridDataTables.html#GridDataTables.prepare4DataTables"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.GridDataTables.GridDataTables.prepare4DataTables" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.html.HTMLGalleria">
   <span id="jumpscale-portal-html-htmlgalleria-module"></span><h2>JumpScale.portal.html.HTMLGalleria module<a class="headerlink" href="#module-JumpScale.portal.html.HTMLGalleria" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.html.HTMLGalleria.HTMLGalleria">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.HTMLGalleria.</tt><tt class="descname">HTMLGalleria</tt><big>(</big><em>page</em>, <em>online=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HTMLGalleria.html#HTMLGalleria"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HTMLGalleria.HTMLGalleria" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.HTMLGalleria.HTMLGalleria.addImagesFromBucket">
   <tt class="descname">addImagesFromBucket</tt><big>(</big><em>bucketname</em>, <em>subfolder='lowdef   '</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HTMLGalleria.html#HTMLGalleria.addImagesFromBucket"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HTMLGalleria.HTMLGalleria.addImagesFromBucket" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HTMLGalleria.HTMLGalleria.prepare4DataTables">
   <tt class="descname">prepare4DataTables</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HTMLGalleria.html#HTMLGalleria.prepare4DataTables"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HTMLGalleria.HTMLGalleria.prepare4DataTables" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.html.HtmlFactory">
   <span id="jumpscale-portal-html-htmlfactory-module"></span><h2>JumpScale.portal.html.HtmlFactory module<a class="headerlink" href="#module-JumpScale.portal.html.HtmlFactory" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.HtmlFactory.</tt><tt class="descname">HtmlFactory</tt><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.escape">
   <tt class="descname">escape</tt><big>(</big><em>text</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.escape"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.escape" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.getHtmllibDir">
   <tt class="descname">getHtmllibDir</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.getHtmllibDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.getHtmllibDir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierBootstrapForm">
   <tt class="descname">getPageModifierBootstrapForm</tt><big>(</big><em>page</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.getPageModifierBootstrapForm"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierBootstrapForm" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierGalleria">
   <tt class="descname">getPageModifierGalleria</tt><big>(</big><em>page</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.getPageModifierGalleria"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierGalleria" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierGridDataTables">
   <tt class="descname">getPageModifierGridDataTables</tt><big>(</big><em>page</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.getPageModifierGridDataTables"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.getPageModifierGridDataTables" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.HtmlFactory.HtmlFactory.unescape">
   <tt class="descname">unescape</tt><big>(</big><em>text</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/HtmlFactory.html#HtmlFactory.unescape"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.HtmlFactory.HtmlFactory.unescape" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.html.elFinder">
   <span id="jumpscale-portal-html-elfinder-module"></span><h2>JumpScale.portal.html.elFinder module<a class="headerlink" href="#module-JumpScale.portal.html.elFinder" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.portal.html.elFinder.connector">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.elFinder.</tt><tt class="descname">connector</tt><big>(</big><em>opts</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/elFinder.html#connector"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector" title="Permalink to this definition">¶</a></dt>
   <dd><p>Connector for elFinder</p>
   <dl class="attribute">
   <dt id="JumpScale.portal.html.elFinder.connector.httpAllowedParameters">
   <tt class="descname">httpAllowedParameters</tt><em class="property"> = ('cmd', 'download', 'target', 'targets[]', 'current', 'tree', 'name', 'content', 'src', 'dst', 'cut', 'init', 'type', 'width', 'height', 'upload[]')</em><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector.httpAllowedParameters" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.portal.html.elFinder.connector.httpHeader">
   <tt class="descname">httpHeader</tt><em class="property"> = {}</em><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector.httpHeader" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.portal.html.elFinder.connector.httpResponse">
   <tt class="descname">httpResponse</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector.httpResponse" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.portal.html.elFinder.connector.httpStatusCode">
   <tt class="descname">httpStatusCode</tt><em class="property"> = 0</em><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector.httpStatusCode" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.elFinder.connector.run">
   <tt class="descname">run</tt><big>(</big><em>httpRequest=</em><span class="optional">[</span><span class="optional">]</span><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/elFinder.html#connector.run"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.elFinder.connector.run" title="Permalink to this definition">¶</a></dt>
   <dd><p>main function</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.portal.html.multipart">
   <span id="jumpscale-portal-html-multipart-module"></span><h2>JumpScale.portal.html.multipart module<a class="headerlink" href="#module-JumpScale.portal.html.multipart" title="Permalink to this headline">¶</a></h2>
   <div class="section" id="parser-for-multipart-form-data">
   <h3>Parser for multipart/form-data<a class="headerlink" href="#parser-for-multipart-form-data" title="Permalink to this headline">¶</a></h3>
   <p>This module provides a parser for the multipart/form-data format. It can read
   from a file, a socket or a WSGI environment. The parser can be used to replace
   cgi.FieldStorage (without the bugs) and works with Python 2.5+ and 3.x (2to3).</p>
   <div class="section" id="licence-mit">
   <h4>Licence (MIT)<a class="headerlink" href="#licence-mit" title="Permalink to this headline">¶</a></h4>
   <blockquote>
   <div><p>Copyright (c) 2010, Marcel Hellkamp.
   Inspired by the Werkzeug library: <a class="reference external" href="http://werkzeug.pocoo.org/">http://werkzeug.pocoo.org/</a></p>
   <p>Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the &#8220;Software&#8221;), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:</p>
   <p>The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.</p>
   <p>THE SOFTWARE IS PROVIDED &#8220;AS IS&#8221;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.</p>
   </div></blockquote>
   <dl class="class">
   <dt id="JumpScale.portal.html.multipart.MultiDict">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">MultiDict</tt><big>(</big><em>*a</em>, <em>**k</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">_abcoll.MutableMapping</span></tt></p>
   <p>A dict that remembers old values for each key</p>
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.append">
   <tt class="descname">append</tt><big>(</big><em>key</em>, <em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.append"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.append" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.get">
   <tt class="descname">get</tt><big>(</big><em>key</em>, <em>default=None</em>, <em>index=-1</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.get" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.getall">
   <tt class="descname">getall</tt><big>(</big><em>key</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.getall"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.getall" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.iterallitems">
   <tt class="descname">iterallitems</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.iterallitems"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.iterallitems" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.keys">
   <tt class="descname">keys</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.keys"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.keys" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultiDict.replace">
   <tt class="descname">replace</tt><big>(</big><em>key</em>, <em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultiDict.replace"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultiDict.replace" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="exception">
   <dt id="JumpScale.portal.html.multipart.MultipartError">
   <em class="property">exception </em><tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">MultipartError</tt><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartError"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartError" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/exceptions.html#exceptions.ValueError" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">exceptions.ValueError</span></tt></a></p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.html.multipart.MultipartParser">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">MultipartParser</tt><big>(</big><em>stream</em>, <em>boundary</em>, <em>content_length=-1</em>, <em>disk_limit=1073741824</em>, <em>mem_limit=1048576</em>, <em>memfile_limit=262144</em>, <em>buffer_size=65536</em>, <em>charset='latin1'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartParser"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartParser" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartParser.get">
   <tt class="descname">get</tt><big>(</big><em>name</em>, <em>default=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartParser.get"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartParser.get" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return the first part with that name or a default value (None).</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartParser.get_all">
   <tt class="descname">get_all</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartParser.get_all"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartParser.get_all" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return a list of parts with that name.</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartParser.parts">
   <tt class="descname">parts</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartParser.parts"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartParser.parts" title="Permalink to this definition">¶</a></dt>
   <dd><p>Returns a list with all parts of the multipart message.</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.portal.html.multipart.MultipartPart">
   <em class="property">class </em><tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">MultipartPart</tt><big>(</big><em>buffer_size=65536</em>, <em>memfile_limit=262144</em>, <em>charset='latin1'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.feed">
   <tt class="descname">feed</tt><big>(</big><em>line</em>, <em>nl=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.feed"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.feed" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.finish_header">
   <tt class="descname">finish_header</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.finish_header"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.finish_header" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.is_buffered">
   <tt class="descname">is_buffered</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.is_buffered"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.is_buffered" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return true if the data is fully buffered in memory.</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.save_as">
   <tt class="descname">save_as</tt><big>(</big><em>path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.save_as"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.save_as" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.value">
   <tt class="descname">value</tt><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.value"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.value" title="Permalink to this definition">¶</a></dt>
   <dd><p>Data decoded with the specified charset</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.write_body">
   <tt class="descname">write_body</tt><big>(</big><em>line</em>, <em>nl</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.write_body"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.write_body" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.portal.html.multipart.MultipartPart.write_header">
   <tt class="descname">write_header</tt><big>(</big><em>line</em>, <em>nl</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#MultipartPart.write_header"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.MultipartPart.write_header" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.copy_file">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">copy_file</tt><big>(</big><em>stream</em>, <em>target</em>, <em>maxread=-1</em>, <em>buffer_size=32</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#copy_file"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.copy_file" title="Permalink to this definition">¶</a></dt>
   <dd><p>Read from :stream and write to :target until :maxread or EOF.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.header_quote">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">header_quote</tt><big>(</big><em>val</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#header_quote"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.header_quote" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.header_unquote">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">header_unquote</tt><big>(</big><em>val</em>, <em>filename=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#header_unquote"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.header_unquote" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.parse_form_data">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">parse_form_data</tt><big>(</big><em>environ</em>, <em>charset='utf8'</em>, <em>strict=False</em>, <em>**kw</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#parse_form_data"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.parse_form_data" title="Permalink to this definition">¶</a></dt>
   <dd><p>Parse form data from an environ dict and return a (forms, files) tuple.
   Both tuple values are dictionaries with the form-field name as a key
   (unicode) and lists as values (multiple values per key are possible).
   The forms-dictionary contains form-field values as unicode strings.
   The files-dictionary contains <a class="reference internal" href="#JumpScale.portal.html.multipart.MultipartPart" title="JumpScale.portal.html.multipart.MultipartPart"><tt class="xref py py-class docutils literal"><span class="pre">MultipartPart</span></tt></a> instances, either
   because the form-field was a file-upload or the value is to big to fit
   into memory limits.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
   <li><strong>environ</strong> &#8211; An WSGI environment dict.</li>
   <li><strong>charset</strong> &#8211; The charset to use if unsure. (default: utf8)</li>
   <li><strong>strict</strong> &#8211; If True, raise <a class="reference internal" href="#JumpScale.portal.html.multipart.MultipartError" title="JumpScale.portal.html.multipart.MultipartError"><tt class="xref py py-exc docutils literal"><span class="pre">MultipartError</span></tt></a> on any parsing
   errors. These are silently ignored by default.</li>
   </ul>
   </td>
   </tr>
   </tbody>
   </table>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.parse_options_header">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">parse_options_header</tt><big>(</big><em>header</em>, <em>options=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#parse_options_header"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.parse_options_header" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.portal.html.multipart.tob">
   <tt class="descclassname">JumpScale.portal.html.multipart.</tt><tt class="descname">tob</tt><big>(</big><em>data</em>, <em>enc='utf8'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/portal/html/multipart.html#tob"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.portal.html.multipart.tob" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </div>
   </div>
   </div>
   <div class="section" id="module-JumpScale.portal.html">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.portal.html" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.portal.html package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.BootStrapForm">JumpScale.portal.html.BootStrapForm module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.GridDataTables">JumpScale.portal.html.GridDataTables module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.HTMLGalleria">JumpScale.portal.html.HTMLGalleria module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.HtmlFactory">JumpScale.portal.html.HtmlFactory module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.elFinder">JumpScale.portal.html.elFinder module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html.multipart">JumpScale.portal.html.multipart module</a><ul>
   <li><a class="reference internal" href="#parser-for-multipart-form-data">Parser for multipart/form-data</a><ul>
   <li><a class="reference internal" href="#licence-mit">Licence (MIT)</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li><a class="reference internal" href="#module-JumpScale.portal.html">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.portal.docpreprocessor.html"
                           title="previous chapter">JumpScale.portal.docpreprocessor package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.portal.macrolib.html"
                           title="next chapter">JumpScale.portal.macrolib package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.portal.html.txt"
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
             <a href="JumpScale.portal.macrolib.html" title="JumpScale.portal.macrolib package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.portal.docpreprocessor.html" title="JumpScale.portal.docpreprocessor package"
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