#-*- coding: utf-8 -*-
##!/usr/bin/env python

import subprocess
import feedparser
import time 


d = feedparser.parse('http://wiadomosci.wp.pl/kat,1342,rss.xml')

introMessage = "Wiadomości dnia z godziny" + time.strftime("%H:%M") 

subprocess.call(["/home/pi/speech.sh", introMessage])

maxItems = 5
itemCounter = 0 

for post in d.entries:
 print post.title
 subprocess.call(["/home/pi/speech.sh", post.title])
 itemCounter = itemCounter + 1
 if itemCounter == maxItems:
  break