# -*- coding: utf-8 -*-

from query_wrapper import Buffer, do_get
from translation_utils import *
from translator import Translator
from error_codes import *

class WorldLingoGlossaries:
    GENERAL                 = 'gl1'
    AUTOMOTIVE              = 'gl2'
    AVIATION_SPACE          = 'gl3'
    CHEMISTRY               = 'gl4'
    COLLOQUIAL              = 'gl5'
    COMPUTERS_IT            = 'gl6'
    EARTH_SCIENCES          = 'gl7'
    ECONOMICS_BUSINESS      = 'gl8'
    ELECTRONICS             = 'gl9'
    FOOD_SCIENCE            = 'gl10'
    LEGAL                   = 'gl11'
    LIFE_SCIENCES           = 'gl12'
    MATHEMATICS             = 'gl13'
    MECHANICAL_ENGINEERING  = 'gl14'
    MEDICINE                = 'gl15'
    METALLURGY              = 'gl16'
    MILITARY_SCIENCE        = 'gl17'
    NAVAL_MARITIME          = 'gl18'
    PHOTOGRAPHY_OPTICS      = 'gl19'
    PHYSICS_ATOMIC_ENERGY   = 'gl20'
    POLITICAL_SCIENCE       = 'gl21'

class WorldLingo(Translator):
    """
    WorldLingo translator

    """
    content_type = "Content-type: text/plain"
    supported_languages = {"zh": "zh_CN"}

    def __init__(self, key, glossary=WorldLingoGlossaries.GENERAL, verbose=False):
        """
        :param key: Secret key
        :type key: string
        :param glossary: Scope of the translations. Use WorldLingoGlossaries to obtain the available glossaries.
        :type glossary: string
        :param verbose: Show information
        :type verbose: bool

        """
        super(WorldLingo, self).__init__(verbose)
        self.key = key
        self.glossary = glossary

    def get_language(self, lang):
        return lang if lang not in self.supported_languages else self.supported_languages[lang]

    def get_translation(self, term, source_language, target_language):
        params = {'wl_data': term,
                  'wl_password': self.key,
                  'wl_srclang': self.get_language(source_language),
                  'wl_trglang': self.get_language(target_language),
                  'wl_gloss':self.glossary}
        b = Buffer()
        response_code = do_get("http://www.worldlingo.com/S000.1/api?", params, [self.content_type], b.callback)

        decoded_content = [line.decode('utf-8') for line in b.content.splitlines()]
        if response_code is OK and int(decoded_content[0]) is 0:
            return [decoded_content[1]], response_code
        else:
            return [], response_code

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "WorldLingo"

if __name__ == "__main__":
    from keys import worldlingo_key
    worldlingo = WorldLingo(worldlingo_key, glossary='')
    translatorTask = TranslatorTask("nut", target_languages=["es"])
    translations = worldlingo.translate(translatorTask)
    print translations.__unicode__()