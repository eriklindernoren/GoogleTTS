# -*- coding: utf-8 -*-
import subprocess, os, signal, sys

class GoogleTTS():
    def __init__ (self, lang="sv"):
        self.script = "./tts.sh"
        self.lang = lang
        self.output_method = "&>/dev/null"

    def setLanguage(language):
        self.lang = language

    def speek(self, message):
        cmd = "%s -l %s -m '%s' %s" % (self.script, self.lang, message, self.output_method)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
        p.wait()

voice = GoogleTTS()
if len(sys.argv) == 1:
    voice.speek("Vad vill du att jag ska säga?")
    text = raw_input("Enter text: ")
else:
    text = sys.argv[1]

voice.speek(text)

