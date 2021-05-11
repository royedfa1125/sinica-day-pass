#! /bin/bash
 
now="$(date +'%Y%m%d')"
cp -u /home/pi/log/"$now"* /media/pi/*/
