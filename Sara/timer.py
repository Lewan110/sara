#-*- coding: utf-8 -*-
##!/usr/bin/env python

import subprocess, sys, re, os
import json, urllib2

czas = sys.argv
czas = czas[1:]
czas = ' '.join(czas)
if not re.findall('\d+', czas):
	subprocess.call(["/home/pi/speech.sh", "Nie zrozumiałam. Odliczanie nie zostało ustawione"])
	quit()

czas = re.findall('\d+', czas)
czas = ''.join(czas)
os.system('/home/pi/speech.sh "Ustawiam odliczanie na ' + czas + ' minut"')
os.system('sleep ' + czas + 'm && aplay /home/pi/alarm.wav && /home/pi/speech.sh "Minęło już ' + czas + ' minut od ustawienia odliczania" &')
