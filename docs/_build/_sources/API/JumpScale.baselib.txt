.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="up" title="JumpScale package" href="JumpScale.html" />
       <link rel="next" title="JumpScale.baselib.actions package" href="JumpScale.baselib.actions.html" />
       <link rel="prev" title="JumpScale.base package" href="JumpScale.base.html" /> 
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
             <a href="JumpScale.baselib.actions.html" title="JumpScale.baselib.actions package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.base.html" title="JumpScale.base package"
                accesskey="P">previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" accesskey="U">JumpScale package</a> &raquo;</li> 
         </ul>
       </div>  
   
       <div class="document">
         <div class="documentwrapper">
           <div class="bodywrapper">
             <div class="body">
               
     <div class="section" id="jumpscale-baselib-package">
   <h1>JumpScale.baselib package<a class="headerlink" href="#jumpscale-baselib-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="subpackages">
   <h2>Subpackages<a class="headerlink" href="#subpackages" title="Permalink to this headline">¶</a></h2>
   <div class="toctree-wrapper compound">
   <ul>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.actions.html">JumpScale.baselib.actions package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.actions.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.actions.action.html">JumpScale.baselib.actions.action package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.action.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.action.html#module-JumpScale.baselib.actions.action.ActionController">JumpScale.baselib.actions.action.ActionController module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.action.html#module-JumpScale.baselib.actions.action.RunningAction">JumpScale.baselib.actions.action.RunningAction module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.action.html#module-JumpScale.baselib.actions.action">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.actions.transaction.html">JumpScale.baselib.actions.transaction package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.transaction.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.transaction.html#module-JumpScale.baselib.actions.transaction.Transaction">JumpScale.baselib.actions.transaction.Transaction module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.transaction.html#module-JumpScale.baselib.actions.transaction.TransactionController">JumpScale.baselib.actions.transaction.TransactionController module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.actions.transaction.html#module-JumpScale.baselib.actions.transaction">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.actions.html#module-JumpScale.baselib.actions">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.admin.html">JumpScale.baselib.admin package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.admin.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.admin.html#module-JumpScale.baselib.admin.Admin">JumpScale.baselib.admin.Admin module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.admin.html#module-JumpScale.baselib.admin">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.backup.html">JumpScale.baselib.backup package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backup.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backup.html#jumpscale-baselib-backup-backupclient-module">JumpScale.baselib.backup.BackupClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backup.html#jumpscale-baselib-backup-backupfactory-module">JumpScale.baselib.backup.BackupFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backup.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.backuptools.html">JumpScale.baselib.backuptools package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backuptools.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backuptools.html#module-JumpScale.baselib.backuptools.backup">JumpScale.baselib.backuptools.backup module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backuptools.html#jumpscale-baselib-backuptools-object-store-module">JumpScale.baselib.backuptools.object_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.backuptools.html#module-JumpScale.baselib.backuptools">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.bitbucket.html">JumpScale.baselib.bitbucket package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.bitbucket.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.bitbucket.html#module-JumpScale.baselib.bitbucket.Bitbucket">JumpScale.baselib.bitbucket.Bitbucket module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.bitbucket.html#module-JumpScale.baselib.bitbucket.BitbucketConfigManagement">JumpScale.baselib.bitbucket.BitbucketConfigManagement module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.bitbucket.html#module-JumpScale.baselib.bitbucket.BitbucketInterface">JumpScale.baselib.bitbucket.BitbucketInterface module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.bitbucket.html#module-JumpScale.baselib.bitbucket">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.blobstor.html">JumpScale.baselib.blobstor package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor.html#module-JumpScale.baselib.blobstor.BlobStor">JumpScale.baselib.blobstor.BlobStor module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor.html#module-JumpScale.baselib.blobstor.BlobStorConfigManagement">JumpScale.baselib.blobstor.BlobStorConfigManagement module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor.html#module-JumpScale.baselib.blobstor">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.blobstor2.html">JumpScale.baselib.blobstor2 package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorclient-module">JumpScale.baselib.blobstor2.BlobStorClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorfactory-module">JumpScale.baselib.blobstor2.BlobStorFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstormaster-module">JumpScale.baselib.blobstor2.BlobStorMaster module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorserver-module">JumpScale.baselib.blobstor2.BlobStorServer module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorserverold-module">JumpScale.baselib.blobstor2.BlobStorServerOld module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorserversimple-module">JumpScale.baselib.blobstor2.BlobStorServerSimple module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#jumpscale-baselib-blobstor2-blobstorworker-module">JumpScale.baselib.blobstor2.BlobStorWorker module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.blobstor2.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.changetracker.html">JumpScale.baselib.changetracker package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.changetracker.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.changetracker.html#jumpscale-baselib-changetracker-changetrackerclient-module">JumpScale.baselib.changetracker.ChangeTrackerClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.changetracker.html#jumpscale-baselib-changetracker-changetrackerfactory-module">JumpScale.baselib.changetracker.ChangeTrackerFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.changetracker.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html">JumpScale.baselib.cloudsystemfs package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.CifsFS">JumpScale.baselib.cloudsystemfs.CifsFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.CloudSystemFS">JumpScale.baselib.cloudsystemfs.CloudSystemFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.FileFS">JumpScale.baselib.cloudsystemfs.FileFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.FtpFS">JumpScale.baselib.cloudsystemfs.FtpFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.HttpFS">JumpScale.baselib.cloudsystemfs.HttpFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs.SshFS">JumpScale.baselib.cloudsystemfs.SshFS module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cloudsystemfs.html#module-JumpScale.baselib.cloudsystemfs">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.cmdline.html">JumpScale.baselib.cmdline package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cmdline.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cmdline.html#module-JumpScale.baselib.cmdline.CommandLauncher">JumpScale.baselib.cmdline.CommandLauncher module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cmdline.html#module-JumpScale.baselib.cmdline.Options">JumpScale.baselib.cmdline.Options module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cmdline.html#module-JumpScale.baselib.cmdline">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.cmdutils.html">JumpScale.baselib.cmdutils package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.cmdutils.html#module-JumpScale.baselib.cmdutils">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.code.html">JumpScale.baselib.code package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.code.cmdutils.html">JumpScale.baselib.code.cmdutils package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.code.cmdutils.html#module-JumpScale.baselib.code.cmdutils">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code.Appserver6GreenletBase">JumpScale.baselib.code.Appserver6GreenletBase module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code.Appserver6GreenletScheduleBase">JumpScale.baselib.code.Appserver6GreenletScheduleBase module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code.Appserver6GreenletTaskletsBase">JumpScale.baselib.code.Appserver6GreenletTaskletsBase module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code.ClassBase">JumpScale.baselib.code.ClassBase module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code.Code">JumpScale.baselib.code.Code module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.code.html#module-JumpScale.baselib.code">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.codeexecutor.html">JumpScale.baselib.codeexecutor package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codeexecutor.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codeexecutor.html#module-JumpScale.baselib.codeexecutor.CodeExecutor">JumpScale.baselib.codeexecutor.CodeExecutor module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codeexecutor.html#module-JumpScale.baselib.codeexecutor">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.codetools.html">JumpScale.baselib.codetools package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.ClassDef">JumpScale.baselib.codetools.ClassDef module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.CodeElements">JumpScale.baselib.codetools.CodeElements module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.CodeManager">JumpScale.baselib.codetools.CodeManager module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.CodeTools">JumpScale.baselib.codetools.CodeTools module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.MethodDef">JumpScale.baselib.codetools.MethodDef module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.PropertyDef">JumpScale.baselib.codetools.PropertyDef module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.RegexTools">JumpScale.baselib.codetools.RegexTools module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.TemplateEngine">JumpScale.baselib.codetools.TemplateEngine module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.TemplateEngineWrapper">JumpScale.baselib.codetools.TemplateEngineWrapper module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.TextCharEditor">JumpScale.baselib.codetools.TextCharEditor module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.TextFileEditor">JumpScale.baselib.codetools.TextFileEditor module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.TextLineEditor">JumpScale.baselib.codetools.TextLineEditor module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools.WordReplacer">JumpScale.baselib.codetools.WordReplacer module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.codetools.html#module-JumpScale.baselib.codetools">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.credis.html">JumpScale.baselib.credis package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.credis.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.credis.html#module-JumpScale.baselib.credis.CRedis">JumpScale.baselib.credis.CRedis module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.credis.html#module-JumpScale.baselib.credis.CRedisQueue">JumpScale.baselib.credis.CRedisQueue module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.credis.html#module-JumpScale.baselib.credis">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.dnsmasq.html">JumpScale.baselib.dnsmasq package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.dnsmasq.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.dnsmasq.html#module-JumpScale.baselib.dnsmasq.dnsmasq">JumpScale.baselib.dnsmasq.dnsmasq module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.dnsmasq.html#module-JumpScale.baselib.dnsmasq">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.elasticsearch.html">JumpScale.baselib.elasticsearch package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.elasticsearch.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.elasticsearch.html#module-JumpScale.baselib.elasticsearch.Elasticsearch">JumpScale.baselib.elasticsearch.Elasticsearch module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.elasticsearch.html#module-JumpScale.baselib.elasticsearch">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.expect.html">JumpScale.baselib.expect package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.expect.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.expect.html#module-JumpScale.baselib.expect.Expect">JumpScale.baselib.expect.Expect module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.expect.html#module-JumpScale.baselib.expect">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.git.html">JumpScale.baselib.git package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.git.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.git.html#module-JumpScale.baselib.git.GitClient">JumpScale.baselib.git.GitClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.git.html#module-JumpScale.baselib.git.GitFactory">JumpScale.baselib.git.GitFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.git.html#module-JumpScale.baselib.git">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.github.html">JumpScale.baselib.github package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.github.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.github.html#module-JumpScale.baselib.github.github">JumpScale.baselib.github.github module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.github.html#module-JumpScale.baselib.github">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.gitlab.html">JumpScale.baselib.gitlab package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.gitlab.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.gitlab.gitlab.html">JumpScale.baselib.gitlab.gitlab package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.gitlab.gitlab.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.gitlab.gitlab.html#module-JumpScale.baselib.gitlab.gitlab.exceptions">JumpScale.baselib.gitlab.gitlab.exceptions module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.gitlab.gitlab.html#module-JumpScale.baselib.gitlab.gitlab">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.gitlab.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.gitlab.html#module-JumpScale.baselib.gitlab.GitlabFactory">JumpScale.baselib.gitlab.GitlabFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.gitlab.html#module-JumpScale.baselib.gitlab.GitlabInstance">JumpScale.baselib.gitlab.GitlabInstance module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.gitlab.html#module-JumpScale.baselib.gitlab">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.graphite.html">JumpScale.baselib.graphite package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.graphite.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.graphite.html#module-JumpScale.baselib.graphite.GraphiteClient">JumpScale.baselib.graphite.GraphiteClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.graphite.html#module-JumpScale.baselib.graphite">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.hash.html">JumpScale.baselib.hash package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hash.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hash.html#module-JumpScale.baselib.hash.HashTool">JumpScale.baselib.hash.HashTool module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hash.html#module-JumpScale.baselib.hash">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.hrd.html">JumpScale.baselib.hrd package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hrd.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hrd.html#module-JumpScale.baselib.hrd.HumanReadableData">JumpScale.baselib.hrd.HumanReadableData module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.hrd.html#module-JumpScale.baselib.hrd">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.http_client.html">JumpScale.baselib.http_client package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.http_client.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.http_client.httplib2.html">JumpScale.baselib.http_client.httplib2 package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.http_client.httplib2.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.http_client.httplib2.html#module-JumpScale.baselib.http_client.httplib2.iri2uri">JumpScale.baselib.http_client.httplib2.iri2uri module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.http_client.httplib2.html#module-JumpScale.baselib.http_client.httplib2.socks">JumpScale.baselib.http_client.httplib2.socks module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.http_client.httplib2.html#module-JumpScale.baselib.http_client.httplib2">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.http_client.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.http_client.html#module-JumpScale.baselib.http_client.HttpClient">JumpScale.baselib.http_client.HttpClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.http_client.html#module-JumpScale.baselib.http_client">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.influxdb.html">JumpScale.baselib.influxdb package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.influxdb.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.influxdb.html#module-JumpScale.baselib.influxdb.Influxdb">JumpScale.baselib.influxdb.Influxdb module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.influxdb.html#module-JumpScale.baselib.influxdb">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.inifile.html">JumpScale.baselib.inifile package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.inifile.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.inifile.html#module-JumpScale.baselib.inifile.IniFile">JumpScale.baselib.inifile.IniFile module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.inifile.html#module-JumpScale.baselib.inifile">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.installtools.html">JumpScale.baselib.installtools package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.installtools.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.installtools.html#module-JumpScale.baselib.installtools.InstallTools">JumpScale.baselib.installtools.InstallTools module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.installtools.html#module-JumpScale.baselib.installtools">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.jpackages.html">JumpScale.baselib.jpackages package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.ActionManager">JumpScale.baselib.jpackages.ActionManager module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.CodeManagementRecipe">JumpScale.baselib.jpackages.CodeManagementRecipe module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.Domain">JumpScale.baselib.jpackages.Domain module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.JPackageClient">JumpScale.baselib.jpackages.JPackageClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.JPackageObject">JumpScale.baselib.jpackages.JPackageObject module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.JPackageStateObject">JumpScale.baselib.jpackages.JPackageStateObject module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.JPackagesGenDocs">JumpScale.baselib.jpackages.JPackagesGenDocs module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.PythonPackage">JumpScale.baselib.jpackages.PythonPackage module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.ReleaseMgmt">JumpScale.baselib.jpackages.ReleaseMgmt module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages.enumerators4">JumpScale.baselib.jpackages.enumerators4 module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jpackages.html#module-JumpScale.baselib.jpackages">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.jsdeveltools.html">JumpScale.baselib.jsdeveltools package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jsdeveltools.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jsdeveltools.html#jumpscale-baselib-jsdeveltools-jsdeveltools-module">JumpScale.baselib.jsdeveltools.JSDevelTools module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jsdeveltools.html#jumpscale-baselib-jsdeveltools-jsdeveltoolsinstaller-module">JumpScale.baselib.jsdeveltools.JSDevelToolsInstaller module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.jsdeveltools.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.key_value_store.html">JumpScale.baselib.key_value_store package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.arakoon_store">JumpScale.baselib.key_value_store.arakoon_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.file_system_store">JumpScale.baselib.key_value_store.file_system_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#jumpscale-baselib-key-value-store-leveldb-store-module">JumpScale.baselib.key_value_store.leveldb_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.memory_store">JumpScale.baselib.key_value_store.memory_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.mongodb_store">JumpScale.baselib.key_value_store.mongodb_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.redis_store">JumpScale.baselib.key_value_store.redis_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.store">JumpScale.baselib.key_value_store.store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store.store_factory">JumpScale.baselib.key_value_store.store_factory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#jumpscale-baselib-key-value-store-test-store-module">JumpScale.baselib.key_value_store.test_store module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.key_value_store.html#module-JumpScale.baselib.key_value_store">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.lrucache.html">JumpScale.baselib.lrucache package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.lrucache.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.lrucache.html#module-JumpScale.baselib.lrucache.LRUCache">JumpScale.baselib.lrucache.LRUCache module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.lrucache.html#module-JumpScale.baselib.lrucache.LRUCacheFactory">JumpScale.baselib.lrucache.LRUCacheFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.lrucache.html#module-JumpScale.baselib.lrucache.RWCache">JumpScale.baselib.lrucache.RWCache module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.lrucache.html#module-JumpScale.baselib.lrucache">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.mailclient.html">JumpScale.baselib.mailclient package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mailclient.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mailclient.html#module-JumpScale.baselib.mailclient.emailclient">JumpScale.baselib.mailclient.emailclient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mailclient.html#module-JumpScale.baselib.mailclient">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.manage.html">JumpScale.baselib.manage package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.manage.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.manage.html#module-JumpScale.baselib.manage.managerbase">JumpScale.baselib.manage.managerbase module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.manage.html#module-JumpScale.baselib.manage">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.mercurial.html">JumpScale.baselib.mercurial package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mercurial.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html">JumpScale.baselib.mercurial.hglib package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.client">JumpScale.baselib.mercurial.hglib.client module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.context">JumpScale.baselib.mercurial.hglib.context module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.error">JumpScale.baselib.mercurial.hglib.error module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.merge">JumpScale.baselib.mercurial.hglib.merge module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.templates">JumpScale.baselib.mercurial.hglib.templates module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib.util">JumpScale.baselib.mercurial.hglib.util module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.mercurial.hglib.html#module-JumpScale.baselib.mercurial.hglib">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mercurial.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mercurial.html#module-JumpScale.baselib.mercurial.HgLibClient">JumpScale.baselib.mercurial.HgLibClient module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mercurial.html#module-JumpScale.baselib.mercurial.HgLibFactory">JumpScale.baselib.mercurial.HgLibFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.mercurial.html#module-JumpScale.baselib.mercurial">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.netconfig.html">JumpScale.baselib.netconfig package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.netconfig.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.netconfig.html#module-JumpScale.baselib.netconfig.Netconfig">JumpScale.baselib.netconfig.Netconfig module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.netconfig.html#module-JumpScale.baselib.netconfig">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.params.html">JumpScale.baselib.params package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.params.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.params.html#module-JumpScale.baselib.params.Params">JumpScale.baselib.params.Params module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.params.html#module-JumpScale.baselib.params">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.performancetrace.html">JumpScale.baselib.performancetrace package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.performancetrace.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.performancetrace.html#module-JumpScale.baselib.performancetrace.PerformanceTrace">JumpScale.baselib.performancetrace.PerformanceTrace module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.performancetrace.html#module-JumpScale.baselib.performancetrace">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.platforms.html">JumpScale.baselib.platforms package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.platforms.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.platforms.ubuntu.html">JumpScale.baselib.platforms.ubuntu package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.platforms.ubuntu.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.platforms.ubuntu.html#module-JumpScale.baselib.platforms.ubuntu.Ubuntu">JumpScale.baselib.platforms.ubuntu.Ubuntu module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.platforms.ubuntu.html#module-JumpScale.baselib.platforms.ubuntu">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.platforms.html#module-JumpScale.baselib.platforms">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.redis.html">JumpScale.baselib.redis package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redis.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redis.html#module-JumpScale.baselib.redis.Redis">JumpScale.baselib.redis.Redis module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redis.html#module-JumpScale.baselib.redis">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.redisworker.html">JumpScale.baselib.redisworker package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redisworker.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redisworker.html#module-JumpScale.baselib.redisworker.RedisWorker">JumpScale.baselib.redisworker.RedisWorker module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.redisworker.html#module-JumpScale.baselib.redisworker">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.remote.html">JumpScale.baselib.remote package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.remote.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.avahi.html">JumpScale.baselib.remote.avahi package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.avahi.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.avahi.html#module-JumpScale.baselib.remote.avahi.Avahi">JumpScale.baselib.remote.avahi.Avahi module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.avahi.html#module-JumpScale.baselib.remote.avahi">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html">JumpScale.baselib.remote.cluster package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#jumpscale-baselib-remote-cluster-cluster-module">JumpScale.baselib.remote.cluster.Cluster module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster.ClusterConfigs">JumpScale.baselib.remote.cluster.ClusterConfigs module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster.ClusterFactory">JumpScale.baselib.remote.cluster.ClusterFactory module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster.ClusterNode">JumpScale.baselib.remote.cluster.ClusterNode module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster.ClusterSSHClient">JumpScale.baselib.remote.cluster.ClusterSSHClient module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster.Replicator">JumpScale.baselib.remote.cluster.Replicator module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cluster.html#module-JumpScale.baselib.remote.cluster">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.cuisine.html">JumpScale.baselib.remote.cuisine package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cuisine.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cuisine.html#module-JumpScale.baselib.remote.cuisine.Cuisine">JumpScale.baselib.remote.cuisine.Cuisine module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.cuisine.html#module-JumpScale.baselib.remote.cuisine">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.fabric.html">JumpScale.baselib.remote.fabric package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.fabric.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.fabric.html#module-JumpScale.baselib.remote.fabric.FabricTool">JumpScale.baselib.remote.fabric.FabricTool module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.fabric.html#module-JumpScale.baselib.remote.fabric">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.remotesystem.html">JumpScale.baselib.remote.remotesystem package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.remotesystem.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.remotesystem.html#module-JumpScale.baselib.remote.remotesystem.RemoteSystem">JumpScale.baselib.remote.remotesystem.RemoteSystem module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.remotesystem.html#module-JumpScale.baselib.remote.remotesystem">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.remote.ssh.html">JumpScale.baselib.remote.ssh package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.ssh.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.ssh.html#module-JumpScale.baselib.remote.ssh.SSHClient">JumpScale.baselib.remote.ssh.SSHClient module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.ssh.html#module-JumpScale.baselib.remote.ssh.SSHTool">JumpScale.baselib.remote.ssh.SSHTool module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.remote.ssh.html#module-JumpScale.baselib.remote.ssh">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.remote.html#module-JumpScale.baselib.remote">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.screen.html">JumpScale.baselib.screen package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.screen.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.screen.html#module-JumpScale.baselib.screen.Screen">JumpScale.baselib.screen.Screen module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.screen.html#module-JumpScale.baselib.screen.Tmux">JumpScale.baselib.screen.Tmux module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.screen.html#module-JumpScale.baselib.screen">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.serializers.html">JumpScale.baselib.serializers package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerBase64">JumpScale.baselib.serializers.SerializerBase64 module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerBlosc">JumpScale.baselib.serializers.SerializerBlosc module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerBlowfish">JumpScale.baselib.serializers.SerializerBlowfish module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerCRC">JumpScale.baselib.serializers.SerializerCRC module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerDict">JumpScale.baselib.serializers.SerializerDict module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerHRD">JumpScale.baselib.serializers.SerializerHRD module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerInt">JumpScale.baselib.serializers.SerializerInt module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerLZMA">JumpScale.baselib.serializers.SerializerLZMA module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerMSGPack">JumpScale.baselib.serializers.SerializerMSGPack module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerPickle">JumpScale.baselib.serializers.SerializerPickle module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#jumpscale-baselib-serializers-serializersnappy-module">JumpScale.baselib.serializers.SerializerSnappy module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerTime">JumpScale.baselib.serializers.SerializerTime module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializerUJson">JumpScale.baselib.serializers.SerializerUJson module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers.SerializersFactory">JumpScale.baselib.serializers.SerializersFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.serializers.html#module-JumpScale.baselib.serializers">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.servers.html">JumpScale.baselib.servers package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.servers.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.servers.html#jumpscale-baselib-servers-cloudbroker-module">JumpScale.baselib.servers.cloudbroker module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.servers.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.sort.html">JumpScale.baselib.sort package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.sort.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.sort.html#module-JumpScale.baselib.sort.Sort">JumpScale.baselib.sort.Sort module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.sort.html#module-JumpScale.baselib.sort">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.specparser.html">JumpScale.baselib.specparser package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.specparser.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.specparser.html#module-JumpScale.baselib.specparser.SpecParser">JumpScale.baselib.specparser.SpecParser module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.specparser.html#module-JumpScale.baselib.specparser">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.ssl.html">JumpScale.baselib.ssl package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.ssl.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.ssl.html#module-JumpScale.baselib.ssl.SSL">JumpScale.baselib.ssl.SSL module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.ssl.html#module-JumpScale.baselib.ssl">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.startupmanager.html">JumpScale.baselib.startupmanager package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.startupmanager.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.startupmanager.html#module-JumpScale.baselib.startupmanager.StartupManager">JumpScale.baselib.startupmanager.StartupManager module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.startupmanager.html#module-JumpScale.baselib.startupmanager">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.stataggregator.html">JumpScale.baselib.stataggregator package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.stataggregator.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.stataggregator.html#module-JumpScale.baselib.stataggregator.StatAggregator">JumpScale.baselib.stataggregator.StatAggregator module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.stataggregator.html#module-JumpScale.baselib.stataggregator.redisstataggregator">JumpScale.baselib.stataggregator.redisstataggregator module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.stataggregator.html#module-JumpScale.baselib.stataggregator">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.statmanager.html">JumpScale.baselib.statmanager package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.statmanager.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.statmanager.html#module-JumpScale.baselib.statmanager.StatManager">JumpScale.baselib.statmanager.StatManager module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.statmanager.html#module-JumpScale.baselib.statmanager">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.tags.html">JumpScale.baselib.tags package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.tags.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.tags.html#module-JumpScale.baselib.tags.Tags">JumpScale.baselib.tags.Tags module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.tags.html#module-JumpScale.baselib.tags.TagsFactory">JumpScale.baselib.tags.TagsFactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.tags.html#module-JumpScale.baselib.tags">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.taskletengine.html">JumpScale.baselib.taskletengine package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.taskletengine.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.taskletengine.html#module-JumpScale.baselib.taskletengine.TaskletEngine">JumpScale.baselib.taskletengine.TaskletEngine module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.taskletengine.html#module-JumpScale.baselib.taskletengine">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.testengine.html">JumpScale.baselib.testengine package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.testengine.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.testengine.html#module-JumpScale.baselib.testengine.TestEngine">JumpScale.baselib.testengine.TestEngine module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.testengine.html#module-JumpScale.baselib.testengine.TestEngineKds">JumpScale.baselib.testengine.TestEngineKds module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.testengine.html#module-JumpScale.baselib.testengine">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.units.html">JumpScale.baselib.units package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.units.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.units.html#module-JumpScale.baselib.units.units">JumpScale.baselib.units.units module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.units.html#module-JumpScale.baselib.units">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.vcs.html">JumpScale.baselib.vcs package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.vcs.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.vcs.html#module-JumpScale.baselib.vcs.vcsfactory">JumpScale.baselib.vcs.vcsfactory module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.vcs.html#module-JumpScale.baselib.vcs">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.watchdog.html">JumpScale.baselib.watchdog package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.watchdog.html#subpackages">Subpackages</a><ul>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.watchdog.client.html">JumpScale.baselib.watchdog.client package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.client.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.client.html#jumpscale-baselib-watchdog-client-watchdogclient-module">JumpScale.baselib.watchdog.client.WatchdogClient module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.client.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l3"><a class="reference internal" href="JumpScale.baselib.watchdog.manager.html">JumpScale.baselib.watchdog.manager package</a><ul>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.manager.html#submodules">Submodules</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.manager.html#jumpscale-baselib-watchdog-manager-watchdogfactory-module">JumpScale.baselib.watchdog.manager.WatchdogFactory module</a></li>
   <li class="toctree-l4"><a class="reference internal" href="JumpScale.baselib.watchdog.manager.html#module-contents">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.watchdog.html#module-JumpScale.baselib.watchdog">Module contents</a></li>
   </ul>
   </li>
   <li class="toctree-l1"><a class="reference internal" href="JumpScale.baselib.webdis.html">JumpScale.baselib.webdis package</a><ul>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.webdis.html#submodules">Submodules</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.webdis.html#module-JumpScale.baselib.webdis.Webdis">JumpScale.baselib.webdis.Webdis module</a></li>
   <li class="toctree-l2"><a class="reference internal" href="JumpScale.baselib.webdis.html#module-JumpScale.baselib.webdis">Module contents</a></li>
   </ul>
   </li>
   </ul>
   </div>
   </div>
   <div class="section" id="module-JumpScale.baselib">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib package</a><ul>
   <li><a class="reference internal" href="#subpackages">Subpackages</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.base.html"
                           title="previous chapter">JumpScale.base package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.actions.html"
                           title="next chapter">JumpScale.baselib.actions package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.txt"
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
             <a href="JumpScale.baselib.actions.html" title="JumpScale.baselib.actions package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.base.html" title="JumpScale.base package"
                >previous</a> |</li>
           <li><a href="../index.html">Jumpscale Doc 7.0 documentation</a> &raquo;</li>
             <li><a href="JumpScale.html" >JumpScale package</a> &raquo;</li> 
         </ul>
       </div>
       <div class="footer">
       </div>
     </body>
   </html>