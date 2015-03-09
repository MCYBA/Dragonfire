#!/usr/bin/python
import sys
import api
from lxml import etree
from api import Data
from subprocess import call
import time
import subprocess
import urllib2
import wikipedia
from random import randint

def command(speech_object):
	previous_command = ""
	while(True):
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			if (previous_command == com):
				continue
			print com
			if (com == "DRAGON FIRE"):
				tts_kill()
				userin = Data([" "]," ")
				words_dragonfire = {
					0 : "Yes, master.",
					1 : "Yes. I'm waiting.",
					2 : "What is your orders?"
				}
				userin.say(words_dragonfire[randint(0,2)])
			if (com == "WHAT IS YOUR NAME"):
				tts_kill()
				userin = Data([" "]," ")
				userin.say("My name is Dragon Fire.")
				previous_command = com
			if (com == "WHAT IS YOUR GENDER"):
				tts_kill()
                                userin = Data([" "]," ")
                                userin.say("I have a female voice but I don't have a gender identity. I'm a computer program sir.")
                                previous_command = com
        		if (com == "OPEN FILE MANAGER"):
				tts_kill()
				userin = Data(["pantheon-files"],"File Manager")
				userin.say("File Manager")
				userin.interact(0)
				previous_command = com
			if (com == "OPEN WEB BROWSER"):
				tts_kill()
				userin= Data(["sensible-browser"],"Web Browser")
				userin.say("Web Browser")
				userin.interact(0)
				previous_command = com
			if (com == "SHUT DOWN THE COMPUTER"):
				tts_kill()
                                userin= Data(["sudo","poweroff"],"Shutting down")
                                userin.say("Shutting down")
				userin.interact(3)
                                previous_command = com
			if (com.startswith("SEARCH FOR")):
				tts_kill()
				userin = Data(["sensible-browser","http://en.wikipedia.org/wiki/"+com[11:].lower()],com[11:])
				userin.interact(0)
				
				try:
					wikipage = wikipedia.page(com[11:].lower())
					wikicontent = "".join([i if ord(i) < 128 else ' ' for i in wikipage.content])
					userin.say(wikicontent)
            				previous_command = com
				except:
					pass
			

def tts_kill():
	call(["pkill", "audsp"])
	call(["pkill", "aplay"])

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
