.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.lib.html package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="up" title="JumpScale.lib package" href="JumpScale.lib.html" />
       <link rel="next" title="JumpScale.lib.jail package" href="JumpScale.lib.jail.html" />
       <link rel="prev" title="JumpScale.lib.docker package" href="JumpScale.lib.docker.html" /> 
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
             <a href="JumpScale.lib.jail.html" title="JumpScale.lib.jail package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.lib.docker.html" title="JumpScale.lib.docker package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.lib.html" accesskey="U">JumpScale.lib package</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <div class="section" id="jumpscale-lib-html-package">
   <h1>JumpScale.lib.html package<a class="headerlink" href="#jumpscale-lib-html-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.lib.html.HTML2Text">
   <span id="jumpscale-lib-html-html2text-module"></span><h2>JumpScale.lib.html.HTML2Text module<a class="headerlink" href="#module-JumpScale.lib.html.HTML2Text" title="Permalink to this headline">¶</a></h2>
   <p>html2text: Turn HTML into equivalent Markdown-structured text.</p>
   <dl class="class">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text">
   <em class="property">class </em><tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">HTML2Text</tt><big>(</big><em>out=None</em>, <em>baseurl=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference external" href="http://docs.python.org/library/htmlparser.html#HTMLParser.HTMLParser" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">HTMLParser.HTMLParser</span></tt></a></p>
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.charref">
   <tt class="descname">charref</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.charref"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.charref" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.close">
   <tt class="descname">close</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.close"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.close" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.drop_last">
   <tt class="descname">drop_last</tt><big>(</big><em>nLetters</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.drop_last"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.drop_last" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.entityref">
   <tt class="descname">entityref</tt><big>(</big><em>c</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.entityref"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.entityref" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.feed">
   <tt class="descname">feed</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.feed"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.feed" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.google_nest_count">
   <tt class="descname">google_nest_count</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.google_nest_count"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.google_nest_count" title="Permalink to this definition">¶</a></dt>
   <dd><p>calculate the nesting count of google doc lists</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle">
   <tt class="descname">handle</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_charref">
   <tt class="descname">handle_charref</tt><big>(</big><em>c</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_charref"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_charref" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_data">
   <tt class="descname">handle_data</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_data"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_data" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_emphasis">
   <tt class="descname">handle_emphasis</tt><big>(</big><em>start</em>, <em>tag_style</em>, <em>parent_style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_emphasis"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_emphasis" title="Permalink to this definition">¶</a></dt>
   <dd><p>handles various text emphases</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_endtag">
   <tt class="descname">handle_endtag</tt><big>(</big><em>tag</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_endtag"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_endtag" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_entityref">
   <tt class="descname">handle_entityref</tt><big>(</big><em>c</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_entityref"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_entityref" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_starttag">
   <tt class="descname">handle_starttag</tt><big>(</big><em>tag</em>, <em>attrs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_starttag"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_starttag" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.handle_tag">
   <tt class="descname">handle_tag</tt><big>(</big><em>tag</em>, <em>attrs</em>, <em>start</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.handle_tag"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.handle_tag" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.o">
   <tt class="descname">o</tt><big>(</big><em>data</em>, <em>puredata=0</em>, <em>force=0</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.o"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.o" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.optwrap">
   <tt class="descname">optwrap</tt><big>(</big><em>text</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.optwrap"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.optwrap" title="Permalink to this definition">¶</a></dt>
   <dd><p>Wrap all paragraphs in the provided text.</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.outtextf">
   <tt class="descname">outtextf</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.outtextf"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.outtextf" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.p">
   <tt class="descname">p</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.p"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.p" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.pbr">
   <tt class="descname">pbr</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.pbr"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.pbr" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.previousIndex">
   <tt class="descname">previousIndex</tt><big>(</big><em>attrs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.previousIndex"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.previousIndex" title="Permalink to this definition">¶</a></dt>
   <dd><p>returns the index of certain set of attributes (of a link) in the
   self.a list</p>
   <p>If the set of attributes is not found, returns None</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.r_unescape">
   <tt class="descname">r_unescape</tt><em class="property"> = &lt;_sre.SRE_Pattern object at 0x4d80ae0&gt;</em><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.r_unescape" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.replaceEntities">
   <tt class="descname">replaceEntities</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.replaceEntities"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.replaceEntities" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.soft_br">
   <tt class="descname">soft_br</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.soft_br"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.soft_br" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.unescape">
   <tt class="descname">unescape</tt><big>(</big><em>s</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.unescape"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.unescape" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.lib.html.HTML2Text.HTML2Text.unknown_decl">
   <tt class="descname">unknown_decl</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#HTML2Text.unknown_decl"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.HTML2Text.unknown_decl" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.dumb_css_parser">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">dumb_css_parser</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#dumb_css_parser"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.dumb_css_parser" title="Permalink to this definition">¶</a></dt>
   <dd><p>returns a hash of css selectors, each of which contains a hash of css attributes</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.dumb_property_dict">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">dumb_property_dict</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#dumb_property_dict"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.dumb_property_dict" title="Permalink to this definition">¶</a></dt>
   <dd><p>returns a hash of css attributes</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.element_style">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">element_style</tt><big>(</big><em>attrs</em>, <em>style_def</em>, <em>parent_style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#element_style"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.element_style" title="Permalink to this definition">¶</a></dt>
   <dd><p>returns a hash of the &#8216;final&#8217; style attributes of the element</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.escape_md">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">escape_md</tt><big>(</big><em>text</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#escape_md"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.escape_md" title="Permalink to this definition">¶</a></dt>
   <dd><p>Escapes markdown-sensitive characters within other markdown constructs.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.escape_md_section">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">escape_md_section</tt><big>(</big><em>text</em>, <em>snob=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#escape_md_section"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.escape_md_section" title="Permalink to this definition">¶</a></dt>
   <dd><p>Escapes markdown-sensitive characters across whole document sections.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.google_fixed_width_font">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">google_fixed_width_font</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#google_fixed_width_font"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.google_fixed_width_font" title="Permalink to this definition">¶</a></dt>
   <dd><p>check if the css of the current element defines a fixed width font</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.google_has_height">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">google_has_height</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#google_has_height"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.google_has_height" title="Permalink to this definition">¶</a></dt>
   <dd><p>check if the style of the element has the &#8216;height&#8217; attribute explicitly defined</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.google_list_style">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">google_list_style</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#google_list_style"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.google_list_style" title="Permalink to this definition">¶</a></dt>
   <dd><p>finds out whether this is an ordered or unordered list</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.google_text_emphasis">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">google_text_emphasis</tt><big>(</big><em>style</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#google_text_emphasis"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.google_text_emphasis" title="Permalink to this definition">¶</a></dt>
   <dd><p>return a list of all emphasis modifiers of the element</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.has_key">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">has_key</tt><big>(</big><em>x</em>, <em>y</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#has_key"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.has_key" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.hn">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">hn</tt><big>(</big><em>tag</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#hn"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.hn" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.html2text">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">html2text</tt><big>(</big><em>html</em>, <em>baseurl=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#html2text"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.html2text" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.list_numbering_start">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">list_numbering_start</tt><big>(</big><em>attrs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#list_numbering_start"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.list_numbering_start" title="Permalink to this definition">¶</a></dt>
   <dd><p>extract numbering from list element attributes</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.main">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">main</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#main"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.main" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.name2cp">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">name2cp</tt><big>(</big><em>k</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#name2cp"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.name2cp" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.onlywhite">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">onlywhite</tt><big>(</big><em>line</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#onlywhite"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.onlywhite" title="Permalink to this definition">¶</a></dt>
   <dd><p>Return true if the line does only consist of whitespace characters.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.skipwrap">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">skipwrap</tt><big>(</big><em>para</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#skipwrap"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.skipwrap" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.unescape">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">unescape</tt><big>(</big><em>s</em>, <em>unicode_snob=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#unescape"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.unescape" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.lib.html.HTML2Text.wrapwrite">
   <tt class="descclassname">JumpScale.lib.html.HTML2Text.</tt><tt class="descname">wrapwrite</tt><big>(</big><em>text</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTML2Text.html#wrapwrite"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTML2Text.wrapwrite" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.lib.html.HTMLFactory">
   <span id="jumpscale-lib-html-htmlfactory-module"></span><h2>JumpScale.lib.html.HTMLFactory module<a class="headerlink" href="#module-JumpScale.lib.html.HTMLFactory" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.lib.html.HTMLFactory.HTMLFactory">
   <em class="property">class </em><tt class="descclassname">JumpScale.lib.html.HTMLFactory.</tt><tt class="descname">HTMLFactory</tt><a class="reference internal" href="../_modules/JumpScale/lib/html/HTMLFactory.html#HTMLFactory"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTMLFactory.HTMLFactory" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.lib.html.HTMLFactory.HTMLFactory.html2text">
   <tt class="descname">html2text</tt><big>(</big><em>html</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/lib/html/HTMLFactory.html#HTMLFactory.html2text"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.lib.html.HTMLFactory.HTMLFactory.html2text" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.lib.html">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.lib.html" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.lib.html package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.lib.html.HTML2Text">JumpScale.lib.html.HTML2Text module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.lib.html.HTMLFactory">JumpScale.lib.html.HTMLFactory module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.lib.html">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.lib.docker.html"
                           title="previous chapter">JumpScale.lib.docker package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.lib.jail.html"
                           title="next chapter">JumpScale.lib.jail package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.lib.html.txt"
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
             <a href="JumpScale.lib.jail.html" title="JumpScale.lib.jail package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.lib.docker.html" title="JumpScale.lib.docker package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.lib.html" >JumpScale.lib package</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>