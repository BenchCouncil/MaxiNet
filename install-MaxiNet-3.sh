#!/bin/bash

echo "MaxiNet-3 1.0 installer"
echo ""
echo "This program installs MaxiNet-3 1.0 and all requirements to the home directory of your user"


echo "MaxiNet installer will now install: "
echo " -Containernet 2.2.1 (and Docker as well)"
echo " -Pox 0.7"
echo " -Metis 5.1"
echo " -Pyro 4"
echo " -MaxiNet-3 1.0"
echo ""

echo "##### install python 3 and set to default python #####"
sudo apt-get install python3 -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo apt-get install python3-pip python3-matplotlib -y

echo "##### install required dependencies #####"
sudo apt-get install git autoconf screen cmake build-essential sysstat uuid-runtime -y

echo "##### install containernet (as well as docker) #####"
sudo apt-get install ansible aptitude -y
# Patch config file if necessary
grep "localhost ansible_connection=local" /etc/ansible/hosts >/dev/null
if [ $? -ne 0 ]; then
  echo "localhost ansible_connection=local" | sudo tee -a /etc/ansible/hosts
fi
cd ~
echo "use my containernet branch"
git clone git://github.com/ChengHuangUCAS/containernet.git
cd containernet/ansible
sudo ansible-playbook -i "localhost," -c local install.yml
cd ..
sudo make install


echo "##### install pox #####"
cd ~
git clone git://github.com/noxrepo/pox.git


echo "##### install metis #####"
cd ~
wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
tar -xzf metis-5.1.0.tar.gz
rm metis-5.1.0.tar.gz
cd metis-5.1.0
make config
make
sudo make install
cd ~

echo "##### install pyro #####"
sudo python -m pip install Pyro4


echo "##### install MaxiNet #####"
# NOTICE: assuming MaxiNet-3 repository in cloned to ~/
cd ~/MaxiNet
sudo make install


echo "##### download Dockerfiles #####"
cd ~
git clone git://github.com/ChengHuangUCAS/MaxiNetDockerfile.git

