# -*- coding: utf-8 -*-

from query_wrapper import do_post, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class SDL(Translator):
    """
    SDL translator

    """

    available_languages = set(["en", "es", "fr", "ru", "de", "ar", "nl", "pt", "zh", "it"])
    language_wrapper = {"en": "eng", "es": "spa", "fr": "fra", "ru": "rus",
                        "de": "ger", "ar": "ara", "nl": "dut", "pt": "por", "zh": "chi", "it": "ita"}

    content_type = "Content-type: application/json"

    def __init__(self, auth, verbose=False):
        """
        :param auth: Secret key
        :type auth: string
        :param verbose: Show information
        :type verbose: bool

        """
        super(SDL, self).__init__(verbose)
        self.auth = auth

    def get_translation(self, term, source_language, target_language):
        data = '{"text":"'+term\
               +'", "from":"'+self.language_wrapper[source_language]\
               +'", "to":"'+self.language_wrapper[target_language]+'"}'
        b = JSONBuffer()
        response_code = do_post("https://lc-api.sdl.com/translate",
                data,
                [self.auth, self.content_type],
                b.callback,
                encode=False)
        if response_code is OK:
            return [b.content["translation"]], response_code
        else:
            return [], response_code

    def get_languages(self):
        return self.available_languages

    def get_name(self):
        return "SDL"

if __name__ == "__main__":
    from keys import sdl_auth
    sdl = SDL(sdl_auth)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = sdl.translate(translatorTask)
    print translations.__unicode__()