# -*- coding: utf-8 -*-
#
# Jumpscale Doc documentation build configuration file, created by
# sphinx-quickstart on Fri Aug 15 11:02:32 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import sys
import os

sys.path.append("/opt/code/github/jumpscale/jumpscale_core/lib/JumpScale/")


# sys.path.append(os.path.abspath('.'))
# from .DummyBuilders import DummyBuilder   


# from mock import MagicMock

# class Mock(MagicMock):
#     @classmethod
#     def __getattr__(cls, name):
#         return Mock()


#     # def get_doc(obj, member):
#     #     if member in obj.__dict__:
#     #         return obj.__dict__[member].__doc__
#     #     return type(obj).__dict__[member].__doc__

#     # def get_docstrings(obj):
#     #     try:
#     #         members = dir(obj)
#     #     except Exception:
#     #         members = []
#     #     return [(member, Mock.get_doc(obj, member)) for member in members]

# MOCK_MODULES = [
#   "JumpScale",
#   "JumpScale.base.BYTEPROCESSOR",
#   "JumpScale.base.ERRORHANDLER",
#   "JumpScale.base.FS",
#   "JumpScale.base.FSWALKER",
#   "JumpScale.base.FSWALKER_test",
#   "JumpScale.base.LOADER",
#   "JumpScale.base.REGEXTOOL",
#   "JumpScale.base.TIMER",
#   "JumpScale.base",
#   "JumpScale.baselib",
#   "JumpScale.baselib.actions",
#   "JumpScale.baselib.actions.action.ActionController",
#   "JumpScale.baselib.actions.action.RunningAction",
#   "JumpScale.baselib.actions.action",
#   "JumpScale.baselib.actions.transaction.Transaction",
#   "JumpScale.baselib.actions.transaction.TransactionController",
#   "JumpScale.baselib.actions.transaction",
#   "JumpScale.baselib.admin.Admin",
#   "JumpScale.baselib.admin",
#   "JumpScale.baselib.backup.BackupClient",
#   "JumpScale.baselib.backup.BackupFactory",
#   "JumpScale.baselib.backup",
#   "JumpScale.baselib.backuptools.backup",
#   "JumpScale.baselib.backuptools.object_store",
#   "JumpScale.baselib.backuptools",
#   "JumpScale.baselib.bitbucket.Bitbucket",
#   "JumpScale.baselib.bitbucket.BitbucketConfigManagement",
#   "JumpScale.baselib.bitbucket.BitbucketInterface",
#   "JumpScale.baselib.bitbucket",
#   "JumpScale.baselib.blobstor.BlobStor",
#   "JumpScale.baselib.blobstor.BlobStorConfigManagement",
#   "JumpScale.baselib.blobstor",
#   "JumpScale.baselib.blobstor2.BlobStorClient",
#   "JumpScale.baselib.blobstor2.BlobStorFactory",
#   "JumpScale.baselib.blobstor2.BlobStorMaster",
#   "JumpScale.baselib.blobstor2.BlobStorServer",
#   "JumpScale.baselib.blobstor2.BlobStorServerOld",
#   "JumpScale.baselib.blobstor2.BlobStorServerSimple",
#   "JumpScale.baselib.blobstor2.BlobStorWorker",
#   "JumpScale.baselib.blobstor2",
#   "JumpScale.baselib.changetracker.ChangeTrackerClient",
#   "JumpScale.baselib.changetracker.ChangeTrackerFactory",
#   "JumpScale.baselib.changetracker",
#   "JumpScale.baselib.cloudsystemfs.CifsFS",
#   "JumpScale.baselib.cloudsystemfs.CloudSystemFS",
#   "JumpScale.baselib.cloudsystemfs.FileFS",
#   "JumpScale.baselib.cloudsystemfs.FtpFS",
#   "JumpScale.baselib.cloudsystemfs.HttpFS",
#   "JumpScale.baselib.cloudsystemfs.SshFS",
#   "JumpScale.baselib.cloudsystemfs",
#   "JumpScale.baselib.cmdline.CommandLauncher",
#   "JumpScale.baselib.cmdline.Options",
#   "JumpScale.baselib.cmdline",
#   "JumpScale.baselib.cmdutils",
#   "JumpScale.baselib.code.Appserver6GreenletBase",
#   "JumpScale.baselib.code.Appserver6GreenletScheduleBase",
#   "JumpScale.baselib.code.Appserver6GreenletTaskletsBase",
#   "JumpScale.baselib.code.ClassBase",
#   "JumpScale.baselib.code.Code",
#   "JumpScale.baselib.code",
#   "JumpScale.baselib.code.cmdutils",
#   "JumpScale.baselib.codeexecutor.CodeExecutor",
#   "JumpScale.baselib.codeexecutor",
#   "JumpScale.baselib.codetools.ClassDef",
#   "JumpScale.baselib.codetools.CodeElements",
#   "JumpScale.baselib.codetools.CodeManager",
#   "JumpScale.baselib.codetools.CodeTools",
#   "JumpScale.baselib.codetools.MethodDef",
#   "JumpScale.baselib.codetools.PropertyDef",
#   "JumpScale.baselib.codetools.RegexTools",
#   "JumpScale.baselib.codetools.TemplateEngine",
#   "JumpScale.baselib.codetools.TemplateEngineWrapper",
#   "JumpScale.baselib.codetools.TextCharEditor",
#   "JumpScale.baselib.codetools.TextFileEditor",
#   "JumpScale.baselib.codetools.TextLineEditor",
#   "JumpScale.baselib.codetools.WordReplacer",
#   "JumpScale.baselib.codetools",
#   "JumpScale.baselib.credis.CRedis",
#   "JumpScale.baselib.credis.CRedisQueue",
#   "JumpScale.baselib.credis",
#   "JumpScale.baselib.dnsmasq.dnsmasq",
#   "JumpScale.baselib.dnsmasq",
#   "JumpScale.baselib.elasticsearch.Elasticsearch",
#   "JumpScale.baselib.elasticsearch",
#   "JumpScale.baselib.expect.Expect",
#   "JumpScale.baselib.expect",
#   "JumpScale.baselib.git.GitClient",
#   "JumpScale.baselib.git.GitFactory",
#   "JumpScale.baselib.git",
#   "JumpScale.baselib.github.github",
#   "JumpScale.baselib.github",
#   "JumpScale.baselib.gitlab.GitlabFactory",
#   "JumpScale.baselib.gitlab.GitlabInstance",
#   "JumpScale.baselib.gitlab",
#   "JumpScale.baselib.gitlab.gitlab.exceptions",
#   "JumpScale.baselib.gitlab.gitlab",
#   "JumpScale.baselib.graphite.GraphiteClient",
#   "JumpScale.baselib.graphite",
#   "JumpScale.baselib.hash.HashTool",
#   "JumpScale.baselib.hash",
#   "JumpScale.baselib.hrd.HumanReadableData",
#   "JumpScale.baselib.hrd",
#   "JumpScale.baselib.http_client.HttpClient",
#   "JumpScale.baselib.http_client",
#   "JumpScale.baselib.http_client.httplib2.iri2uri",
#   "JumpScale.baselib.http_client.httplib2.socks",
#   "JumpScale.baselib.http_client.httplib2",
#   "JumpScale.baselib.influxdb.Influxdb",
#   "JumpScale.baselib.influxdb",
#   "JumpScale.baselib.inifile.IniFile",
#   "JumpScale.baselib.inifile",
#   "JumpScale.baselib.installtools.InstallTools",
#   "JumpScale.baselib.installtools",
#   "JumpScale.baselib.jpackages.ActionManager",
#   "JumpScale.baselib.jpackages.CodeManagementRecipe",
#   "JumpScale.baselib.jpackages.Domain",
#   "JumpScale.baselib.jpackages.JPackageClient",
#   "JumpScale.baselib.jpackages.JPackageObject",
#   "JumpScale.baselib.jpackages.JPackageStateObject",
#   "JumpScale.baselib.jpackages.JPackagesGenDocs",
#   "JumpScale.baselib.jpackages.PythonPackage",
#   "JumpScale.baselib.jpackages.ReleaseMgmt",
#   "JumpScale.baselib.jpackages.enumerators4",
#   "JumpScale.baselib.jpackages",
#   "JumpScale.baselib.jsdeveltools.JSDevelTools",
#   "JumpScale.baselib.jsdeveltools.JSDevelToolsInstaller",
#   "JumpScale.baselib.jsdeveltools",
#   "JumpScale.baselib.key_value_store.arakoon_store",
#   "JumpScale.baselib.key_value_store.file_system_store",
#   "JumpScale.baselib.key_value_store.leveldb_store",
#   "JumpScale.baselib.key_value_store.memory_store",
#   "JumpScale.baselib.key_value_store.mongodb_store",
#   "JumpScale.baselib.key_value_store.redis_store",
#   "JumpScale.baselib.key_value_store.store",
#   "JumpScale.baselib.key_value_store.store_factory",
#   "JumpScale.baselib.key_value_store.test_store",
#   "JumpScale.baselib.key_value_store",
#   "JumpScale.baselib.lrucache.LRUCache",
#   "JumpScale.baselib.lrucache.LRUCacheFactory",
#   "JumpScale.baselib.lrucache.RWCache",
#   "JumpScale.baselib.lrucache",
#   "JumpScale.baselib.mailclient.emailclient",
#   "JumpScale.baselib.mailclient",
#   "JumpScale.baselib.manage.managerbase",
#   "JumpScale.baselib.manage",
#   "JumpScale.baselib.mercurial.HgLibClient",
#   "JumpScale.baselib.mercurial.HgLibFactory",
#   "JumpScale.baselib.mercurial",
#   "JumpScale.baselib.mercurial.hglib.client",
#   "JumpScale.baselib.mercurial.hglib.context",
#   "JumpScale.baselib.mercurial.hglib.error",
#   "JumpScale.baselib.mercurial.hglib.merge",
#   "JumpScale.baselib.mercurial.hglib.templates",
#   "JumpScale.baselib.mercurial.hglib.util",
#   "JumpScale.baselib.mercurial.hglib",
#   "JumpScale.baselib.netconfig.Netconfig",
#   "JumpScale.baselib.netconfig",
#   "JumpScale.baselib.params.Params",
#   "JumpScale.baselib.params",
#   "JumpScale.baselib.performancetrace.PerformanceTrace",
#   "JumpScale.baselib.performancetrace",
#   "JumpScale.baselib.platforms",
#   "JumpScale.baselib.platforms.ubuntu.Ubuntu",
#   "JumpScale.baselib.platforms.ubuntu",
#   "JumpScale.baselib.redis.Redis",
#   "JumpScale.baselib.redis",
#   "JumpScale.baselib.redisworker.RedisWorker",
#   "JumpScale.baselib.redisworker",
#   "JumpScale.baselib.remote",
#   "JumpScale.baselib.remote.avahi.Avahi",
#   "JumpScale.baselib.remote.avahi",
#   "JumpScale.baselib.remote.cluster.Cluster",
#   "JumpScale.baselib.remote.cluster.ClusterConfigs",
#   "JumpScale.baselib.remote.cluster.ClusterFactory",
#   "JumpScale.baselib.remote.cluster.ClusterNode",
#   "JumpScale.baselib.remote.cluster.ClusterSSHClient",
#   "JumpScale.baselib.remote.cluster.Replicator",
#   "JumpScale.baselib.remote.cluster",
#   "JumpScale.baselib.remote.cuisine.Cuisine",
#   "JumpScale.baselib.remote.cuisine",
#   "JumpScale.baselib.remote.fabric.FabricTool",
#   "JumpScale.baselib.remote.fabric",
#   "JumpScale.baselib.remote.remotesystem.RemoteSystem",
#   "JumpScale.baselib.remote.remotesystem",
#   "JumpScale.baselib.remote.ssh.SSHClient",
#   "JumpScale.baselib.remote.ssh.SSHTool",
#   "JumpScale.baselib.remote.ssh",
#   "JumpScale.baselib.screen.Screen",
#   "JumpScale.baselib.screen.Tmux",
#   "JumpScale.baselib.screen",
#   "JumpScale.baselib.serializers.SerializerBase64",
#   "JumpScale.baselib.serializers.SerializerBlosc",
#   "JumpScale.baselib.serializers.SerializerBlowfish",
#   "JumpScale.baselib.serializers.SerializerCRC",
#   "JumpScale.baselib.serializers.SerializerDict",
#   "JumpScale.baselib.serializers.SerializerHRD",
#   "JumpScale.baselib.serializers.SerializerInt",
#   "JumpScale.baselib.serializers.SerializerLZMA",
#   "JumpScale.baselib.serializers.SerializerMSGPack",
#   "JumpScale.baselib.serializers.SerializerPickle",
#   "JumpScale.baselib.serializers.SerializerSnappy",
#   "JumpScale.baselib.serializers.SerializerTime",
#   "JumpScale.baselib.serializers.SerializerUJson",
#   "JumpScale.baselib.serializers.SerializersFactory",
#   "JumpScale.baselib.serializers",
#   "JumpScale.baselib.servers.cloudbroker",
#   "JumpScale.baselib.servers",
#   "JumpScale.baselib.sort.Sort",
#   "JumpScale.baselib.sort",
#   "JumpScale.baselib.specparser.SpecParser",
#   "JumpScale.baselib.specparser",
#   "JumpScale.baselib.ssl.SSL",
#   "JumpScale.baselib.ssl",
#   "JumpScale.baselib.startupmanager.StartupManager",
#   "JumpScale.baselib.startupmanager",
#   "JumpScale.baselib.stataggregator.StatAggregator",
#   "JumpScale.baselib.stataggregator",
#   "JumpScale.baselib.statmanager.StatManager",
#   "JumpScale.baselib.statmanager",
#   "JumpScale.baselib.tags.Tags",
#   "JumpScale.baselib.tags.TagsFactory",
#   "JumpScale.baselib.tags",
#   "JumpScale.baselib.taskletengine.TaskletEngine",
#   "JumpScale.baselib.taskletengine",
#   "JumpScale.baselib.testengine.TestEngine",
#   "JumpScale.baselib.testengine.TestEngineKds",
#   "JumpScale.baselib.testengine",
#   "JumpScale.baselib.units.units",
#   "JumpScale.baselib.units",
#   "JumpScale.baselib.vcs.vcsfactory",
#   "JumpScale.baselib.vcs",
#   "JumpScale.baselib.watchdog",
#   "JumpScale.baselib.watchdog.client.WatchdogClient",
#   "JumpScale.baselib.watchdog.client",
#   "JumpScale.baselib.watchdog.manager.WatchdogFactory",
#   "JumpScale.baselib.watchdog.manager",
#   "JumpScale.baselib.webdis.Webdis",
#   "JumpScale.baselib.webdis",
#   "JumpScale.core.Application",
#   "JumpScale.core.Dirs",
#   "JumpScale.core.PlatformTypes",
#   "JumpScale.core.Time",
#   "JumpScale.core.Util",
#   "JumpScale.core.decorators",
#   "JumpScale.core",
#   "JumpScale.core.actors.ActorObject",
#   "JumpScale.core.actors.ActorObjects",
#   "JumpScale.core.actors",
#   "JumpScale.core.base",
#   "JumpScale.core.base.idgenerator.IDGenerator",
#   "JumpScale.core.base.idgenerator",
#   "JumpScale.core.base.time.Time",
#   "JumpScale.core.base.time",
#   "JumpScale.core.baseclasses.BaseEnumeration",
#   "JumpScale.core.baseclasses.BaseType",
#   "JumpScale.core.baseclasses.dirtyflaggingmixin",
#   "JumpScale.core.baseclasses",
#   "JumpScale.core.config.ConfigLib",
#   "JumpScale.core.config.IConfigBase",
#   "JumpScale.core.config.JConfig",
#   "JumpScale.core.config.JConfigBase",
#   "JumpScale.core.config",
#   "JumpScale.core.config.generator.agent_cfg",
#   "JumpScale.core.config.generator.arakoon_cfg",
#   "JumpScale.core.config.generator.osis_cfg",
#   "JumpScale.core.config.generator",
#   "JumpScale.core.db.DBConnection",
#   "JumpScale.core.db",
#   "JumpScale.core.debugger.Debugging",
#   "JumpScale.core.debugger",
#   "JumpScale.core.enumerators.AppStatusType",
#   "JumpScale.core.enumerators.ErrorConditionLevel",
#   "JumpScale.core.enumerators.ErrorConditionType",
#   "JumpScale.core.enumerators.LogLevel",
#   "JumpScale.core.enumerators.MessageType",
#   "JumpScale.core.enumerators.WinRegHiveType",
#   "JumpScale.core.enumerators.WinRegValueType",
#   "JumpScale.core.enumerators",
#   "JumpScale.core.errorhandling.ErrorConditionHandler",
#   "JumpScale.core.errorhandling.ErrorConditionObject",
#   "JumpScale.core.errorhandling.EventHandler",
#   "JumpScale.core.errorhandling.six",
#   "JumpScale.core.errorhandling.stacks",
#   "JumpScale.core.errorhandling",
#   "JumpScale.core.extensions.PMExtension",
#   "JumpScale.core.extensions.PMExtensions",
#   "JumpScale.core.extensions.PMExtensionsGroup",
#   "JumpScale.core.extensions",
#   "JumpScale.core.locale.locale",
#   "JumpScale.core.locale",
#   "JumpScale.core.logging.LogHandler",
#   "JumpScale.core.logging.RedirectStreams",
#   "JumpScale.core.logging",
#   "JumpScale.core.logging.logtargets.LogTargetFS",
#   "JumpScale.core.logging.logtargets.LogTargetLogForwarder",
#   "JumpScale.core.logging.logtargets.LogTargetScribe",
#   "JumpScale.core.logging.logtargets.LogTargetStdOut",
#   "JumpScale.core.logging.logtargets.LogTargetToPylabsLogConsole",
#   "JumpScale.core.logging.logtargets",
#   "JumpScale.core.pmtypes.CollectionTypes",
#   "JumpScale.core.pmtypes.CustomTypes",
#   "JumpScale.core.pmtypes.GenericTypes",
#   "JumpScale.core.pmtypes.IPAddress",
#   "JumpScale.core.pmtypes.PrimitiveTypes",
#   "JumpScale.core.pmtypes.base",
#   "JumpScale.core.pmtypes",
#   "JumpScale.core.properties.DirtyFlaggedProperty",
#   "JumpScale.core.properties.collections",
#   "JumpScale.core.properties.common",
#   "JumpScale.core.properties.customtypes",
#   "JumpScale.core.properties.primitives",
#   "JumpScale.core.properties",
#   "JumpScale.core.shellconfig.ConfigFileManager",
#   "JumpScale.core.shellconfig.DeclarativeConfig",
#   "JumpScale.core.shellconfig.ShellConfig",
#   "JumpScale.core.shellconfig",
#   "JumpScale.core.system.System",
#   "JumpScale.core.system.TarFile",
#   "JumpScale.core.system.ZipFile",
#   "JumpScale.core.system.fs",
#   "JumpScale.core.system.fswalker",
#   "JumpScale.core.system.net",
#   "JumpScale.core.system.process",
#   "JumpScale.core.system.processhelper",
#   "JumpScale.core.system.string",
#   "JumpScale.core.system.text",
#   "JumpScale.core.system.unix",
#   "JumpScale.core.system.windows",
#   "JumpScale.core.system",
#   "JumpScale.grid",
#   "JumpScale.grid.agentcontroller.AgentControllerFactory",
#   "JumpScale.grid.agentcontroller",
#   "JumpScale.grid.gevent.GeventLoop",
#   "JumpScale.grid.gevent.GeventLoopFactory",
#   "JumpScale.grid.gevent",
#   "JumpScale.grid.geventws.GeventWSFactory",
#   "JumpScale.grid.geventws.GeventWSServer",
#   "JumpScale.grid.geventws.GeventWSTransport",
#   "JumpScale.grid.geventws",
#   "JumpScale.grid.grid.BrokerMainActions",
#   "JumpScale.grid.grid.GridFactory",
#   "JumpScale.grid.grid.LogTargetElasticSearch",
#   "JumpScale.grid.grid.LogTargetOSIS",
#   "JumpScale.grid.grid.ZBroker",
#   "JumpScale.grid.grid.ZLogger",
#   "JumpScale.grid.grid.ZLoggerClient",
#   "JumpScale.grid.grid.ZWorker",
#   "JumpScale.grid.grid.ZWorkerClient",
#   "JumpScale.grid.grid",
#   "JumpScale.grid.grid.CoreModel.ModelObject",
#   "JumpScale.grid.grid.CoreModel.ZBase",
#   "JumpScale.grid.grid.CoreModel",
#   "JumpScale.grid.gridhealthchecker.gridhealthchecker",
#   "JumpScale.grid.gridhealthchecker",
#   "JumpScale.grid.jumpscripts.JumpscriptFactory",
#   "JumpScale.grid.jumpscripts",
#   "JumpScale.grid.master.Master",
#   "JumpScale.grid.master.MasterObjects",
#   "JumpScale.grid.master",
#   "JumpScale.grid.messagehandling.LogHandlerDB",
#   "JumpScale.grid.messagehandling.MessageHandler",
#   "JumpScale.grid.messagehandling.client_management",
#   "JumpScale.grid.messagehandling.logServerLocal",
#   "JumpScale.grid.messagehandling.logger_patch",
#   "JumpScale.grid.messagehandling.server",
#   "JumpScale.grid.messagehandling.server_management",
#   "JumpScale.grid.messagehandling.utils",
#   "JumpScale.grid.messagehandling",
#   "JumpScale.grid.messagehandling.gevent_zeromq.core",
#   "JumpScale.grid.messagehandling.gevent_zeromq.core",
#   "JumpScale.grid.messagehandling.gevent_zeromq.tests",
#   "JumpScale.grid.messagehandling.gevent_zeromq",
#   "JumpScale.grid.mongodbclient.MongoDBClient",
#   "JumpScale.grid.mongodbclient",
#   "JumpScale.grid.osis.OSISBaseObject",
#   "JumpScale.grid.osis.OSISBaseObjectComplexType",
#   "JumpScale.grid.osis.OSISCMDS",
#   "JumpScale.grid.osis.OSISClientForCat",
#   "JumpScale.grid.osis.OSISFactory",
#   "JumpScale.grid.osis.OSISStore",
#   "JumpScale.grid.osis.OSISStoreES",
#   "JumpScale.grid.osis.OSISStoreMongo",
#   "JumpScale.grid.osis",
#   "JumpScale.grid.osismodel.OSIS",
#   "JumpScale.grid.osismodel.OSISInstance",
#   "JumpScale.grid.osismodel",
#   "JumpScale.grid.processmanager.ProcessmanagerFactory",
#   "JumpScale.grid.processmanager",
#   "JumpScale.grid.serverbase.Daemon",
#   "JumpScale.grid.serverbase.DaemonClient",
#   "JumpScale.grid.serverbase.Exceptions",
#   "JumpScale.grid.serverbase.ServerBaseFactory",
#   "JumpScale.grid.serverbase.TCPHATransport",
#   "JumpScale.grid.serverbase.returnCodes",
#   "JumpScale.grid.serverbase",
#   "JumpScale.grid.socketserver.QSocketServer",
#   "JumpScale.grid.socketserver.QSocketServerClient",
#   "JumpScale.grid.socketserver",
#   "JumpScale.grid.tipc.TipcFactory",
#   "JumpScale.grid.tipc.TipcServer",
#   "JumpScale.grid.tipc.TipcTransport",
#   "JumpScale.grid.tipc",
#   "JumpScale.grid.tlog.TLOG",
#   "JumpScale.grid.tlog",
#   "JumpScale.grid.tornado.TornadoFactory",
#   "JumpScale.grid.tornado.TornadoServer",
#   "JumpScale.grid.tornado.TornadoTransport",
#   "JumpScale.grid.tornado",
#   "JumpScale.grid.zdaemon.ZDaemon",
#   "JumpScale.grid.zdaemon.ZDaemonAgent",
#   "JumpScale.grid.zdaemon.ZDaemonFactory",
#   "JumpScale.grid.zdaemon.ZDaemonTransport",
#   "JumpScale.grid.zdaemon",
#   "JumpScale.lib",
#   "JumpScale.lib.btrfs.BtrfsExtension",
#   "JumpScale.lib.btrfs",
#   "JumpScale.lib.cisco_ios.CiscoSwitchManager",
#   "JumpScale.lib.cisco_ios.Router",
#   "JumpScale.lib.cisco_ios",
#   "JumpScale.lib.dataprocessors",
#   "JumpScale.lib.dhcp.dhcp",
#   "JumpScale.lib.dhcp",
#   "JumpScale.lib.diskmanager.Diskmanager",
#   "JumpScale.lib.diskmanager",
#   "JumpScale.lib.docker.Docker",
#   "JumpScale.lib.docker",
#   "JumpScale.lib.html.HTML2Text",
#   "JumpScale.lib.html.HTMLFactory",
#   "JumpScale.lib.html",
#   "JumpScale.lib.jail.JailFactory",
#   "JumpScale.lib.jail",
#   "JumpScale.lib.kvm.KVM",
#   "JumpScale.lib.kvm",
#   "JumpScale.lib.lxc.Lxc",
#   "JumpScale.lib.lxc",
#   "JumpScale.lib.mysql.MySQLFactory",
#   "JumpScale.lib.mysql",
#   "JumpScale.lib.nginx.nginx",
#   "JumpScale.lib.nginx",
#   "JumpScale.lib.numtools.NumTools",
#   "JumpScale.lib.numtools",
#   "JumpScale.lib.objectinspector.ObjectInspector",
#   "JumpScale.lib.objectinspector",
#   "JumpScale.lib.osticket.OSTicketFactory",
#   "JumpScale.lib.osticket",
#   "JumpScale.lib.ovsnetconfig.NetConfigFactory",
#   "JumpScale.lib.ovsnetconfig",
#   "JumpScale.lib.ovsnetconfig.VXNet.netclasses",
#   "JumpScale.lib.ovsnetconfig.VXNet.systemlist",
#   "JumpScale.lib.ovsnetconfig.VXNet.tests",
#   "JumpScale.lib.ovsnetconfig.VXNet.utils",
#   "JumpScale.lib.ovsnetconfig.VXNet.vxlan",
#   "JumpScale.lib.ovsnetconfig.VXNet",
#   "JumpScale.lib.platform",
#   "JumpScale.lib.platform.inventoryscan",
#   "JumpScale.lib.platform.inventoryscan.cmdtools.EnumerateResourcesCommand",
#   "JumpScale.lib.platform.inventoryscan.cmdtools.InventoryScanEnums",
#   "JumpScale.lib.platform.inventoryscan.cmdtools",
#   "JumpScale.lib.platform.inventoryscan.manage.Device",
#   "JumpScale.lib.platform.inventoryscan.manage.DeviceHypervisor",
#   "JumpScale.lib.platform.inventoryscan.manage.DeviceOperatingSystem",
#   "JumpScale.lib.platform.inventoryscan.manage.DevicePerformance",
#   "JumpScale.lib.platform.inventoryscan.manage.Disk",
#   "JumpScale.lib.platform.inventoryscan.manage.ISCSIInitiator",
#   "JumpScale.lib.platform.inventoryscan.manage.ISCSITarget",
#   "JumpScale.lib.platform.inventoryscan.manage.InventoryManager",
#   "JumpScale.lib.platform.inventoryscan.manage.Nic",
#   "JumpScale.lib.platform.inventoryscan.manage.Partition",
#   "JumpScale.lib.platform.inventoryscan.manage.PartitionRaid",
#   "JumpScale.lib.platform.inventoryscan.manage.ZFS",
#   "JumpScale.lib.platform.inventoryscan.manage.ZPool",
#   "JumpScale.lib.platform.inventoryscan.manage.ZPoolDisk",
#   "JumpScale.lib.platform.inventoryscan.manage.ZPoolMirror",
#   "JumpScale.lib.platform.inventoryscan.manage",
#   "JumpScale.lib.puppet.PuppetTool",
#   "JumpScale.lib.puppet",
#   "JumpScale.lib.qemu_img.qemu_img",
#   "JumpScale.lib.qemu_img",
#   "JumpScale.lib.rogerthat.rogerthat",
#   "JumpScale.lib.rogerthat",
#   "JumpScale.lib.routeros.RouterOS",
#   "JumpScale.lib.routeros",
#   "JumpScale.lib.sandboxer.Sandboxer",
#   "JumpScale.lib.sandboxer",
#   "JumpScale.lib.sheet.Sheet",
#   "JumpScale.lib.sheet.Sheets",
#   "JumpScale.lib.sheet",
#   "JumpScale.lib.shorewall.shorewall",
#   "JumpScale.lib.shorewall",
#   "JumpScale.portal",
#   "JumpScale.portal.codegentools.CodeGenerator",
#   "JumpScale.portal.codegentools.CodeGeneratorActorClass",
#   "JumpScale.portal.codegentools.CodeGeneratorActorLocal",
#   "JumpScale.portal.codegentools.CodeGeneratorActorRemote",
#   "JumpScale.portal.codegentools.CodeGeneratorActorTasklets",
#   "JumpScale.portal.codegentools.CodeGeneratorBase",
#   "JumpScale.portal.codegentools.CodeGeneratorEnumeration",
#   "JumpScale.portal.codegentools.CodeGeneratorEveModel",
#   "JumpScale.portal.codegentools.CodeGeneratorModel",
#   "JumpScale.portal.codegentools",
#   "JumpScale.portal.docgenerator.Confluence2HTML",
#   "JumpScale.portal.docgenerator.Confluence2RST",
#   "JumpScale.portal.docgenerator.Docgenerator",
#   "JumpScale.portal.docgenerator.Page",
#   "JumpScale.portal.docgenerator.PageAlkira",
#   "JumpScale.portal.docgenerator.PageConfluence",
#   "JumpScale.portal.docgenerator.PageGroup",
#   "JumpScale.portal.docgenerator.PageHTML",
#   "JumpScale.portal.docgenerator.PageRST",
#   "JumpScale.portal.docgenerator.WikiClientAlkira",
#   "JumpScale.portal.docgenerator.WikiClientConfluence",
#   "JumpScale.portal.docgenerator",
#   "JumpScale.portal.docpreprocessor.DocParser",
#   "JumpScale.portal.docpreprocessor.DocPreprocessor",
#   "JumpScale.portal.docpreprocessor.DocPreprocessorFactory",
#   "JumpScale.portal.docpreprocessor",
#   "JumpScale.portal.html.BootStrapForm",
#   "JumpScale.portal.html.GridDataTables",
#   "JumpScale.portal.html.HTMLGalleria",
#   "JumpScale.portal.html.HtmlFactory",
#   "JumpScale.portal.html.elFinder",
#   "JumpScale.portal.html.multipart",
#   "JumpScale.portal.html",
#   "JumpScale.portal.macrolib.blog",
#   "JumpScale.portal.macrolib.div_base",
#   "JumpScale.portal.macrolib",
#   "JumpScale.portal.macrolib.imagelib.ImageLib",
#   "JumpScale.portal.macrolib.imagelib",
#   "JumpScale.portal.macrolib.plantuml",
#   "JumpScale.portal.portal.MacroExecutor",
#   "JumpScale.portal.portal.OsisBeaker",
#   "JumpScale.portal.portal.PortalAuthenticatorOSIS",
#   "JumpScale.portal.portal.PortalClient",
#   "JumpScale.portal.portal.PortalClientWS",
#   "JumpScale.portal.portal.PortalFactory",
#   "JumpScale.portal.portal.PortalRest",
#   "JumpScale.portal.portal.PortalServer",
#   "JumpScale.portal.portal.RequestContext",
#   "JumpScale.portal.portal.auth",
#   "JumpScale.portal.portal",
#   "JumpScale.portal.portalloaders.ActorsInfo",
#   "JumpScale.portal.portalloaders.ActorsLoader",
#   "JumpScale.portal.portalloaders.BucketLoader",
#   "JumpScale.portal.portalloaders.LoaderBase",
#   "JumpScale.portal.portalloaders.PortalLoaderFactory",
#   "JumpScale.portal.portalloaders.SpacesLoader",
#   "JumpScale.portal.portalloaders"
# ]

# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# if True: #on_rtd:
     # sphinx.builders.Builder = DummyBuilder
#     sphinx.builders.Builder.name =  'DummyBuilder'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Jumpscale Doc'
copyright = u'2014, Jumpscale'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '7.0'
# The full version, including alpha/beta/rc tags.
release = '7.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role =

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'JumpscaleDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'JumpscaleDoc.tex', u'Jumpscale Doc Documentation',
   u'jumpscale', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'jumpscaledoc', u'Jumpscale Doc Documentation',[u'jumpscale'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'JumpscaleDoc', u'Jumpscale Doc Documentation',
   u'jumpscale', 'JumpscaleDoc', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Jumpscale Doc'
epub_author = u'Jumpscale'
epub_publisher = u'Jumpscale'
epub_copyright = u'2014, Jumpscale'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'Jumpscale Doc'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}