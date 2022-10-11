#!/bin/bash

# Install script for Mininet Vagrant VM
# Adapted from https://github.com/kaichengyan/mininet-vagrant

MININET_VERSION="2.3.0"
POX_VERSION=angler

sudo apt-get update
sudo apt-get install -y python2 python-is-python2 unzip net-tools
git clone https://github.com/mininet/mininet
(cd mininet && git checkout $MININET_VERSION)
sed -i 's+git://github.com/mininet/openflow+https://github.com/mininet/openflow+g' mininet/util/install.sh
mininet/util/install.sh -nfvp
pushd pox
git checkout $POX_VERSION
popd

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python get-pip.py
rm -f get-pip.py

sudo pip install pathlib
sudo pip install twisted
sudo pip install ltprotocol
sudo apt-get install traceroute

sudo apt-get install -y dos2unix
printf "Using dos2unix to convert files to Unix format if necessary..."
find /vagrant -name "*" -type f | xargs dos2unix -q
