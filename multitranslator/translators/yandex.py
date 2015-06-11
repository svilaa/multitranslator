# -*- coding: utf-8 -*-

from query_wrapper import do_post, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class Yandex(Translator):
    """
    Yandex translator

    """
    content_type = "Content-type: application/x-www-form-urlencoded"

    def __init__(self, private_key, verbose=False):
        """
        :param private_key: Secret key
        :type private_key: string
        :param verbose: Show information
        :type verbose: bool

        """
        super(Yandex, self).__init__(verbose)
        self.private_key = private_key

    def get_translation(self, term, source_language, target_language):
        post_data = {'key': self.private_key,
                     'lang': source_language + "-" + target_language,
                     'text': term}

        b = JSONBuffer()
        response_code = do_post("https://translate.yandex.net/api/v1.5/tr.json/translate",
                post_data,
                [self.content_type],
                b.callback)

        if response_code is OK:
            translation_code = b.content["code"]
            if translation_code is OK:
                return [b.content["text"][0]], response_code
            else:
                return [], translation_code
        else:
            return [], response_code

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "Yandex"

if __name__ == "__main__":
    from keys import yandex_private_key
    yandex = Yandex(yandex_private_key)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = yandex.translate(translatorTask)
    print translations.__unicode__()