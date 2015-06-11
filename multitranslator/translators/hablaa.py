# -*- coding: utf-8 -*-

from translation_utils import *
from translator import Translator
from query_wrapper import JSONBuffer
import httplib2
import urllib
from error_codes import *

class Hablaa(Translator):
    """
    Hablaa translator

    """
    language_wrapper = {"en": "eng", "es": "spa", "fr": "fra",
                        "ru": "rus", "de": "deu", "ar": "ara",
                        "nl": "nld", "pt": "por","zh": "zho",
                        "it": "ita"}

    def __init__(self, verbose=False):
        """
        :param verbose: Show information
        :type verbose: bool

        """
        super(Hablaa, self).__init__(verbose)

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_translation(self, term, source_language, target_language):
        src = self.language_wrapper[source_language]
        tgt = self.language_wrapper[target_language]
        params = term + "/" + src + "-" + tgt + "/"
        URL = "http://hablaa.com/hs/translation/"
        h = httplib2.Http(timeout=5)
        try:
            response, content = h.request(URL + urllib.quote(params), "GET")
            translator_code = int(response['status'])
            if translator_code is OK:
                b = JSONBuffer()
                b.callback(content)
                return [term['text'] for term in b.content], translator_code
            else:
                return [], translator_code
        except:
            return [], TIMEOUT

    def get_name(self):
        return "Hablaa"

    def translate(self, translatorTask):
        return super(Hablaa, self).translate(translatorTask)

if __name__ == "__main__":
    hablaa = Hablaa()
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = hablaa.translate(translatorTask)
    print translations.__unicode__()