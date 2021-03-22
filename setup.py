import sys, subprocess,distutils
from setuptools import setup, find_packages
from tempfile import NamedTemporaryFile

setup(name='MaxiNet-3',
      version='1.0',
      description='Distributed Software Defined Network Emulation (Python 3)',
      long_description="MaxiNet extends the famous Mininet emulation environment to span the emulation across several physical machines. This allows to emulate very large SDN networks. MaxiNet-3 is based on MaxiNet 1.2, and transplanted to Python 3.8.",
      classifiers=[
        'Programming Language :: Python :: 3.8',
      ],
      keywords='mininet MaxiNet SDN Network OpenFlow openvswitch',
      url='https://github.com/ChengHuangUCAS/MaxiNet',
      author_email='huangcheng14@mails.ucas.edu.cn',
      packages=find_packages(),
      install_requires=[
          'Pyro4',
      ],
      include_package_data=True,
      package_data={
        "MaxiNet":["Scripts/*"],
      },
      entry_points={
        'console_scripts': [
            'MaxiNetWorker = MaxiNet.WorkerServer.server:main',
            'MaxiNetFrontendServer = MaxiNet.FrontendServer.server:main',
            'MaxiNetStatus = MaxiNet.WorkerServer.server:getFrontendStatus',
        ]
      },
      zip_safe=False)

if((__name__=="__main__") and (sys.argv[1] == "install")):
    # We need to make package_data files executable...
    # Ugly hack:
    f = NamedTemporaryFile('w+t')
    f.write("""
import os,subprocess
print "Setting executable bits..."
from MaxiNet.tools import Tools
d = Tools.get_script_dir()
for f in filter(lambda x: x[-3:]==".sh",os.listdir(d)):
    print f
    subprocess.call(["sudo","chmod","a+x",d+f])
""")
    f.flush()
    subprocess.call(["python",fn])
    f.close()
