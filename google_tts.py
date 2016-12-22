# -*- coding: utf-8 -*-
import subprocess, os, signal, sys

class GoogleTTS():
    def __init__ (self, lang="sv"):
        self.script = "./tts.sh"
        self.lang = lang
        self.output_method = "2>/dev/null"

    def set_language(language):
        self.lang = language

    def speak(self, message):
        cmd = "%s -l %s -m '%s' %s" % (self.script, self.lang, message, self.output_method)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
        p.wait()

