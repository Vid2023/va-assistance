# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:08:33 2023

@author: Vidya
"""
from __future__ import print_function
import datetime

import pyttsx3
import speech_recognition as sr
#import pytz
import subprocess
import os



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()




def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])



print("Start")

while(get_audio()!="stop app"):# True:
    print("Listening")
    text = get_audio()

   
    NOTE_STRS = ["make a note", "write this down", "remember this"]
    for phrase in NOTE_STRS:
        if phrase in text:
            speak("What would you like me to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that.")
    CAL_STRS=["want to compute","calc","calculator"]
    for phrase in CAL_STRS:
        if phrase in text:
            speak("i AM OPENING CALCULATOR FOR YOU")
            subprocess.Popen(["calc.exe"])
            #speak("I've made a note of that.")
    MUSIC_STRS=["play music","play mp3","song please"]
    for phrase in MUSIC_STRS:
        if phrase in text:
            speak("opening media player for you")
            subprocess.Popen(["C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"])
            #(["wmplayer.exe"])


'''p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE, text=True)
out, err = p.communicate()

for line in out.splitlines():
    if 'notepad' in line:
        pid = int(line.split(None, 1)[0])    
        os.kill(pid, signal.SIGKILL)  '''

#Contact: tim@techwithtim.net 