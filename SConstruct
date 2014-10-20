import glob
import os

import IEEnv

import VersionControl
VersionControl.setVersion('IEBuild', '6.15.1')
import IEBuild

majorVersion = '0'
minorVersion = '0'
patchVersion = '1'

versionParts = {'major':majorVersion, 'minor':minorVersion, 'patch':patchVersion}
version = '{major}.{minor}.{patch}'.format(**versionParts)

application = 'xcorder'

if "INSTALLPREFIX" not in ARGUMENTS:
	if ARGUMENTS.get("RELEASE", "0") == "1" :
		ARGUMENTS["INSTALLPREFIX"] = "{root}/apps/{application}/{version}/".format(
			root=IEEnv.Environment.rootPath(),
			application=application,
			version=version,
		)
	else:
		ARGUMENTS["INSTALLPREFIX"] = "{home}/apps/{application}/{version}/".format(
			home=os.path.expanduser("~"),
			application=application,
			version=version,
		)
else:
	ARGUMENTS["INSTALLPREFIX"] = "{prefix}/apps/{application}/{version}/".format(
		prefix=ARGUMENTS["INSTALLPREFIX"],
		application=application,
		version=version,
	)

program = IEBuild.Buildable(
	ARGUMENTS,
)
env = program.finalize()

source = []
for pattern in ['*.py', '*.svg', '*.qss', 'README.*', '*LICENSE*', 'xcorder']:
	env.Install(ARGUMENTS['INSTALLPREFIX'], glob.glob(pattern))

env.Alias('install', ARGUMENTS['INSTALLPREFIX'])
