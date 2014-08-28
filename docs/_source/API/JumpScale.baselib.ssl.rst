.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.ssl package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.startupmanager package" href="JumpScale.baselib.startupmanager.html" />
       <link rel="prev" title="JumpScale.baselib.specparser package" href="JumpScale.baselib.specparser.html" /> 
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
             <a href="JumpScale.baselib.startupmanager.html" title="JumpScale.baselib.startupmanager package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.specparser.html" title="JumpScale.baselib.specparser package"
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
               
     <div class="section" id="jumpscale-baselib-ssl-package">
   <h1>JumpScale.baselib.ssl package<a class="headerlink" href="#jumpscale-baselib-ssl-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.ssl.SSL">
   <span id="jumpscale-baselib-ssl-ssl-module"></span><h2>JumpScale.baselib.ssl.SSL module<a class="headerlink" href="#module-JumpScale.baselib.ssl.SSL" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.ssl.SSL.</tt><tt class="descname">KeyStor</tt><big>(</big><em>keyvaluestor=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.createKeyPair">
   <tt class="descname">createKeyPair</tt><big>(</big><em>organization=''</em>, <em>user=''</em>, <em>path=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.createKeyPair"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.createKeyPair" title="Permalink to this definition">¶</a></dt>
   <dd><p>creates keypairs &amp; stores in localdb
   &#64;return (priv,pub) keys</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.decrypt">
   <tt class="descname">decrypt</tt><big>(</big><em>orgsender</em>, <em>sender</em>, <em>orgreader</em>, <em>reader</em>, <em>message</em>, <em>signature=None</em>, <em>base64=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.decrypt"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.decrypt" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.encrypt">
   <tt class="descname">encrypt</tt><big>(</big><em>orgsender</em>, <em>sender</em>, <em>orgreader</em>, <em>reader</em>, <em>message</em>, <em>sign=True</em>, <em>base64=True</em>, <em>pubkeyReader=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.encrypt"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.encrypt" title="Permalink to this definition">¶</a></dt>
   <dd><p>&#64;param sender, name of person sending
   &#64;param name of person reading
   &#64;return encryptedtext,signature</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.getPrivKey">
   <tt class="descname">getPrivKey</tt><big>(</big><em>organization</em>, <em>user</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.getPrivKey"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.getPrivKey" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.getPubKey">
   <tt class="descname">getPubKey</tt><big>(</big><em>organization</em>, <em>user</em>, <em>returnAsString=False</em>, <em>pubkeyReader=''</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.getPubKey"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.getPubKey" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.perftest">
   <tt class="descname">perftest</tt><big>(</big><em>nrrounds=1000</em>, <em>sign=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.perftest"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.perftest" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.setPubKey">
   <tt class="descname">setPubKey</tt><big>(</big><em>organization</em>, <em>user</em>, <em>pemstr</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.setPubKey"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.setPubKey" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.KeyStor.test">
   <tt class="descname">test</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#KeyStor.test"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.KeyStor.test" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   <dl class="class">
   <dt id="JumpScale.baselib.ssl.SSL.SSL">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.ssl.SSL.</tt><tt class="descname">SSL</tt><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#SSL"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.SSL" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.ssl.SSL.SSL.getSSLHandler">
   <tt class="descname">getSSLHandler</tt><big>(</big><em>keyvaluestor=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#SSL.getSSLHandler"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.SSL.getSSLHandler" title="Permalink to this definition">¶</a></dt>
   <dd><p>default keyvaluestor=j.db.keyvaluestore.getFileSystemStore(&#8220;sslkeys&#8221;, serializers=[])  #make sure to use no serializers
   pass another keyvaluestor if required (first do &#8216;import JumpScale.baselib.key_value_store&#8217;)</p>
   </dd></dl>
   
   </dd></dl>
   
   <dl class="function">
   <dt id="JumpScale.baselib.ssl.SSL.empty_callback">
   <tt class="descclassname">JumpScale.baselib.ssl.SSL.</tt><tt class="descname">empty_callback</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/ssl/SSL.html#empty_callback"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.ssl.SSL.empty_callback" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.ssl">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.ssl" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.ssl package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.ssl.SSL">JumpScale.baselib.ssl.SSL module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.ssl">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.specparser.html"
                           title="previous chapter">JumpScale.baselib.specparser package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.startupmanager.html"
                           title="next chapter">JumpScale.baselib.startupmanager package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.ssl.txt"
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
             <a href="JumpScale.baselib.startupmanager.html" title="JumpScale.baselib.startupmanager package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.specparser.html" title="JumpScale.baselib.specparser package"
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