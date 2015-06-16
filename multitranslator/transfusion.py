# -*- coding: utf-8 -*-
"""
Transfusion is the main module of MultiTranslator, it is a set of functions used to 
configure an launch translations, avoiding the headaches of the individual 
implementations of the translators and how the data is managed.

"""

import copy
try:
    import pathos.multiprocessing as mp
except ImportError:
    pass

from translators.settings import *
from translators.translation_utils import *
from corrector.corrector import *

default_supported_languages = {'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Portuguese': 'pt', 'Chinese': 'zh',
            'Russian': 'ru', 'Arabic': 'ar', "German": 'de', "Italian": 'it', "Dutch": 'nl'}

class Transfusion:
    """__init__(self, translators=<List of translators>, verbose=False, corrector=<Corrector>)
    
    :param translators: A list with the desired translators
    :type translators: List of Translator
    :param verbose: Shows information about the state of the translations
    :type verbose: bool
    :param corrector: Corrector used to filter the translations
    :type corrector: Corrector

    """
    def __init__(self, translators=default_translators.values(), verbose=False, corrector=Corrector()):
        self.translators = translators
        self.verbose = verbose
        self.set_verbose(self.verbose)
        self.corrector = corrector

    def set_translators(self, translators):
        """
        Replace the current translators

        :param translators: The new translators
        :type translators: List of Translator
        """
        self.translators = translators
        self.set_verbose(self.verbose)

    def set_verbose(self, value):
        """
        Update the verbose flag

        :param value: The new state for verbose
        :type value: bool
        """
        self.verbose = value
        for translator in self.translators:
            translator.set_verbose(self.verbose)

    def get_translation(self, translatorTask, correct=False):
        """
        Translates the required term from the source language to the target languages

        :param translatorTask: The required information to perform the translation
        :type translatorTask: TranslatorTask
        :param correct: Apply or not the corrector
        :type correct: bool
        :return: The set of translations for each language and translator, including the original task
        :rtype: Translation

        """
        translations = []
        for translator in self.translators:
            translations.append(translator.translate(translatorTask))
        translation = Translation(translatorTask, translations)
        if correct:
            translation = self.get_correction(translation)
        return translation

    def _execute(self, args):
        return args[0].translate(args[1])

    def get_concurrent_translation(self, translatorTask, threads, correct=False):
        """
        Concurrent execution of the translation process. This function requires pathos.multiprocessing library

        :param translatorTask: The required information to perform the translation
        :type translatorTask: TranslatorTask
        :param threads: The number of threads. If is lower than 1, only 1 thread will work.
        :type threads: int
        :param correct: Apply or not the corrector
        :param correct: bool
        :return: The set of translations for each language and translator, including the original task
        :rtype: Translation

        """
        if threads <= 0:
            threads = 1
        pool = mp.ProcessingPool(threads)
        tasks = []
        for translator in self.translators:
            tasks.append((translator,translatorTask))
        jobs = pool.map(self._execute, tasks)
        translation = Translation(translatorTask, jobs)
        if correct:
            translation = self.get_correction(translation)
        return translation

    def get_correction(self, translation):
        """
        Apply the filters of the corrector to try to remove or repair invalid translations

        :param translation: The translation information sent to the corrector
        :type translation: Translation
        :return: A copy of the original translation with the filters of the corrector applied
        :rtype: Translation

        """
        correction = copy.deepcopy(translation)
        original_term = translation.translator_task.term
        for job in correction.jobs:
            for lang, trans in job.translations.iteritems():
                for i, tran in enumerate(trans):
                    trans[i] = self.corrector.apply_all(tran, original_term, lang)
            for lang in job.translations:
                job.translations[lang] = filter(None, job.translations[lang])
        return correction