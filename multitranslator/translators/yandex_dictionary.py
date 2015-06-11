# -*- coding: utf-8 -*-

from query_wrapper import do_get, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class YandexDict(Translator):
    """
    Yandex Dictionary

    """
    content_type = "Content-type: text/plain"

    supported_target_languages = set(["en","es","it","fr","ru","nl","pt","de"])

    def __init__(self, private_key, verbose=False):
        """
        :param private_key: Secret key
        :type private_key: string
        :param verbose: Show information
        :type verbose: bool

        """
        super(YandexDict, self).__init__(verbose)
        self.private_key = private_key

    def _get_terms(self, term, content):
        words = []
        if "def" in content:
            for definition in content["def"]:
                for translate in definition["tr"]:
                    if term.lower() != translate["text"]:   # try tr field
                        words.append(translate["text"])
                    if "syn" in translate:                  # try syn field
                        for synonym in translate["syn"]:
                            if term != synonym["text"]:
                                words.append(synonym["text"])
        return words

    def get_translation(self, term, source_language, target_language):
        if target_language not in self.supported_target_languages:
            return [], NOT_SUPPORTED_LANGUAGE
        params = {'key': self.private_key,
                  'text': term,
                  'lang': source_language + '-' + target_language}

        b = JSONBuffer()
        response_code = do_get("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?",
               params,
               [self.content_type],
               b.callback)
        if response_code is OK:
            return self._get_terms(term, b.content), response_code
        else:
            return [], response_code

    def get_languages(self):
        return self.supported_target_languages

    def get_name(self):
        return "Yandex dictionary"

if __name__ == "__main__":
    from keys import yandex_dict_private_key
    yandex_dict = YandexDict(yandex_dict_private_key)
    translatorTask = TranslatorTask("computer", target_languages=["es"])
    translations = yandex_dict.translate(translatorTask)
    print translations.__unicode__()