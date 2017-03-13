#-*- coding: utf-8 -*-
##!/usr/bin/env python

import psutil
import datetime
import subprocess



cpu_percent = psutil.cpu_percent(interval=0.4)
memory_percent = psutil.virtual_memory()[2]

#response = "Aktualne obciążenie procesora wynosi %s procent." %cpu_percent
#response = response.replace(".0","")
response2 = "W użyciu jest %s procent pamięci operacyjnej." %memory_percent
response2 = response2.replace(".0","")

def uptime():
 
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "dzień" or "dni" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "godzinę" or "godzin" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minutę" or "minut" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "sukundę" or "sekund" )
 
     return string;
 
response3 =  "Od ostatniego restartu minęło " + uptime()
#print response
print response2
print response3

#subprocess.call(["/home/pi/speech.sh", response])
subprocess.call(["/home/pi/speech.sh", response2])
subprocess.call(["/home/pi/speech.sh", response3])