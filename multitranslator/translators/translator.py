from abc import ABCMeta, abstractmethod
import sys
import time
from translation_utils import *
from collections import OrderedDict
from error_codes import *

class Translator:
    """
    The abstract class Translator defines the methods that a translator must implement,
    every implementation of a translator needs to extends this class for a correct behavior.

    """
    __metaclass__ = ABCMeta

    def __init__(self, verbose=False):
        """
        :param verbose: Show information about the current state of the translations
        :type verbose: bool

        """
        self.verbose = verbose

    def translate(self, translatorTask):
        """
        Obtain the TranslatorJob from the required information in translatorTask.
        If verbose is activated, additional information is showed using the error output

        :param translatorTask: The assigned task that the translator performs
        :type translatorTask: TranslatorTask
        :return: The TranslatorJob that contains the translations
        :rtype: TranslatorJob

        """
        start = time.time()
        translations = OrderedDict()
        if self.verbose:
            print>>sys.stderr, self.get_name(), "working..."
        supported_languages = self.get_languages()
        for target_language in translatorTask.target_languages:
            current_start = time.time()
            if target_language in supported_languages:
                translations[target_language], response_code = self.get_translation(translatorTask.term,
                                                                  translatorTask.source_language,
                                                                  target_language)
            else:
                translations[target_language], response_code = [], NOT_SUPPORTED_LANGUAGE
            if self.verbose:
                print>>sys.stderr, self.get_name(), translatorTask.term, target_language, response_code, time.time() - current_start
        final_time = time.time() - start
        return TranslatorJob(self.get_name(), translations, final_time)

    def set_verbose(self, value):
        """
        Change the state of verbose

        :param value: The new value for verbose
        :type value: bool

        """
        self.verbose = value

    @abstractmethod
    def get_translation(self, term, source_language, target_language):
        """
        Obtain a list of translations of term from source_language to target_language,
        and the status code of the translator.
        Recommended the use of quotes for term.

        :param term: Text to be translated
        :type term: string
        :param source_language: The code language for the original language
        :type source_language: string
        :param target_language: The code language for the result language
        :type target_language: string
        :return: A tuple with list of translations and the status code of the translator
        :rtype: tuple (List of string, int)

        """
        pass

    @abstractmethod
    def get_name(self):
        """
        Obtain the name of the translator

        :return: The name of the translator
        :rtype: string

        """
        pass

    @abstractmethod
    def get_languages(self):
        """
        Obtain the list of code languages compatible with this translator

        :return: A list of code languages
        :rtype: List of string
        """
        pass