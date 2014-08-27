.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.actions.transaction package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="up" title="JumpScale.baselib.actions package" href="JumpScale.baselib.actions.html" />
       <link rel="next" title="JumpScale.baselib.admin package" href="JumpScale.baselib.admin.html" />
       <link rel="prev" title="JumpScale.baselib.actions.action package" href="JumpScale.baselib.actions.action.html" /> 
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
             <a href="JumpScale.baselib.admin.html" title="JumpScale.baselib.admin package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.actions.action.html" title="JumpScale.baselib.actions.action package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" >JumpScale.baselib package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.actions.html" accesskey="U">JumpScale.baselib.actions package</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <div class="section" id="jumpscale-baselib-actions-transaction-package">
   <h1>JumpScale.baselib.actions.transaction package<a class="headerlink" href="#jumpscale-baselib-actions-transaction-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.actions.transaction.Transaction">
   <span id="jumpscale-baselib-actions-transaction-transaction-module"></span><h2>JumpScale.baselib.actions.transaction.Transaction module<a class="headerlink" href="#module-JumpScale.baselib.actions.transaction.Transaction" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.actions.transaction.Transaction.Transaction">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.actions.transaction.Transaction.</tt><tt class="descname">Transaction</tt><big>(</big><em>description</em>, <em>errormessage</em>, <em>resolutionmessage</em>, <em>callback=None</em>, <em>callbackparams=None</em>, <em>maxloglevel=2</em>, <em>maxloglevelcapture=5</em>, <em>silent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/Transaction.html#Transaction"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.Transaction.Transaction" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Representation of an transaction
   &#64;property errorcallback: std None, is function which will be called when error happens in this transaction
   &#64;property logs : logs captured since start of transaction</p>
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.Transaction.Transaction.getErrorMessage">
   <tt class="descname">getErrorMessage</tt><big>(</big><em>withloginfo=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/Transaction.html#Transaction.getErrorMessage"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.Transaction.Transaction.getErrorMessage" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.Transaction.Transaction.getLog">
   <tt class="descname">getLog</tt><big>(</big><em>maxLevel=9</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/Transaction.html#Transaction.getLog"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.Transaction.Transaction.getLog" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.actions.transaction.TransactionController">
   <span id="jumpscale-baselib-actions-transaction-transactioncontroller-module"></span><h2>JumpScale.baselib.actions.transaction.TransactionController module<a class="headerlink" href="#module-JumpScale.baselib.actions.transaction.TransactionController" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.actions.transaction.TransactionController.</tt><tt class="descname">TransactionController</tt><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <p>Manager controlling actions
   Transactions = jumpscale transactions
   see <a class="reference external" href="mailto:#&#37;&#52;&#48;todo">#<span>&#64;</span>todo</a> doc on jumpscale
   &#64;property transactions: array of transactions 
   &#64;property width: Maximum width of output
   &#64;property maxloglevel : max loglevel which will be captured (default for all transactions)
   for more info see: <a class="reference external" href="http://www.jumpscale.org/display/PM/Transactions">http://www.jumpscale.org/display/PM/Transactions</a></p>
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.clean">
   <tt class="descname">clean</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.clean"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.clean" title="Permalink to this definition">¶</a></dt>
   <dd><p>Clean the list of running actions</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.hasRunningTransactions">
   <tt class="descname">hasRunningTransactions</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.hasRunningTransactions"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.hasRunningTransactions" title="Permalink to this definition">¶</a></dt>
   <dd><p>Check whether actions are currently running
   &#64;returns: Whether actions are runnin</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.hide">
   <tt class="descname">hide</tt><big>(</big><em>maxloglevel</em>, <em>callback</em>, <em>callbackparams</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.hide"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.hide" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.start">
   <tt class="descname">start</tt><big>(</big><em>description</em>, <em>errormessage=None</em>, <em>resolutionmessage=None</em>, <em>maxloglevel=2</em>, <em>maxloglevelcapture=5</em>, <em>callback=None</em>, <em>callbackparams=None</em>, <em>silent=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.start"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.start" title="Permalink to this definition">¶</a></dt>
   <dd><p>Start a new transaction and return the transaction</p>
   <p>&#64;param description: Description of the transaction
   &#64;param errormessage: Error message displayed to the user when the transaction fails
   &#64;param resolutionmessage: Resolution message displayed to the user when the transaction fails
   &#64;param maxloglevel specify which logs with max level should be remembered when doing the transaction
   &#64;param callback can use this to provide a sort of rollback mechanism to e.g. cleanup a state
   &#64;param callbackparams dict of parameters</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.stop">
   <tt class="descname">stop</tt><big>(</big><em>failed=False</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.stop"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.stop" title="Permalink to this definition">¶</a></dt>
   <dd><p>Stop the currently running transaction</p>
   <p>This will get the latest started transaction from the transaction stack and
   display status
   &#64;param failed, used when error is raised by errorconditionhanlder</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.actions.transaction.TransactionController.TransactionController.stopall">
   <tt class="descname">stopall</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/actions/transaction/TransactionController.html#TransactionController.stopall"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.actions.transaction.TransactionController.TransactionController.stopall" title="Permalink to this definition">¶</a></dt>
   <dd><p>stop all transaction</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.actions.transaction">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.actions.transaction" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.actions.transaction package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.actions.transaction.Transaction">JumpScale.baselib.actions.transaction.Transaction module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.actions.transaction.TransactionController">JumpScale.baselib.actions.transaction.TransactionController module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.actions.transaction">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.actions.action.html"
                           title="previous chapter">JumpScale.baselib.actions.action package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.admin.html"
                           title="next chapter">JumpScale.baselib.admin package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.actions.transaction.txt"
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
             <a href="JumpScale.baselib.admin.html" title="JumpScale.baselib.admin package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.actions.action.html" title="JumpScale.baselib.actions.action package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.html" >JumpScale.baselib package</a> &raquo;</li>
             <li><a href="JumpScale.baselib.actions.html" >JumpScale.baselib.actions package</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>