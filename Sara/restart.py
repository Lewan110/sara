#!/usr/bin/python -*- coding: utf-8 -*-

import os

stream = os.popen('/home/pi/speech.sh Procedura restartu została uruchomiona')
os.system('sudo reboot')


