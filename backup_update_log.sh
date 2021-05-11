#! /bin/bash
 
now="$(date +'%Y%m%d')"
cp -u /home/pi/log/"$now"* /media/pi/*/

cd /home/pi/Scan/ && git pull

mac=$(ifconfig | grep ether| awk {'print $2'} | sed -r 's/://g')
url="https://script.google.com/macros/s/AKfycbzuze4yIhfZF02vs_rmmtICdNMr1IYEOjpMBWuSq8-ax1yth6Mrr3cR/exec?id="
url_final=$url$mac
curl $url_final
