#-*- coding: utf-8 -*-
from urllib2 import Request, urlopen, URLError
import json, sys, subprocess

article = sys.argv
article = article[1:]
article = '%20'.join(article)
if article == "":
	subprocess.call(["/home/pi/speech.sh", "Nie zrozumiałam szukanego wyrazu"])
	quit()


request = Request('https://pl.wikipedia.org/w/api.php?format=json&utf8&action=query&prop=extracts&exintro=&explaintext=&titles='+article)
try:
    response = urlopen(request)
    data = json.load(response)

    output = data["query"]["pages"]
    if 'extract' not in output[output.keys()[0]] or output[output.keys()[0]]["extract"] == "" :
        subprocess.call(["/home/pi/speech.sh", "Nie znalazłam informacji o wyrażeniu " + article])
        quit()
    final = output[output.keys()[0]]["extract"]
    print final
except URLError, e:
    final = "Wystąpił błąd API wikipedii"

subprocess.call(["/home/pi/speech.sh", final])
