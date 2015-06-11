# -*- coding: utf-8 -*-

from corrector_configuration import *

void_string = u''

class Corrector:
    """
    Corrector class tries to remove or repair invalid translations using the assigned filters

    """
    def __init__(self, filters=default_filters, available_languages=corrector_available_languages):
        """
        :param filters: Filters used by the corrector
        :type filters: dictionary, keys are strings, values are lists of AbstractFilter
        :param available_languages: Languages supported by the corrector
        :type available_languages: set of string

        """
        self.filters = filters
        self.available_languages = corrector_available_languages

    def apply_filters(self, term, filters_type):
        """
        Apply the filters of type filters_type
        :param term: The term to be corrected
        :type term: string
        :param filters_type: The set of filters used
        :type filters_type: string
        :return: The corrected term
        :rtype: string

        """
        corrected_term = term
        for current_filter in self.filters[filters_type]:
            corrected_term = current_filter.apply(corrected_term)
        return corrected_term

    def is_same_or_void(self, term, original_term):
        """
        Return if term is equal to original_term or void

        :param term: Text to be checked
        :type term: string
        :param original_term: Text to compare
        :type original_term: string
        :return: True if term is equal to original term or void, otherwise, False
        :rtype: bool

        """
        return term == original_term or term == void_string

    def apply_all(self, term, original_term, language=None):
        """
        Executes all the filters in order, checking for every set if is equal to
        original_term or void

        :param term: Text to be corrected
        :type term: string
        :param original_term: Text to compare
        :type original_term: string
        :param language: The language code of the terms
        :type language: string
        :return: The corrected term
        :rtype: string

        """
        if language is not None and language not in self.available_languages:
            return term
        corrected_term = term
        if self.is_same_or_void(corrected_term, original_term):
            return void_string
        for filters in self.filters.keys():
            corrected_term = self.apply_filters(corrected_term, filters)
            if self.is_same_or_void(corrected_term, original_term):
                return void_string
        return corrected_term

if __name__ == "__main__":
    corrector = Corrector()
    print corrector.apply_all(u"hola.", u'hello')
    print corrector.apply_all(u"Hello", u'hello')