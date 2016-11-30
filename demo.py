# -*- coding: utf-8 -*-
import sys
from google_tts import GoogleTTS

voice = GoogleTTS()
if len(sys.argv) == 1:
    voice.speek("Vad vill du att jag ska säga?")
    text = raw_input("Enter text: ")
else:
    text = sys.argv[1]

voice.speek(text)