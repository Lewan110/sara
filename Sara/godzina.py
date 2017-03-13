#!/usr/bin/python -*- coding: utf-8 -*-

from datetime import datetime
import os

godzina = datetime.now().strftime('%H:%M:%S')


stream = os.popen('/home/pi/speech.sh Aktualna godzina to ' + godzina)