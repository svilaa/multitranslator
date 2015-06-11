# -*- coding: utf-8 -*-

import sys
from dict_cc_module.dictcc.dictcc import *
from translation_utils import *
from translator import Translator
from error_codes import *
import urllib2

class Dict_CC(Translator):
    """
    Dict.cc translator using dict_cc_module

    """
    def __init__(self, exactly_term=True, verbose=False):
        """
        :param exactly_term: Save only translations where the original obtained term is the same
        :type exactly_term: bool
        :param verbose: Show information
        :type verbose: bool

        """
        super(Dict_CC, self).__init__(verbose)
        self.exactly_term = exactly_term
        self.dictcc = Dict()

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt"])

    def _are_same_languages(self, own_language, results_language):
        return AVAILABLE_LANGUAGES[own_language] == results_language.lower()

    def _get_words(self, term, order, tuples):
        source = not order
        target = order
        words = []
        for pair in tuples:
            if not self.exactly_term or pair[source] == term:
                words.append(pair[target].decode('utf-8'))
        return words

    def get_translation(self, term, source_language, target_language):
        try:
            results = self.dictcc.translate(urllib2.quote(term), source_language, target_language)
            if results.n_results is 0:
                return [], NO_CONTENT
            words = self._get_words(term, self._are_same_languages(source_language, results.from_lang), results.translation_tuples)
            return words, OK
        except:
            return [], TIMEOUT

    def get_name(self):
        return "Dict.cc"

    def translate(self, translatorTask):
        return super(Dict_CC, self).translate(translatorTask)

if __name__ == "__main__":
    dict_cc = Dict_CC(exactly_term=False)
    translatorTask = TranslatorTask("owl", target_languages=["es"])
    translations = dict_cc.translate(translatorTask)
    print translations.__unicode__()
