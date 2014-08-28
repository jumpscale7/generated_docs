.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.netconfig package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.params package" href="JumpScale.baselib.params.html" />
       <link rel="prev" title="JumpScale.baselib.mercurial.hglib package" href="JumpScale.baselib.mercurial.hglib.html" /> 
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
             <a href="JumpScale.baselib.params.html" title="JumpScale.baselib.params package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.mercurial.hglib.html" title="JumpScale.baselib.mercurial.hglib package"
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
               
     <div class="section" id="jumpscale-baselib-netconfig-package">
   <h1>JumpScale.baselib.netconfig package<a class="headerlink" href="#jumpscale-baselib-netconfig-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.netconfig.Netconfig">
   <span id="jumpscale-baselib-netconfig-netconfig-module"></span><h2>JumpScale.baselib.netconfig.Netconfig module<a class="headerlink" href="#module-JumpScale.baselib.netconfig.Netconfig" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.netconfig.Netconfig.</tt><tt class="descname">Netconfig</tt><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.addIpToInterface">
   <tt class="descname">addIpToInterface</tt><big>(</big><em>dev</em>, <em>ipaddr</em>, <em>aliasnr=1</em>, <em>start=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.addIpToInterface"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.addIpToInterface" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterface">
   <tt class="descname">enableInterface</tt><big>(</big><em>dev='eth0'</em>, <em>start=False</em>, <em>dhcp=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.enableInterface"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterface" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceBridgeDhcp">
   <tt class="descname">enableInterfaceBridgeDhcp</tt><big>(</big><em>dev</em>, <em>bridgedev</em>, <em>start=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.enableInterfaceBridgeDhcp"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceBridgeDhcp" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceBridgeStatic">
   <tt class="descname">enableInterfaceBridgeStatic</tt><big>(</big><em>dev</em>, <em>ipaddr=None</em>, <em>bridgedev=None</em>, <em>gw=None</em>, <em>start=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.enableInterfaceBridgeStatic"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceBridgeStatic" title="Permalink to this definition">¶</a></dt>
   <dd><p>ipaddr in form of 192.168.10.2/24 (can be list)
   gateway in form of 192.168.10.254</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceStatic">
   <tt class="descname">enableInterfaceStatic</tt><big>(</big><em>dev</em>, <em>ipaddr</em>, <em>gw=None</em>, <em>start=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.enableInterfaceStatic"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.enableInterfaceStatic" title="Permalink to this definition">¶</a></dt>
   <dd><p>ipaddr in form of 192.168.10.2/24 (can be list)
   gateway in form of 192.168.10.254</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.remove">
   <tt class="descname">remove</tt><big>(</big><em>dev</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.remove"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.remove" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.reset">
   <tt class="descname">reset</tt><big>(</big><em>shutdown=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.reset"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.reset" title="Permalink to this definition">¶</a></dt>
   <dd><p>empty config of /etc/network/interfaces</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.setNameserver">
   <tt class="descname">setNameserver</tt><big>(</big><em>addr</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.setNameserver"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.setNameserver" title="Permalink to this definition">¶</a></dt>
   <dd><p>resolvconf will be disabled</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.setRoot">
   <tt class="descname">setRoot</tt><big>(</big><em>root</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.setRoot"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.setRoot" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.netconfig.Netconfig.Netconfig.shutdownNetwork">
   <tt class="descname">shutdownNetwork</tt><big>(</big><em>excludes=</em><span class="optional">[</span><span class="optional">]</span><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/netconfig/Netconfig.html#Netconfig.shutdownNetwork"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.netconfig.Netconfig.Netconfig.shutdownNetwork" title="Permalink to this definition">¶</a></dt>
   <dd><p>find all interfaces and shut them all down with ifdown
   this is to remove all networking things going on</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.netconfig">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.netconfig" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.netconfig package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.netconfig.Netconfig">JumpScale.baselib.netconfig.Netconfig module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.netconfig">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.mercurial.hglib.html"
                           title="previous chapter">JumpScale.baselib.mercurial.hglib package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.params.html"
                           title="next chapter">JumpScale.baselib.params package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.netconfig.txt"
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
             <a href="JumpScale.baselib.params.html" title="JumpScale.baselib.params package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.mercurial.hglib.html" title="JumpScale.baselib.mercurial.hglib package"
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