#! /bin/bash
 
now="$(date +'%Y%m%d')"
cp -u /home/pi/log/"$now"* /media/pi/*/

cd /home/pi/Scan/ && git pull

url='https://script.google.com/macros/s/AKfycbx1hU4T2L4_nmlKJp-NENxifkcJhKJk7Fe0uWApZi3ZrIsdUq2ROc1xT7-PVXZO2-iH/exec'
mac=$(ifconfig wlan0 | grep ether| awk {'print $2'} | sed -r 's/://g')
commit=$(git log -1 | tail -n 1| sed -r 's/\ /_/g')
url_final=$url"?id="$mac"&commit="$commit
curl $url_final
