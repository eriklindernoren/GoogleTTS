# -*- coding: utf-8 -*-
import sys
from google_tts import GoogleTTS

voice = GoogleTTS()
if len(sys.argv) == 1:
    voice.speak("What would you like me to say?")
    text = raw_input("Enter text: ")
else:
    text = sys.argv[1]

voice.speak(text)