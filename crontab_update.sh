#! /bin/bash

cd /home/pi/Scan
cp DeviceName.txt DeviceName
git checkout DeviceName.txt
git pull
cp DeviceName DeviceName.txt
