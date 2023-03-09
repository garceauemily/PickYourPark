#! /bin/sh
sudo apt-get install unzip patch xsltproc gcc libreadline-dev python-dev python-setuptools
cd python-mercuryapi
sudo make
sudo make install
cd ../