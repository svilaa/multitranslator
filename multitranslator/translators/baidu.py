# -*- coding: utf-8 -*-

from query_wrapper import do_get, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class Baidu(Translator):
    """
    Baidu translator

    """
    language_wrapper = {"en": "en", "es": "spa", "fr": "fra",
                        "ru": "ru", "de": "de", "ar": "ara",
                        "nl": "nl", "pt": "pt","zh": "zh",
                        "it": "it"}

    content_type = "Content-type: application/json"

    def __init__(self, key, verbose=False):
      """
      :param key: Secret key
      :type key: string
      :param verbose: Show information
      :type verbose: bool
      """
      super(Baidu, self).__init__(verbose)
      self.key = key

    def get_translation(self, term, source_language, target_language):
        params = {'client_id': self.key,
                  'from': self.language_wrapper[source_language],
                  'to': self.language_wrapper[target_language],
                  'q': term}

        b = JSONBuffer()
        response_code = do_get("http://openapi.baidu.com/public/2.0/bmt/translate?",
               params,
               [self.content_type],
               b.callback)
        if response_code is OK:
            return [elem["dst"] for elem in b.content["trans_result"]], response_code
        else:
            return [], response_code

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "Baidu"

if __name__ == "__main__":
    from keys import baidu_api_key
    baidu = Baidu(baidu_api_key)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = baidu.translate(translatorTask)
    print translations.__unicode__()