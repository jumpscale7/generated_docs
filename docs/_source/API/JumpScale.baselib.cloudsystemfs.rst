.. raw:: html
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   
   
   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
       <title>JumpScale.baselib.cloudsystemfs package &mdash; Jumpscale Doc 7.0 documentation</title>
       
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
       <link rel="next" title="JumpScale.baselib.cmdline package" href="JumpScale.baselib.cmdline.html" />
       <link rel="prev" title="JumpScale.baselib.changetracker package" href="JumpScale.baselib.changetracker.html" /> 
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
             <a href="JumpScale.baselib.cmdline.html" title="JumpScale.baselib.cmdline package"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.changetracker.html" title="JumpScale.baselib.changetracker package"
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
               
     <div class="section" id="jumpscale-baselib-cloudsystemfs-package">
   <h1>JumpScale.baselib.cloudsystemfs package<a class="headerlink" href="#jumpscale-baselib-cloudsystemfs-package" title="Permalink to this headline">¶</a></h1>
   <div class="section" id="submodules">
   <h2>Submodules<a class="headerlink" href="#submodules" title="Permalink to this headline">¶</a></h2>
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.CifsFS">
   <span id="jumpscale-baselib-cloudsystemfs-cifsfs-module"></span><h2>JumpScale.baselib.cloudsystemfs.CifsFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.CifsFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.CifsFS.</tt><tt class="descname">CifsFS</tt><big>(</big><em>end_type</em>, <em>server</em>, <em>share</em>, <em>username</em>, <em>password</em>, <em>is_dir</em>, <em>recursive</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>Atype='copy'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd><p>Umount cifs share</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.download">
   <tt class="descname">download</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.download" title="Permalink to this definition">¶</a></dt>
   <dd><p>Download file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.end_type">
   <tt class="descname">end_type</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.end_type" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.exists">
   <tt class="descname">exists</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks file or directory existance</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.filename">
   <tt class="descname">filename</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.filename" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.is_dir">
   <tt class="descname">is_dir</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.is_dir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.list">
   <tt class="descname">list</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.list" title="Permalink to this definition">¶</a></dt>
   <dd><p>List content of directory</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.mntpoint">
   <tt class="descname">mntpoint</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.mntpoint" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.options">
   <tt class="descname">options</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.options" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.password">
   <tt class="descname">password</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.password" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.recursive">
   <tt class="descname">recursive</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.recursive" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.server">
   <tt class="descname">server</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.server" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.share">
   <tt class="descname">share</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.share" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.subdir">
   <tt class="descname">subdir</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.subdir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.upload">
   <tt class="descname">upload</tt><big>(</big><em>uploadPath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CifsFS.html#CifsFS.upload"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.upload" title="Permalink to this definition">¶</a></dt>
   <dd><p>Store file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.username">
   <tt class="descname">username</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CifsFS.CifsFS.username" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.CloudSystemFS">
   <span id="jumpscale-baselib-cloudsystemfs-cloudsystemfs-module"></span><h2>JumpScale.baselib.cloudsystemfs.CloudSystemFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.CloudSystemFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.CloudSystemFS.</tt><tt class="descname">CloudSystemFS</tt><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS" title="Permalink to this definition">¶</a></dt>
   <dd><dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.copyDir">
   <tt class="descname">copyDir</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>recursive=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.copyDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.copyDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>Copy Directory</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.copyFile">
   <tt class="descname">copyFile</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.copyFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.copyFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>export specified file to destination
   &#64;todo needs to be copied onto cloudapi aswell</p>
   <p>&#64;param sourcepath: location of the file to export
   &#64;type sourcepath: string</p>
   <p>&#64;param destinationpath: location to export the file to. e.g. cifs://login:passwd&#64;10.10.1.1/systemnas
   &#64;type destinationpath: string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.exportDir">
   <tt class="descname">exportDir</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>recursive=True</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.exportDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.exportDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>export specified folder to destination
   &#64;todo needs to be copied onto cloudapi aswell</p>
   <p>&#64;param sourcepath:       location to export. e.g. <a class="reference external" href="ftp://login:passwd&#64;10.10.1.1/myroot/drive_c_kds.vdi">ftp://login:passwd&#64;10.10.1.1/myroot/drive_c_kds.vdi</a>
   &#64;type sourcepath:        string</p>
   <p>&#64;param destinationpath:  location to export the dir to
   &#64;type destinationpath:   string</p>
   <p>&#64;param recursive:        if true will include all sub-directories
   &#64;type recursive:         boolean</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.exportVolume">
   <tt class="descname">exportVolume</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>format='vdi'</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.exportVolume"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.exportVolume" title="Permalink to this definition">¶</a></dt>
   <dd><p>export volume to a e.g. VDI</p>
   <p>&#64;param sourcepath:         device name of the volume to export e.g.  E: F on windows, or /dev/sda5 on linux
   &#64;type sourcepath:          string</p>
   <p>&#64;param destinationpath:    location to export the volume to e.g. <a class="reference external" href="ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/test.vdi">ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/test.vdi</a>, if .vdi.tgz at end then compression will happen automatically
   &#64;type destinationpath:     string
   &#64;param tempdir:            (optional) directory to use as temporary directory, for cifs/smb tempdir can be None which means: export directly over CIFS
   &#64;type tempdir:             string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.fileGetContents">
   <tt class="descname">fileGetContents</tt><big>(</big><em>url</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.fileGetContents"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.fileGetContents" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importDir">
   <tt class="descname">importDir</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.importDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>import specified dir to machine path
   &#64;todo needs to be copied onto cloudapi aswell</p>
   <p>&#64;param sourcepath: location to import the dir from. e.g. <a class="reference external" href="ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/">ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/</a>
   &#64;type sourcepath: string</p>
   <p>&#64;param destinationpath: location to import the dir to (i.e.full path on machine)
   &#64;type destinationpath: string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importFile">
   <tt class="descname">importFile</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.importFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>import specified file to machine path
   &#64;todo needs to be copied onto cloudapi aswell</p>
   <p>&#64;param sourcepath: location to import the file from. e.g. <a class="reference external" href="ftp://login:passwd&#64;10.10.1.1/myroot/drive_c_kds.vdi">ftp://login:passwd&#64;10.10.1.1/myroot/drive_c_kds.vdi</a>
   &#64;type sourcepath: string</p>
   <p>&#64;param destinationpath: location to import the file to (i.e.full path on machine)
   &#64;type destinationpath: string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importVolume">
   <tt class="descname">importVolume</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>format='vdi'</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.importVolume"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.importVolume" title="Permalink to this definition">¶</a></dt>
   <dd><p>Import volume from specified source</p>
   <p>&#64;param sourcepath: location to import the volume from e.g. <a class="reference external" href="ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/test.vdi">ftp://login:passwd&#64;10.10.1.1/myroot/mymachine1/test.vdi</a>, if .vdi.tgz at end then compression will happen automatically
   &#64;type sourcepath: string</p>
   <p>&#64;param destinationpath: name of the device to import to e.g.  E: F on windows, or /dev/sda5 on linux
   &#64;type destinationpath: string
   &#64;param tempdir:            (optional) directory whereto will be exported; default is the default temp-directory as determined by underlying system
   &#64;type tempdir:             string</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.listDir">
   <tt class="descname">listDir</tt><big>(</big><em>path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.listDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.listDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>List content of specified path</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.moveDir">
   <tt class="descname">moveDir</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>recursive=True</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.moveDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.moveDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>Move directory</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.moveFile">
   <tt class="descname">moveFile</tt><big>(</big><em>sourcepath</em>, <em>destinationpath</em>, <em>tempdir='/tmp/jumpscale'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.moveFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.moveFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>Move a file</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.sourcePathExists">
   <tt class="descname">sourcePathExists</tt><big>(</big><em>sourcepath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.sourcePathExists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.sourcePathExists" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.writeFile">
   <tt class="descname">writeFile</tt><big>(</big><em>url</em>, <em>content</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/CloudSystemFS.html#CloudSystemFS.writeFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.CloudSystemFS.CloudSystemFS.writeFile" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.FileFS">
   <span id="jumpscale-baselib-cloudsystemfs-filefs-module"></span><h2>JumpScale.baselib.cloudsystemfs.FileFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.FileFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.FileFS.</tt><tt class="descname">FileFS</tt><big>(</big><em>end_type</em>, <em>path</em>, <em>is_dir=False</em>, <em>recursive=False</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>Atype='copy'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FileFS.html#FileFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FileFS.html#FileFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd><p>If needed umount and cleanup</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.download">
   <tt class="descname">download</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FileFS.html#FileFS.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.download" title="Permalink to this definition">¶</a></dt>
   <dd><p>Download file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.end_type">
   <tt class="descname">end_type</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.end_type" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.exists">
   <tt class="descname">exists</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FileFS.html#FileFS.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks file or directory existance</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.is_dir">
   <tt class="descname">is_dir</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.is_dir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.local_file">
   <tt class="descname">local_file</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.local_file" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.path">
   <tt class="descname">path</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.path" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.recursive">
   <tt class="descname">recursive</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.recursive" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FileFS.FileFS.upload">
   <tt class="descname">upload</tt><big>(</big><em>uploadPath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FileFS.html#FileFS.upload"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FileFS.FileFS.upload" title="Permalink to this definition">¶</a></dt>
   <dd><p>Store file</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.FtpFS">
   <span id="jumpscale-baselib-cloudsystemfs-ftpfs-module"></span><h2>JumpScale.baselib.cloudsystemfs.FtpFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.FtpFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.FtpFS.</tt><tt class="descname">FtpFS</tt><big>(</big><em>end_type</em>, <em>server</em>, <em>path</em>, <em>username</em>, <em>password</em>, <em>is_dir=False</em>, <em>recursive=False</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>Atype='copy'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd><p>Cleanup of ftp connection</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.download">
   <tt class="descname">download</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.download" title="Permalink to this definition">¶</a></dt>
   <dd><p>Download file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.end_type">
   <tt class="descname">end_type</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.end_type" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.exists">
   <tt class="descname">exists</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks file or directory existance</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.filename">
   <tt class="descname">filename</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.filename" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.ftp">
   <tt class="descname">ftp</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.ftp" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.handleDownloadDir">
   <tt class="descname">handleDownloadDir</tt><big>(</big><em>dirname</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.handleDownloadDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.handleDownloadDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>Ftp handle a download directory</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.handleUploadDir">
   <tt class="descname">handleUploadDir</tt><big>(</big><em>dir</em>, <em>upload_path</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.handleUploadDir"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.handleUploadDir" title="Permalink to this definition">¶</a></dt>
   <dd><p>Ftp handle a upload directory</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.is_dir">
   <tt class="descname">is_dir</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.is_dir" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.list">
   <tt class="descname">list</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.list" title="Permalink to this definition">¶</a></dt>
   <dd><p>List files in dir</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.local_file">
   <tt class="descname">local_file</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.local_file" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.password">
   <tt class="descname">password</tt><em class="property"> = 'user&#64;aserver.com'</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.password" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.path">
   <tt class="descname">path</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.path" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.recursive">
   <tt class="descname">recursive</tt><em class="property"> = False</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.recursive" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.retrieveFile">
   <tt class="descname">retrieveFile</tt><big>(</big><em>file</em>, <em>dir</em>, <em>dest</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.retrieveFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.retrieveFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>Ftp copying file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.server">
   <tt class="descname">server</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.server" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.storeFile">
   <tt class="descname">storeFile</tt><big>(</big><em>file</em>, <em>uploadPath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.storeFile"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.storeFile" title="Permalink to this definition">¶</a></dt>
   <dd><p>Ftp upload file</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.upload">
   <tt class="descname">upload</tt><big>(</big><em>uploadPath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/FtpFS.html#FtpFS.upload"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.upload" title="Permalink to this definition">¶</a></dt>
   <dd><p>Store file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.username">
   <tt class="descname">username</tt><em class="property"> = 'anonymous'</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.FtpFS.FtpFS.username" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.HttpFS">
   <span id="jumpscale-baselib-cloudsystemfs-httpfs-module"></span><h2>JumpScale.baselib.cloudsystemfs.HttpFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.HttpFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.HttpFS.</tt><tt class="descname">HttpFS</tt><big>(</big><em>end_type</em>, <em>server</em>, <em>path</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>Atype=None</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/HttpFS.html#HttpFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/HttpFS.html#HttpFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd><p>Cleanup http connection and temp file</p>
   </dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.download">
   <tt class="descname">download</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/HttpFS.html#HttpFS.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.download" title="Permalink to this definition">¶</a></dt>
   <dd><p>Download file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.end_type">
   <tt class="descname">end_type</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.end_type" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.exists">
   <tt class="descname">exists</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/HttpFS.html#HttpFS.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks if a file exists</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.filename">
   <tt class="descname">filename</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.filename" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.http_socket">
   <tt class="descname">http_socket</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.http_socket" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.local_file">
   <tt class="descname">local_file</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.local_file" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.path">
   <tt class="descname">path</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.path" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.server">
   <tt class="descname">server</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.server" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.upload">
   <tt class="descname">upload</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/HttpFS.html#HttpFS.upload"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.HttpFS.HttpFS.upload" title="Permalink to this definition">¶</a></dt>
   <dd><p>Upload of file
   This is currently not supported for HTTP</p>
   </dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs.SshFS">
   <span id="jumpscale-baselib-cloudsystemfs-sshfs-module"></span><h2>JumpScale.baselib.cloudsystemfs.SshFS module<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs.SshFS" title="Permalink to this headline">¶</a></h2>
   <dl class="class">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS">
   <em class="property">class </em><tt class="descclassname">JumpScale.baselib.cloudsystemfs.SshFS.</tt><tt class="descname">SshFS</tt><big>(</big><em>end_type</em>, <em>server</em>, <em>directory</em>, <em>username</em>, <em>password</em>, <em>is_dir</em>, <em>recursive</em>, <em>tempdir='/tmp/jumpscale'</em>, <em>Atype='copy'</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS" title="Permalink to this definition">¶</a></dt>
   <dd><p>Bases: <tt class="xref py py-class docutils literal"><span class="pre">object</span></tt></p>
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.cleanup">
   <tt class="descname">cleanup</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS.cleanup"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.cleanup" title="Permalink to this definition">¶</a></dt>
   <dd><p>Umount sshfs share</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.directory">
   <tt class="descname">directory</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.directory" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.download">
   <tt class="descname">download</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS.download"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.download" title="Permalink to this definition">¶</a></dt>
   <dd><p>Download file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.end_type">
   <tt class="descname">end_type</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.end_type" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.exists">
   <tt class="descname">exists</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS.exists"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.exists" title="Permalink to this definition">¶</a></dt>
   <dd><p>Checks file or directory existance</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.filename">
   <tt class="descname">filename</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.filename" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.list">
   <tt class="descname">list</tt><big>(</big><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS.list"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.list" title="Permalink to this definition">¶</a></dt>
   <dd><p>List content of directory</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.mntpoint">
   <tt class="descname">mntpoint</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.mntpoint" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.password">
   <tt class="descname">password</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.password" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.server">
   <tt class="descname">server</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.server" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.share">
   <tt class="descname">share</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.share" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   <dl class="method">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.upload">
   <tt class="descname">upload</tt><big>(</big><em>uploadPath</em><big>)</big><a class="reference internal" href="../_modules/JumpScale/baselib/cloudsystemfs/SshFS.html#SshFS.upload"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.upload" title="Permalink to this definition">¶</a></dt>
   <dd><p>Store file</p>
   </dd></dl>
   
   <dl class="attribute">
   <dt id="JumpScale.baselib.cloudsystemfs.SshFS.SshFS.username">
   <tt class="descname">username</tt><em class="property"> = None</em><a class="headerlink" href="#JumpScale.baselib.cloudsystemfs.SshFS.SshFS.username" title="Permalink to this definition">¶</a></dt>
   <dd></dd></dl>
   
   </dd></dl>
   
   </div>
   <div class="section" id="module-JumpScale.baselib.cloudsystemfs">
   <span id="module-contents"></span><h2>Module contents<a class="headerlink" href="#module-JumpScale.baselib.cloudsystemfs" title="Permalink to this headline">¶</a></h2>
   </div>
   </div>
   
   
             </div>
           </div>
         </div>
         <div class="sphinxsidebar">
           <div class="sphinxsidebarwrapper">
     <h3><a href="../index.html">Table Of Contents</a></h3>
     <ul>
   <li><a class="reference internal" href="#">JumpScale.baselib.cloudsystemfs package</a><ul>
   <li><a class="reference internal" href="#submodules">Submodules</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.CifsFS">JumpScale.baselib.cloudsystemfs.CifsFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.CloudSystemFS">JumpScale.baselib.cloudsystemfs.CloudSystemFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.FileFS">JumpScale.baselib.cloudsystemfs.FileFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.FtpFS">JumpScale.baselib.cloudsystemfs.FtpFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.HttpFS">JumpScale.baselib.cloudsystemfs.HttpFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs.SshFS">JumpScale.baselib.cloudsystemfs.SshFS module</a></li>
   <li><a class="reference internal" href="#module-JumpScale.baselib.cloudsystemfs">Module contents</a></li>
   </ul>
   </li>
   </ul>
   
     <h4>Previous topic</h4>
     <p class="topless"><a href="JumpScale.baselib.changetracker.html"
                           title="previous chapter">JumpScale.baselib.changetracker package</a></p>
     <h4>Next topic</h4>
     <p class="topless"><a href="JumpScale.baselib.cmdline.html"
                           title="next chapter">JumpScale.baselib.cmdline package</a></p>
     <h3>This Page</h3>
     <ul class="this-page-menu">
       <li><a href="../_sources/API/JumpScale.baselib.cloudsystemfs.txt"
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
             <a href="JumpScale.baselib.cmdline.html" title="JumpScale.baselib.cmdline package"
                >next</a> |</li>
           <li class="right" >
             <a href="JumpScale.baselib.changetracker.html" title="JumpScale.baselib.changetracker package"
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