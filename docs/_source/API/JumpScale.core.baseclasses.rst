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
   
       <title>JumpScale.core.baseclasses package &mdash; Jumpscale Doc 7.0 documentation</title>
   
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
       <link rel="next" title="JumpScale.core.config package" href="JumpScale.core.config.html" />
       <link rel="prev" title="JumpScale.core.base.time package" href="JumpScale.core.base.time.html" />
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
             <a href="JumpScale.core.config.html" title="JumpScale.core.config package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.base.time.html" title="JumpScale.core.base.time package"
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
   
     <div class="section" id="jumpscale-core-baseclasses-package">
   <h1>JumpScale.core.baseclasses package<a class="headerlink" href="#jumpscale-core-baseclasses-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.core.baseclasses.BaseEnumeration">
   <span id="jumpscale-core-baseclasses-baseenumeration-module"></span><h2>JumpScale.core.baseclasses.BaseEnumeration module<a class="headerlink" href="#module-JumpScale.core.baseclasses.BaseEnumeration" title="Permalink to this headline">¶</a></h2>
   <p>Base Enumeration type implementation</p>
   <div class="section" id="enumeration-lifecycle">
   <h3>Enumeration lifecycle<a class="headerlink" href="#enumeration-lifecycle" title="Permalink to this headline">¶</a></h3>
   <p>Since the BaseEnumeration type implementation in the following 270 lines of code
   (maybe more at the time you read this) can be non-obvious at first sight,
   here&#8217;s an overview of the lifecycle of an enumeration, several pitfalls and
   how we get around them.</p>
   <div class="section" id="enumeration-definition">
   <h4>Enumeration definition<a class="headerlink" href="#enumeration-definition" title="Permalink to this headline">¶</a></h4>
   <p>Enumerations are ordinary classes which got the L{BaseEnumeration} class as base.
   The BaseEnumeration class itself provides not much functionality, next to basic
   implementations of __str__ and __repr__, a check method which checks whether
   a given variable is a valid enumeration item (cfr check methods on other
   pmtype classes), and a generic getByName method which retrieves an enumeration
   item based on its name.</p>
   <p>The hard labour is performed by the custom metaclass of BaseEnumeration,
   BaseEnumerationMeta.</p>
   </div>
   <div class="section" id="baseenumerationmeta-magic">
   <h4>BaseEnumerationMeta magic<a class="headerlink" href="#baseenumerationmeta-magic" title="Permalink to this headline">¶</a></h4>
   <p>This class behaves like any other metaclass, generating types from a class.
   Once the type is created, 2 classmethods are added to it, by using a function
   generator: registerItem (generated by generateRegisterItem) and
   finishItemRegistration (generated by generateFinishItemRegistration). These are
   added per-type and not on the BaseEnumeration base type, since we want to be able
   to remove them from types once the type finishItemRegistration is called. If
   the methods would be defined in the BaseEnumeration base type, we would not be able
   to remove them from actual enumeration types (subclasses) unless removing them
   from the BaseEnumeration base class, which would result in a situation where the
   methods are no longer available on any BaseEnumeration subclasses.</p>
   <p>Next to type generation, we cache all generated types, using the full path of
   the module they are defined in (minus extension) and the type name as key. We
   strip the extension because it is possible a type is initially loaded from (eg)
   /foo/bar.py and later on (in the same process) from /foo/bar.pyc, since the
   Python interpreter will generate the precompiled pyc file when the source file
   is loaded the first time, using this one later on.</p>
   </div>
   <div class="section" id="lazy-loading-pitfalls-and-type-caching">
   <h4>Lazy loading pitfalls and type caching<a class="headerlink" href="#lazy-loading-pitfalls-and-type-caching" title="Permalink to this headline">¶</a></h4>
   <p>It might sound strange types should be cached: once a module is loaded into the
   Python process, types defined in it should be generated, registered, and used
   later on, right?</p>
   <p>Well, in a normal application this is the way it&#8217;s supposed to work. Inside
   jumpscale we got one extra catch though: lazy-loading of extensions.</p>
   <p>When an extension is lazy-loaded, this is done using the load_module function
   of the built-in imp module. This results in a complete reload of the module and
   any (directly or indirectly) imported module. This results in a recreation of
   all types as well (ie the already registered types are not reused). In normal
   situations this is not an issue, except here, since in the &#8216;check&#8217; method of
   BaseEnumeration we use an &#8216;is&#8217; comparison.</p>
   <p>We can get around this by caching all types we create in our metaclass, based
   on definition module and name of the class.</p>
   </div>
   <div class="section" id="when-even-caching-becomes-complicated">
   <h4>When even caching becomes complicated<a class="headerlink" href="#when-even-caching-becomes-complicated" title="Permalink to this headline">¶</a></h4>
   <p>Caching our types resolves the issue presented in the previous section. More
   problems arise though. If we defined an enumeration once, registered one or
   more items, and called finishItemRegistration, the registerItem and
   finishItemRegistration methods (attributes) are no longer available on the
   type. When we load an extension using the same enumeration (importing the
   module where the enumeration is defined once again), the existing type will be
   returned when the enumeration class is parsed, returning the type which no
   longer got registerItem and finishItemRegistration attributes. In the
   enumeration definition module, there will most likely be calls to the
   registerItem and finishItemRegistration methods (ie the same code which created
   all items initially). This implies we need to re-add the necessary methods to
   the enumeration class.</p>
   <p>We do this by adding a registerItem callable which does nothing at all, and a
   new finishItemRegistration method as generated by
   generateFinishItemRegistration.</p>
   </div>
   <div class="section" id="the-story-of-intermediate-classes">
   <h4>The story of intermediate classes<a class="headerlink" href="#the-story-of-intermediate-classes" title="Permalink to this headline">¶</a></h4>
   <p>One more item to tackle: &#8216;intermediate classes&#8217;. An intermediate enumeration
   is a subclass of BaseEnumeration which represents no actual object by itself, but
   should be subclassed by real enumerations, only providing some extra
   functionality (eg EnumerationWithValue). We do not want to be able to register
   items on these classes, so we don&#8217;t add registerItem or finishItemRegistration
   methods to these classes, which can be identified by a special class attribute
   they should set, C{_INTERMEDIATE_CLASS}.</p>
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">BaseEnumeration</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumeration"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Base class for any enumeration-style class</p>
   <p>If you are creating a subclass of BaseEnumeration which is <em>not</em> a &#8216;final&#8217;
   class (ie representing a real-world object, just creating an BaseEnumeration
   type which provides some more functionality which should be subclassed as
   well), you should add an attribute called _INTERMEDIATE_CLASS to your
   intermediate class so the BaseEnumeration type system can take this into
   account when adding methods to final classes.</p>
   <p>Subclasses of BaseEnumeration can have a classmethod called C{_initItems}
   which will be called when the corresponding type is constructed. Thisj.enumerators.MessageType.UNKNOWN
   allows you to add items to an enumeration inside the enumeration
   definition, eg:</p>
   <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">MyEnumeration</span><span class="p">(</span><span class="n">BaseEnumeration</span><span class="p">):</span>
   <span class="gp">... </span>    <span class="nd">@classmethod</span>
   <span class="gp">... </span>    <span class="k">def</span> <span class="nf">_initItems</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">registerItem</span><span class="p">(</span><span class="s">&#39;foo&#39;</span><span class="p">)</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">registerItem</span><span class="p">(</span><span class="s">&#39;bar&#39;</span><span class="p">)</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">finishItemRegistration</span><span class="p">()</span>
   <span class="gp">...</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">MyEnumeration</span><span class="o">.</span><span class="n">FOO</span>
   <span class="go">foo</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">MyEnumeration</span><span class="o">.</span><span class="n">BAR</span>
   <span class="go">bar</span>
   </pre></div>
   </div>
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.check">
   <em class="property">classmethod </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumeration.check"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Type check for this enumeration type</p>
   <p>This method checks whether the provided argument value is an instance
   of this enumeration type and is registered on it.</p>
   <p>&#64;param value: Value to validate
   &#64;type value: BaseEnumeration subclass
   &#64;returns: Whether value is a valid enumeration item
   &#64;rtype: bool</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.getByLevel">
   <em class="property">classmethod </em><tt class="descname">getByLevel</tt><big>(</big><em>level</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumeration.getByLevel"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.getByLevel" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get enumeration value based on item level as provided to L{registerItem}
   only works for enumeration where level has been defined</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.getByName">
   <em class="property">classmethod </em><tt class="descname">getByName</tt><big>(</big><em>itemname</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumeration.getByName"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.getByName" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get enumeration value based on item name as provided to L{registerItem}</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.printdoc">
   <tt class="descname">printdoc</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumeration.printdoc"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration.printdoc" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumerationMeta">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">BaseEnumerationMeta</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#BaseEnumerationMeta"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumerationMeta" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">type</span></tt></p>
   <p>Meta class for BaseEnumeration and its subclasses</p>
   <p>We want to be able to remove the registerItem and finishItemRegistration
   methods from subclasses of BaseEnumeration at runtime, more precisely after
   finishItemRegistration on a subclass is called.</p>
   <p>These methods are attributes at class-level (ie. on the enumeration
   subclass or one of its parents).</p>
   <p>We can not place the methods in the BaseEnumeration class (which would be more
   logical), because if we&#8217;d put it there, removing the desired methods from
   subclasses won&#8217;t work, because they are not attributes on the actual
   subclass (they are attributes on the parent Enumeration class). We could
   obviously remove them from the parent BaseEnumeration class, but then, all at
   once, the method would be completely gone on _any_ subclass of BaseEnumeration
   as well, including unfinished enumerations. Which is not exactly the
   desired behaviour.</p>
   <p>As explained in the previous paragraphs, we can&#8217;t have registerItem and
   finishItemRegistration on the BaseEnumeration class, so we should add them as
   attributes to the actual enumeration subclasses. This way we _can_ remove
   the methods from the class (and it&#8217;s instances) at runtime.</p>
   <p>This is exactly what this metaclass does: it generates the desired methods
   using some method generators, and adds them as attributes on the
   BaseEnumeration subclasses.</p>
   <p>It does not add the methods on the BaseEnumeration type itself, so this class
   is (and should be) useless as-is.</p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.EnumerationProperty">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">EnumerationProperty</tt><big>(</big><em>enumtype</em>, <em>fget=None</em>, <em>fset=None</em>, <em>fdel=None</em>, <em>doc=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#EnumerationProperty"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.EnumerationProperty" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">property</span></tt></p>
   <p>Specialized descriptor for Enumeration class attributes</p>
   <p>This descriptor (think &#8216;property&#8217;) can be used when the property value
   should be an item of an enumeration. The Enumeration type should be
   provided to the constructor, after which automatic type checking is
   performed when trying to set the attribute, and string conversion is done
   behind the scenes.</p>
   <p>This string conversion makes sure only the item name is stored as an
   attribute on the class instance, not the enumeration item itself. This
   removes several potential pitfalls when serializing (pickling) the
   instance.</p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.EnumerationWithValue">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">EnumerationWithValue</tt><big>(</big><em>value</em>, <em>doc=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#EnumerationWithValue"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.EnumerationWithValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration" title="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration</span></tt></a></p>
   <p>Enumeration base type providing separation between item name and value</p>
   <p>Since some names (which are invalid Python identifiers) are forbidden as
   enumeration item name, this class provides separation between item names
   and item value (which is the value returned by __str__, equal to name in
   the basic Enumeration type).</p>
   <p>Next to this, it offers a &#8216;doc&#8217; attribute which is returned by __repr__.</p>
   <p>Example use case: the VirtualboxNicType enumeration contains an item which
   should be called &#8216;82540EM&#8217;. This is an invalid identifier, so it had to be
   renamed to &#8216;I82540EM&#8217; as name. We still want to provide the original value
   as well though.
   Next to this, &#8216;82540EM&#8217; is not easy to understand, so we want to represent
   the item as &#8216;Intel PRO/1000MT Desktop&#8217; to the end-user, which is the doc
   property displayed by __repr__.</p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.JSModelEnumerationContainer">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">JSModelEnumerationContainer</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#JSModelEnumerationContainer"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.JSModelEnumerationContainer" title="Permalink to this definition">¶</a></dt>
   <dd><p>Dummy object to store the JSModel enumerators on it</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.generateFinishItemRegistration">
   <tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">generateFinishItemRegistration</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#generateFinishItemRegistration"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.generateFinishItemRegistration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generate an C{BaseEnumeration.finishItemRegistration} method</p>
   <p>We need this external generator so we can add the finishItemRegistration
   method to subclasses of BaseEnumeration in their metaclass.</p>
   <p>We need to set the methods per subclass, otherwise we can&#8217;t del the method
   attribute from the class when the consumer calls finishItemRegistration.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.generateRegisterItem">
   <tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">generateRegisterItem</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#generateRegisterItem"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.generateRegisterItem" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generate an C{BaseEnumeration.registerItem} method</p>
   <p>We need this external generator so we can add the registerItem method to
   subclasses of BaseEnumeration in their metaclass.</p>
   <p>We need to set the methods per subclass, otherwise we can&#8217;t delete the method
   attribute from the class when the consumer calls C{finishItemRegistration}.</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.getEnumName">
   <tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">getEnumName</tt><big>(</big><em>name</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#getEnumName"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.getEnumName" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.isValidIdentifier">
   <tt class="descclassname">JumpScale.core.baseclasses.BaseEnumeration.</tt><tt class="descname">isValidIdentifier</tt><big>(</big><em>identifier</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseEnumeration.html#isValidIdentifier"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.isValidIdentifier" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether a given string is a valid Python identifier (variable name)</p>
   <p>In several places (when using user-provided names to create properties or
   attributes) we should be able to alert the user when attempting to use an
   invalid identifier, as defined by the Python grammar.</p>
   <p>This method checks names against the grammar snippet specified in the
   Python language reference (<a class="reference external" href="http://docs.python.org/ref/identifiers.html">http://docs.python.org/ref/identifiers.html</a>).</p>
   <p>It also filters out keywords.</p>
   <p>&#64;param identifier: Identifier to check
   &#64;type identified: string</p>
   <p>&#64;returns: Whether or not the provided identifier is valid
   &#64;rtype: bool</p>
   </dd></dl>
   
   </div>
   </div>
   </div>
   <div class="section" id="module-JumpScale.core.baseclasses.BaseType">
   <span id="jumpscale-core-baseclasses-basetype-module"></span><h2>JumpScale.core.baseclasses.BaseType module<a class="headerlink" href="#module-JumpScale.core.baseclasses.BaseType" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseType.BaseType">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseType.</tt><tt class="descname">BaseType</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseType.html#BaseType"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseType.BaseType" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseType.BaseTypeMeta">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.BaseType.</tt><tt class="descname">BaseTypeMeta</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseType.html#BaseTypeMeta"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseType.BaseTypeMeta" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">type</span></tt></p>
   <p>Meta class for all BaseTypes, makes sure we know the name of descriptor attributes</p>
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.core.baseclasses.BaseType.generate_init_properties">
   <tt class="descclassname">JumpScale.core.baseclasses.BaseType.</tt><tt class="descname">generate_init_properties</tt><big>(</big><em>cls</em>, <em>attrs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/BaseType.html#generate_init_properties"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.BaseType.generate_init_properties" title="Permalink to this definition">¶</a></dt>
   <dd><p>Generate a class __init_properties__ method</p>
   <p>&#64;param cls: Type to generate method for
   &#64;type cls: type
   &#64;param attrs: Class construction attributes
   &#64;type attrs: dict</p>
   <p>&#64;returns: __init_properties__ method
   &#64;rtype: method</p>
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.baseclasses.dirtyflaggingmixin">
   <span id="jumpscale-core-baseclasses-dirtyflaggingmixin-module"></span><h2>JumpScale.core.baseclasses.dirtyflaggingmixin module<a class="headerlink" href="#module-JumpScale.core.baseclasses.dirtyflaggingmixin" title="Permalink to this headline">¶</a></h2>
   <p>Mixin and helpers to access &#8216;dirty flagging&#8217; information set by pmtypes</p>
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.dirtyflaggingmixin.</tt><tt class="descname">DirtyFlaggingMixin</tt><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/dirtyflaggingmixin.html#DirtyFlaggingMixin"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin" title="Permalink to this definition">¶</a></dt>
   <dd><p>Mixin class that will add 2 attributes on the a class containing data about changes to the properties</p>
   <dl class="attribute">
   <dt id="JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.dirtyProperties">
   <tt class="descname">dirtyProperties</tt><a class="headerlink" href="#JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.dirtyProperties" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether a given object was dirtied after last save</p>
   <p>&#64;type: bool</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.isDirtiedAfterSave">
   <tt class="descname">isDirtiedAfterSave</tt><a class="headerlink" href="#JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.isDirtiedAfterSave" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.isDirty">
   <tt class="descname">isDirty</tt><a class="headerlink" href="#JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.isDirty" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get a set of all dirtied properties</p>
   <p>&#64;type: set</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.reset_dirtied_after_save">
   <tt class="descname">reset_dirtied_after_save</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/core/baseclasses/dirtyflaggingmixin.html#DirtyFlaggingMixin.reset_dirtied_after_save"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.core.baseclasses.dirtyflaggingmixin.DirtyFlaggingMixin.reset_dirtied_after_save" title="Permalink to this definition">¶</a></dt>
   <dd><p>Reset dirtied after save state</p>
   <p>Call this from the function which saves to object to CMDB.</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.core.baseclasses">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.core.baseclasses" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.</tt><tt class="descname">BaseEnumeration</tt><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Base class for any enumeration-style class</p>
   <p>If you are creating a subclass of BaseEnumeration which is <em>not</em> a &#8216;final&#8217;
   class (ie representing a real-world object, just creating an BaseEnumeration
   type which provides some more functionality which should be subclassed as
   well), you should add an attribute called _INTERMEDIATE_CLASS to your
   intermediate class so the BaseEnumeration type system can take this into
   account when adding methods to final classes.</p>
   <p>Subclasses of BaseEnumeration can have a classmethod called C{_initItems}
   which will be called when the corresponding type is constructed. Thisj.enumerators.MessageType.UNKNOWN
   allows you to add items to an enumeration inside the enumeration
   definition, eg:</p>
   <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">MyEnumeration</span><span class="p">(</span><span class="n">BaseEnumeration</span><span class="p">):</span>
   <span class="gp">... </span>    <span class="nd">@classmethod</span>
   <span class="gp">... </span>    <span class="k">def</span> <span class="nf">_initItems</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">registerItem</span><span class="p">(</span><span class="s">&#39;foo&#39;</span><span class="p">)</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">registerItem</span><span class="p">(</span><span class="s">&#39;bar&#39;</span><span class="p">)</span>
   <span class="gp">... </span>        <span class="n">cls</span><span class="o">.</span><span class="n">finishItemRegistration</span><span class="p">()</span>
   <span class="gp">...</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">MyEnumeration</span><span class="o">.</span><span class="n">FOO</span>
   <span class="go">foo</span>
   <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">MyEnumeration</span><span class="o">.</span><span class="n">BAR</span>
   <span class="go">bar</span>
   </pre></div>
   </div>
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.check">
   <em class="property">classmethod </em><tt class="descname">check</tt><big>(</big><em>value</em><big>)</big><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.check" title="Permalink to this definition">¶</a></dt>
   <dd><p>Type check for this enumeration type</p>
   <p>This method checks whether the provided argument value is an instance
   of this enumeration type and is registered on it.</p>
   <p>&#64;param value: Value to validate
   &#64;type value: BaseEnumeration subclass
   &#64;returns: Whether value is a valid enumeration item
   &#64;rtype: bool</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.getByLevel">
   <em class="property">classmethod </em><tt class="descname">getByLevel</tt><big>(</big><em>level</em><big>)</big><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.getByLevel" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get enumeration value based on item level as provided to L{registerItem}
   only works for enumeration where level has been defined</p>
   </dd></dl>
   
   <dl class="classmethod">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.getByName">
   <em class="property">classmethod </em><tt class="descname">getByName</tt><big>(</big><em>itemname</em><big>)</big><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.getByName" title="Permalink to this definition">¶</a></dt>
   <dd><p>Get enumeration value based on item name as provided to L{registerItem}</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.core.baseclasses.BaseEnumeration.printdoc">
   <tt class="descname">printdoc</tt><big>(</big><big>)</big><a class="headerlink" href="#JumpScale.core.baseclasses.BaseEnumeration.printdoc" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.EnumerationWithValue">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.</tt><tt class="descname">EnumerationWithValue</tt><big>(</big><em>value</em>, <em>doc=None</em><big>)</big><a class="headerlink" href="#JumpScale.core.baseclasses.EnumerationWithValue" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <a class="reference internal" href="#JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration" title="JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration"><tt class="xref py py-class docutils literal"><span class="pre">JumpScale.core.baseclasses.BaseEnumeration.BaseEnumeration</span></tt></a></p>
   <p>Enumeration base type providing separation between item name and value</p>
   <p>Since some names (which are invalid Python identifiers) are forbidden as
   enumeration item name, this class provides separation between item names
   and item value (which is the value returned by __str__, equal to name in
   the basic Enumeration type).</p>
   <p>Next to this, it offers a &#8216;doc&#8217; attribute which is returned by __repr__.</p>
   <p>Example use case: the VirtualboxNicType enumeration contains an item which
   should be called &#8216;82540EM&#8217;. This is an invalid identifier, so it had to be
   renamed to &#8216;I82540EM&#8217; as name. We still want to provide the original value
   as well though.
   Next to this, &#8216;82540EM&#8217; is not easy to understand, so we want to represent
   the item as &#8216;Intel PRO/1000MT Desktop&#8217; to the end-user, which is the doc
   property displayed by __repr__.</p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.core.baseclasses.BaseType">
   <em class="property">class </em><tt class="descclassname">JumpScale.core.baseclasses.</tt><tt class="descname">BaseType</tt><a class="headerlink" href="#JumpScale.core.baseclasses.BaseType" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
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
   <li><a class="reference internal" href="#">JumpScale.core.baseclasses package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.baseclasses.BaseEnumeration">JumpScale.core.baseclasses.BaseEnumeration module</a><ul>
   <li><a class="reference internal" href="#enumeration-lifecycle">Enumeration lifecycle</a><ul>
   <li><a class="reference internal" href="#enumeration-definition">Enumeration definition</a></li>
   <li><a class="reference internal" href="#baseenumerationmeta-magic">BaseEnumerationMeta magic</a></li>
   <li><a class="reference internal" href="#lazy-loading-pitfalls-and-type-caching">Lazy loading pitfalls and type caching</a></li>
   <li><a class="reference internal" href="#when-even-caching-becomes-complicated">When even caching becomes complicated</a></li>
   <li><a class="reference internal" href="#the-story-of-intermediate-classes">The story of intermediate classes</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li><a class="reference internal" href="#module-JumpScale.core.baseclasses.BaseType">JumpScale.core.baseclasses.BaseType module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.baseclasses.dirtyflaggingmixin">JumpScale.core.baseclasses.dirtyflaggingmixin module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.core.baseclasses">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.core.base.time.html"
                           title="previous chapter">JumpScale.core.base.time package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.core.config.html"
                           title="next chapter">JumpScale.core.config package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.core.baseclasses.txt"
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
             <a href="JumpScale.core.config.html" title="JumpScale.core.config package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.core.base.time.html" title="JumpScale.core.base.time package"
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
       <li><a href="../_sources/API/JumpScale.core.baseclasses.txt"
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