#!/bin/bash

if ! [[ "18.04 20.04 22.04 22.10" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

if [ -e /etc/apt/sources.list.d/mssql-release.list ];
then
    echo "/etc/apt/sources.list.d/mssql-release.list is already exists"
    exit;
fi

curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > ./mssql-release.list

if [ ! -e /etc/apt/sources.list.d ];
then
    sudo mkdir /etc/apt/sources.list.d/
fi
sudo cp ./mssql-release.list /etc/apt/sources.list.d

sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18

# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc

# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev
