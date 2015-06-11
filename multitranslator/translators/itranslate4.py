# -*- coding: utf-8 -*-

from query_wrapper import do_get, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class ITranslate(Translator):
    """
    iTranslate4 translator

    """
    content_type = "Content-type: text/json"

    def __init__(self, auth, domain='general', min_results=1, max_results=1, verbose=False):
        """
        In general, min_results and max_results must be equal to obtain the minimum number
        of translations required

        :param auth: Secret key
        :type auth: string
        :param domain: Subject of the terms, currently only general is available
        :type domain: string
        :param min_results: Minimum number of results
        :type min_results: int
        :param max_results: Maximum number of results
        :type max_results: int
        :param verbose: Show information
        :type verbose: bool
        """
        super(ITranslate, self).__init__(verbose)
        self.auth = auth
        self.domain = domain
        self.min_results = min_results
        self.max_results = max_results

    def get_translation(self, term, source_language, target_language):

        params = {'auth': self.auth,
                  'src': source_language,
                  'trg': target_language,
                  'dom': self.domain,
                  'min': self.min_results,
                  'max': self.max_results,
                  'dat': term}

        b = JSONBuffer()
        response_code = do_get("http://itranslate4.eu/api/Translate?",
               params,
               [self.content_type],
               b.callback)
        if response_code is OK:
          words = []
          for text in b.content['dat']:
            words.append(text['text'][0])
          return words, response_code
        else:
          return [], response_code

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "iTranslate4"

if __name__ == "__main__":
    from keys import itranslate_key
    itranslate = ITranslate(itranslate_key, domain='general',min_results=3, max_results=3)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = itranslate.translate(translatorTask)
    print translations.__unicode__()