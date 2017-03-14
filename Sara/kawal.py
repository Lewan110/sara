#-*- coding: utf-8 -*-
##!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import subprocess
link = "http://www.deszczowce.pl/skrypty/losowy_zart.php"



response = urlopen(link).read().decode("iso-8859-2").encode("utf-8")
response2 = response.replace("&#45; ","")
response3 = response2.replace("');","")
response4 = response3.replace("document.write('","")
kawal = response4.split("<br />")

# Loop and print each city name.
for linia in kawal:
	#subprocess.call(["/home/pi/speech.sh", linia])
    print(linia)
