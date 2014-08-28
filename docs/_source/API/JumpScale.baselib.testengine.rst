.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.testengine package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.units package" href="JumpScale.baselib.units.html" />
       <link rel="prev" title="JumpScale.baselib.taskletengine package" href="JumpScale.baselib.taskletengine.html" /> 
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
             <a href="JumpScale.baselib.units.html" title="JumpScale.baselib.units package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.taskletengine.html" title="JumpScale.baselib.taskletengine package"
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
               
     <div class="section" id="jumpscale-baselib-testengine-package">
   <h1>JumpScale.baselib.testengine package<a class="headerlink" href="#jumpscale-baselib-testengine-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.testengine.TestEngine">
   <span id="jumpscale-baselib-testengine-testengine-module"></span><h2>JumpScale.baselib.testengine.TestEngine module<a class="headerlink" href="#module-JumpScale.baselib.testengine.TestEngine" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngine.FakeTestObj">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngine.</tt><tt class="descname">FakeTestObj</tt><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#FakeTestObj"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.FakeTestObj" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngine.Tee">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngine.</tt><tt class="descname">Tee</tt><big>(</big><em>*fobjs</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#Tee"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.Tee" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.Tee.flush">
   <tt class="descname">flush</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#Tee.flush"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.Tee.flush" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.Tee.write">
   <tt class="descname">write</tt><big>(</big><em>data</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#Tee.write"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.Tee.write" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngine.Test">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngine.</tt><tt class="descname">Test</tt><big>(</big><em>db</em>, <em>testmodule</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#Test"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.Test" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.Test.execute">
   <tt class="descname">execute</tt><big>(</big><em>testrunname</em>, <em>debug=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#Test.execute"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.Test.execute" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestEngine">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngine.</tt><tt class="descname">TestEngine</tt><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestEngine"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestEngine" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestEngine.initTests">
   <tt class="descname">initTests</tt><big>(</big><em>noOsis</em>, <em>osisip='127.0.0.1'</em>, <em>login=''</em>, <em>passwd=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestEngine.initTests"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestEngine.initTests" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestEngine.runTests">
   <tt class="descname">runTests</tt><big>(</big><em>testrunname=None</em>, <em>debug=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestEngine.runTests"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestEngine.runTests" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestEngine.testFile">
   <tt class="descname">testFile</tt><big>(</big><em>testrunname</em>, <em>filepath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestEngine.testFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestEngine.testFile" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngine.</tt><tt class="descname">TestResult</tt><big>(</big><em>debug=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">unittest.result.TestResult</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.addError">
   <tt class="descname">addError</tt><big>(</big><em>test</em>, <em>err</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.addError"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.addError" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.addFailure">
   <tt class="descname">addFailure</tt><big>(</big><em>test</em>, <em>err</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.addFailure"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.addFailure" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.addSkip">
   <tt class="descname">addSkip</tt><big>(</big><em>test</em>, <em>reason</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.addSkip"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.addSkip" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.addSuccess">
   <tt class="descname">addSuccess</tt><big>(</big><em>test</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.addSuccess"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.addSuccess" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.printStatus">
   <tt class="descname">printStatus</tt><big>(</big><em>test</em>, <em>state=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.printStatus"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.printStatus" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.startTest">
   <tt class="descname">startTest</tt><big>(</big><em>test</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.startTest"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.startTest" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngine.TestResult.stopTest">
   <tt class="descname">stopTest</tt><big>(</big><em>test</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngine.html#TestResult.stopTest"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngine.TestResult.stopTest" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.testengine.TestEngineKds">
   <span id="jumpscale-baselib-testengine-testenginekds-module"></span><h2>JumpScale.baselib.testengine.TestEngineKds module<a class="headerlink" href="#module-JumpScale.baselib.testengine.TestEngineKds" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.FileLikeStreamObject">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngineKds.</tt><tt class="descname">FileLikeStreamObject</tt><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#FileLikeStreamObject"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.FileLikeStreamObject" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.FileLikeStreamObject.write">
   <tt class="descname">write</tt><big>(</big><em>buf</em>, <em>**args</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#FileLikeStreamObject.write"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.FileLikeStreamObject.write" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.Test">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngineKds.</tt><tt class="descname">Test</tt><big>(</big><em>db</em>, <em>testclass</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#Test"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.Test" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.Test.execute">
   <tt class="descname">execute</tt><big>(</big><em>testrunname</em>, <em>debug=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#Test.execute"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.Test.execute" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.TestEngineKds">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.testengine.TestEngineKds.</tt><tt class="descname">TestEngineKds</tt><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#TestEngineKds"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.TestEngineKds" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.TestEngineKds.initTests">
   <tt class="descname">initTests</tt><big>(</big><em>osisip='127.0.0.1'</em>, <em>login=''</em>, <em>passwd=''</em>, <em>noOsis=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#TestEngineKds.initTests"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.TestEngineKds.initTests" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.testengine.TestEngineKds.TestEngineKds.runTests">
   <tt class="descname">runTests</tt><big>(</big><em>testrunname=None</em>, <em>debug=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/testengine/TestEngineKds.html#TestEngineKds.runTests"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.testengine.TestEngineKds.TestEngineKds.runTests" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.testengine">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.testengine" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.testengine package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.testengine.TestEngine">JumpScale.baselib.testengine.TestEngine module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.testengine.TestEngineKds">JumpScale.baselib.testengine.TestEngineKds module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.testengine">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.taskletengine.html"
                           title="previous chapter">JumpScale.baselib.taskletengine package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.units.html"
                           title="next chapter">JumpScale.baselib.units package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.testengine.txt"
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
             <a href="JumpScale.baselib.units.html" title="JumpScale.baselib.units package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.taskletengine.html" title="JumpScale.baselib.taskletengine package"
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