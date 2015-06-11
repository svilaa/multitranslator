# -*- coding: utf-8 -*-

from mstranslator_module.mstranslator import Translator as MSTranslator
from translation_utils import *
from translator import Translator
from error_codes import *

class Bing(Translator):
    """
    Bing translator using mstranslator_module

    """
    def __init__(self, client_id, client_secret, more_translations=False, max_translations=10, verbose=False):
        """
        :param client_id: Client ID
        :type client_id: string
        :param client_secret: Password
        :type client_secret: string
        :param more_translations: If True, translations done by the users are allowed,
                                  otherwise, only the Bing translation is obtained
        :type more_translations: bool
        :param max_translations: Maximum number of requested translations to the server
        :type max_translations: int
        :param verbose: Shows information
        :type verbose: bool

        """
        super(Bing, self).__init__(verbose)
        self.translator = MSTranslator(client_id, client_secret)
        self.more_translations = more_translations
        self.max_translations = max_translations

    def get_language_names(self):
        return self.translator.get_lang_names(self.translator.get_langs(), 'en')

    def get_language_codes(self):
        return self.translator.get_langs()

    def get_translation(self, term, source_language, target_language):
        try:
            if not self.more_translations:
                translation = self.translator.translate(term, source_language, target_language)
                return [translation], OK
            else:
                content = self.translator.get_translations(term, source_language, target_language)
                print content
                return list(set([elem["TranslatedText"] for elem in content["Translations"]])), OK
        except:
            return [], TIMEOUT

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "Bing"

    def translate(self, translatorTask):
        return super(Bing, self).translate(translatorTask)

if __name__ == "__main__":
    from keys import bing_client_id, bing_client_secret
    bing = Bing(bing_client_id, bing_client_secret, more_translations=True)
    translatorTask = TranslatorTask(term='computer', target_languages=['es'])
    translations = bing.translate(translatorTask)
    print translations.__unicode__()