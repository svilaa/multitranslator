# -*- coding: utf-8 -*-

import goslate
from translation_utils import *
from translator import Translator
from error_codes import *

class Google(Translator):
    """
    Google translator using goslate

    """
    def __init__(self, verbose=False):
        """
        :param verbose: Show information
        :type verbose: bool

        """
        super(Google, self).__init__(verbose)
        self.gs = goslate.Goslate(retry_times=1, timeout=5)

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])
        #return self.gs.get_languages()

    def get_translation(self, term, source_language, target_language):
        try:
            return [self.gs.translate(term, target_language, source_language)], OK
        except:
            return [], TIMEOUT

    def get_name(self):
        return "Google"

    def translate(self, translatorTask):
        return super(Google, self).translate(translatorTask)

if __name__ == "__main__":
    google = Google()
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = google.translate(translatorTask)
    print translations.__unicode__()