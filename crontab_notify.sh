#! /bin/bash

url='https://script.google.com/macros/s/AKfycbw7kzX-9vdikkEBVQIPiFqUQFj00q_dGDGetQWeDGpaJK9sxPUMQWOQQq1fD_DnVAg3/exec'
mac=$(sudo ifconfig wlan0 | grep ether| awk {'print $2'} | sed -r 's/://g')
commit=$(cd /home/pi/Scan && git log -1 | tail -n 1| sed -r 's/\ /_/g')
url_final=$url"?id="$mac"&commit="$commit
curl $url_final
