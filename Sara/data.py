#!/usr/bin/python -*- coding: utf-8 -*-

import os
import commands
status, output = commands.getstatusoutput("date +'%a %d %b' | sed -e 's/Mon/Poniedziałek/g; s/Tue/Wtorek/g; s/Wed/Środa/g;s/Thu/Czwartek/g; s/Fri/Piątek/g; s/Sat/Sobota/g; s/Sun/Niedziela/g;s/Jan/Styczeń/g; s/Feb/Luty/g; s/Mar/Marzec/g; s/Apr/Kwiecień/g;s/May/Maj/g; s/Jun/Czerwiec/g; s/Jul/Lipiec/g; s/Sep/Sierpień/g;s/Aug/Wrzesień/g; s/Oct/Październik/g; s/Nov/Listopad/g;s/Dec/Grudzień/g'")

stream = os.popen('/home/pi/speech.sh Aktualna data to ' + output)