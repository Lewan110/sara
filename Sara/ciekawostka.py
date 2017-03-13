#-*- coding: utf-8 -*-
##!/usr/bin/env python

import urllib2, subprocess
link = "http://www.deszczowce.pl/skrypty/losowa_ciekawostka.php"



response = urllib2.urlopen(link).read().decode("iso-8859-2").encode("utf-8")
response2 = response.replace("&#45; ","")
response3 = response2.replace("');","")
response4 = response3.replace("document.write('","")
kawal = response4.split("<br />")

# Loop and print each city name.
for linia in kawal:
	subprocess.call(["/home/pi/speech.sh", linia])
