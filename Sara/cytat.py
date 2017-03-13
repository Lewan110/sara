#-*- coding: utf-8 -*-
##!/usr/bin/env python

import urllib2, subprocess, cgi
link = "http://www.deszczowce.pl/skrypty/losowy_cytat.php"



response = urllib2.urlopen(link).read().decode("iso-8859-2").encode("utf-8")
response2 = response.replace("&#45; ","")
response3 = response2.replace("');","")
response4 = response3.replace("<i>","")
response5 = response4.replace("</i>","")
response6 = response5.replace("<b>","powiedział ")
response7 = response6.replace("</b>","")
response8 = response7.replace("document.write('","")
kawal = response8.split("<br />")

# Loop and print each city name.
for linia in kawal:
	subprocess.call(["/home/pi/speech.sh", linia])
