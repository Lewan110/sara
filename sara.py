#-*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import subprocess
import os.path
import time
from subprocess import Popen, PIPE, STDOUT
import speech_recognition as sr
from os import path
from tendo import singleton
from random import randint
me = singleton.SingleInstance()

reload(sys)  
sys.setdefaultencoding('utf8')


subprocess.call(["/home/pi/speech.sh", " System został uruchomiony"])


def transcribe(duration):

	filename = '/home/pi/test.wav'
	#Przejdź w stan uśpienia jeżeli gra muzyka
	#------------------------------------
	if isAudioPlaying():
		return ""

	

	#Nagraj próbkę dźwięku
	#------------------------------------

    	os.system('arecord -D plughw:1,0 -f cd -c 1 -t wav -d ' + str(duration) + '  -q -r 16000 ' + filename)


	#Sprawdź czy próbka dźwięku jest wystarczająco głośna
	#------------------------------------
	"""
	cmd = 'sox ' + filename + ' -n stat'
	p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	soxOutput = p.stdout.read()
	maxAmpStart = soxOutput.find("Maximum amplitude")+24
	maxAmpEnd = maxAmpStart + 7
	maxAmpValueText = soxOutput[maxAmpStart:maxAmpEnd]
	print "Maksymalna amplituda: " + maxAmpValueText
	maxAmpValue = float(maxAmpValueText)
	time.sleep(0.05)
	#if (maxAmpValue < 0.1) or (0.275 < maxAmpValue < 0.3) :
	if (maxAmpValue < 0.1) :
		#Próbka za cicha - nic nie rób
		return ""	
	"""


	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")

	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)

	#Wyślij próbkę do Google
	#------------------------------------	
	
	try:
		final_result = r.recognize_google(audio, language="pl-PL")
		print("Rozpoznałam tekst jako: " + final_result)
	except sr.UnknownValueError:
		print("Nie rozpoznałam tekstu")
		final_result = ""
	except sr.RequestError as e:
		print("Wystąpił błąd; {0}".format(e))
		final_result = ""
	return final_result

def isAudioPlaying():
	
	audioPlaying = False 

        cmd = 'ps -C omxplayer,mplayer'
	lineCounter = 0
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

        for ln in p.stdout:
		lineCounter = lineCounter + 1
		if lineCounter > 1:
			audioPlaying = True
			break

	return audioPlaying ; 



def listenForCommand(): 
	
	command  = transcribe(3)
	
	print time.strftime("%Y-%m-%d %H:%M:%S ")  + "Komenda: " + command 
	success=True 

	#Ustawienia wszystkich komend i ich akcji
	#------------------------------------	
	
	
	if command.lower().find("powtórz")>-1 :
		subprocess.call(["/home/pi/speech.sh", "Co mam powtórzyć?"])
		os.system("aplay -q -D plughw:0,0 /home/pi/beep.wav")
		command2  = transcribe(5)
		if command2.lower == "" :
					subprocess.call(["/home/pi/speech.sh", "Nic nie zrozumiałam"])
		else:
			subprocess.call(["/home/pi/speech.sh", command2])
				
	elif command.lower().find("odliczanie")>-1 or command.lower().find("alarm")>-1 or command.lower().find("minutnik")>-1 :
				subprocess.call(["/home/pi/speech.sh", "Na ile minut ustawić odliczanie"])
				os.system("aplay -q -D plughw:1,0 /home/pi/beep.wav")
				command2  = transcribe(3)
				os.system('python /home/pi/Sara/timer.py ' + command2)
				
	elif command.lower().find("wiki")>-1 :
				subprocess.call(["/home/pi/speech.sh", "Co chcesz sprawdzić w wikipedii?"])
				os.system("aplay -q -D plughw:1,0 /home/pi/beep.wav")
				command2  = transcribe(4)
				os.system('python /home/pi/Sara/wikipedia.py ' + command2)

	elif command.lower().find("wydarzenia")>-1 or command.lower().find("wiadomości")>-1 :
				subprocess.call(["/home/pi/speech.sh", "Przeczytać wiadomości z polski czy ze świata?"])
				wiadomosci = True
				while wiadomosci:
					os.system("aplay -q -D plughw:1,0 /home/pi/beep.wav")
					command2  = transcribe(3)
					if command2.lower().find("polski")>-1 or command2.lower().find("polska")>-1 :
						os.system('python /home/pi/Sara/rss-polska.py')
						wiadomosci = False
					elif command2.lower().find("świat")>-1 or command2.lower().find("świata")>-1 :
						os.system('python /home/pi/Sara/rss-swiat.py')
						wiadomosci = False
					else:
						subprocess.call(["/home/pi/speech.sh", "Nie rozumiem. Powtórz"])
				
	elif command.lower().find("status")>-1 :
                os.system('python /home/pi/Sara/status.py')
				
	elif command.lower().find("ciekawostka")>-1 or command.lower().find("ciekawostkę")>-1 :
                os.system('python /home/pi/Sara/ciekawostka.py')
	
	elif command.lower().find("cytat")>-1 :
                os.system('python /home/pi/Sara/cytat.py')

	elif command.lower().find("data")>-1 or command.lower().find("datę")>-1 :
                os.system('python /home/pi/Sara/data.py')

	elif command.lower().find("kawał")>-1 or command.lower().find("żart")>-1 :
                os.system('python /home/pi/Sara/kawal.py')
				
	elif command.lower().find("godzina")>-1 or command.lower().find("godzinę")>-1 :
                os.system('python /home/pi/Sara/godzina.py')
				
	elif command.lower().find("euro")>-1 :
                os.system('python /home/pi/Sara/euro.py')

	elif command.lower().find("dolar")>-1 :
                os.system('python /home/pi/Sara/dolar.py')

	elif command.lower().find("restart")>-1 :
                os.system('python /home/pi/Sara/restart.py')

        elif command.lower().find("najlepsza")>-1 :
                os.system('python /home/pi/Sara/fifa.py')


		

	else:
		subprocess.call(["/home/pi/speech.sh", " nie zrozumiałam polecenia"])
		success=False

	return success 





while True:
		
	sys.stdout.flush() 
	
	#Słuchaj słowa klucza
	#------------------------------------	
        spokenText = transcribe(3) ;
	
	if len(spokenText) > 0: 
        	print time.strftime("%Y-%m-%d %H:%M:%S ")  + "Słowo-klucz: " + spokenText

        triggerWordIndex  = spokenText.lower().find("ara")

        if triggerWordIndex >-1:
		#Wykryto słowo-klucz
		#------------------------------------	
                subprocess.call(["/home/pi/speech.sh", " słucham"])
                os.system("aplay -q -D plughw:1,0 /home/pi/beep.wav")
		success = listenForCommand()	
		
		if not success:
			time.sleep(0.01)
