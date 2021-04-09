#!/usr/bin/python2

#
# This example shows how to use MaxiNet's CommandLineInterface (CLI).
# Using the CLI, commands can be run interactively at emulated hosts.
# Thanks to our build-in py command you can dynamically change the
# topology.
#

from MaxiNet.Frontend import maxinet
from MaxiNet.tools import FatTree
from mininet.node import OVSSwitch

topo = FatTree(4, 10, 0.1)
cluster = maxinet.Cluster()

exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

exp.CLI(locals(), globals())


exp.stop()
