#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import simplejson as json

class TranslatorInformation:
    """
    Manage the status of the terms validated by a translator

    """
    def __init__(self, name, source_terms, languages):
        """
        :param name: The name of the translator
        :type name: string
        :param source_terms: The terms required for the validation
        :type source_terms: List of string
        :param languages: The language codes required for the validation
        :type languages: List of string

        """
        self.name = name
        self.terms = self._init_terms(source_terms, languages)

    def _init_terms(self, source_terms, languages):
        terms = {}
        for term in source_terms:
            terms[term] = {}
            for language in languages:
                terms[term][language] = False
        return terms

    def accept_term(self, term, language):
        """
        Mark as accepted the term for this language

        :param term: The term to be accepted
        :type term: string
        :param language: The language code of the term
        :type language: string

        """
        self.terms[term][language] = True

    def is_accepted(self, term, language):
        """
        Check if the term is accepted for this language

        :param term: The term to be checked
        :type term: string
        :param language: The language of the term
        :type language: string
        :return: True if the term is accepted, otherwise, False
        :rtype: bool

        """
        return self.terms[term][language]

class TranslationValidator:
    """
    Write analysis about about the accuracy of the translators and the success rate for
    every term and language

    """
    def __init__(self, validation_file, separator=False, detailed=False, percentage=False, verbose=False):
        """
        :param validation_file: The filename that contains the required information for the validation
        :type validation_file: string
        :param separator: Add extra lines for a better readability
        :type separator: bool
        :param detailed: Show more information about the statistics
        :type detailed: bool
        :param percentage: The percentages are showed in a most readable style
        :type percentage: bool
        :param verbose: Show information about the current state of the execution
        :type verbose: bool

        """
        with open(validation_file) as json_data:
            self.information = json.load(json_data, 'utf-8')
        self.translators_info = {}
        self.linebreak = '\n' if separator else ''
        self.detailed = detailed
        self.percentage = percentage
        self.verbose = verbose

    def add_directory(self, directory):
        """
        Add all the files with translations inside this directory

        :param directory: The directory with the JSON files
        :type directory: string

        """
        for filename in os.listdir(directory):
            if self.verbose:
                print>>sys.stderr, "Working with", filename
            self.add_translation(os.path.join(directory, filename))

    def _try_create_translator_information(self, name):
        if name not in self.translators_info:
            self.translators_info[name] = TranslatorInformation(name, self.information["valid_translations"].keys(), self.information["languages"]["target_languages"])

    def _write_utf8_encoded(self, file_descriptor, content):
        print >>file_descriptor, content.encode('utf-8')

    def _write_utf8_encoded_without_jumpline(self, file_descriptor, content):
        print >>file_descriptor, content.encode('utf-8'),

    def add_statistic(self, translator_name, current_term, language, translations, valid_translations):
        """
        Add the validated data to the translation information of translator_name

        :param translator_name: The name of the translator
        :type translator_name: string
        :param current_term: The term to be linked with the translator
        :type current_term: string
        :param language: The language code of the translations
        :type language: string
        :param translations: The translations of this translator with the current language
        :type translations: List of string
        :param valid_translations: The correct translations of current_term with the current language
        :type valid_translations: List of string

        """
        found = False
        for current_translation in translations:
            if current_translation in valid_translations:
                found = True
                break
        self._try_create_translator_information(translator_name)
        if found:
            self.translators_info[translator_name].accept_term(current_term, language)

    def add_translation(self, translation_file):
        """
        Validate all the translations inside translation_file and put the results into the corresponding TranslationInfo

        :param translation_file: The JSON file with the translations
        :type translation_file: string

        """
        with open(translation_file) as translation_data:
            translation = json.load(translation_data, 'utf-8')
            current_term = translation["task"]["term"]
            for job in translation["jobs"]:
                for lang_trans in job["languages"]:
                    try:
                        self.add_statistic(job["name"], current_term, lang_trans["code"], lang_trans["translations"], self.information["valid_translations"][current_term][lang_trans["code"]])
                    except KeyError:
                        pass

    def _get_formatted_rate(self, accepted, total):
        if total is 0:
            return "No available information"
        if self.percentage:
            return "%.0f%% (%i of %i)" % (100*accepted/total, accepted, total)
        else:
            return "%.0f\t%i\t%i" % (100*accepted/total, accepted, total)

    def _get_descriptor(self, filename):
        if filename is None or filename is "stdout":
            return sys.stdout
        else:
            return open(filename+'.tsv', 'w')

    def _close_descriptor(self, descriptor):
        if descriptor is not sys.stdout:
            descriptor.close()

    def write_analysis_by_translator(self, filename=None):
        """
        Does an analysis focused on the accuracy of the translators

        :param filename: The filename where the analysis is wrote
        :type filename: string or None, if string is None, the used file descriptor is sys.stdout

        """
        f = self._get_descriptor(filename)
        for translator in self.translators_info.values():
            self._write_utf8_encoded(f, translator.name)
            for language in self.information["languages"]["target_languages"]:
                self._write_utf8_encoded_without_jumpline(f, self.linebreak)
                self._write_utf8_encoded_without_jumpline(f, '\t'+language)
                accepted = 0
                terms_validation_list = []
                for term, langs in translator.terms.items():
                    if language in langs:
                        if self.verbose:
                            print>>sys.stderr, "Working with", translator.name, language, term
                        is_accepted = translator.is_accepted(term, language)
                        if is_accepted: accepted+=1
                        terms_validation_list.append([term, str(is_accepted)])
                self._write_utf8_encoded(f, '\t'+self._get_formatted_rate(accepted, len(translator.terms)))
                if self.detailed:
                    for term_tuple in terms_validation_list:
                        self._write_utf8_encoded(f, '\t\t' + '\t'.join(term_tuple))
        self._close_descriptor(f)

    def write_analysis_by_term(self, filename=None):
        """
        Does an analysis focused on the success rate of the terms

        :param filename: The filename where the analysis is wrote
        :type filename: string or None, if string is None, the used file descriptor is sys.stdout

        """
        f = self._get_descriptor(filename)
        for term in self.information["valid_translations"]:
            self._write_utf8_encoded(f, term)
            for language in self.information["languages"]["target_languages"]:
                self._write_utf8_encoded_without_jumpline(f, '\t'+language)
                accepted = 0
                translators_validation_list = []
                for translator in self.translators_info.values():
                    if self.verbose:
                        print>>sys.stderr, "Working with", term, language, translator.name
                    is_accepted = translator.is_accepted(term, language)
                    if is_accepted: accepted+=1
                    translators_validation_list.append([translator.name, str(is_accepted)])
                self._write_utf8_encoded(f, '\t'+self._get_formatted_rate(accepted, len(self.translators_info)))
                if self.detailed:
                    for translator in translators_validation_list:
                        self._write_utf8_encoded(f, '\t\t' + '\t'.join(translator))
        self._write_utf8_encoded_without_jumpline(f, self.linebreak)
        self._close_descriptor(f)

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True, help="directory with the JSON files that contain the translations")
    parser.add_argument("-tr", "--report-by-translator", nargs='?', const="stdout", type=str, required=False, dest="translator", help="does an analysis focused on the accuracy of the translators")
    parser.add_argument("-te", "--report-by-term", type=str, nargs='?', const="stdout", required=False, dest="term", help="does an analysis focused on the success rate of the terms")
    parser.add_argument("-vf", "--validation-file", type=str, required=True, dest="validation_file", help="the JSON file with the required information for the analysis")
    parser.add_argument("-v", "--verbose", action='store_true', required=False, help="show information about the current state of the execution")
    parser.add_argument("-d", "--detailed", action='store_true', required=False, help="show more information about the statistics")
    parser.add_argument("-s", "--separator", action='store_true', required=False, help="add extra lines for a better readability")
    parser.add_argument("-p", "--percentage", action='store_true', required=False, dest="percentage", help="the percentages are showed in a most readable style")

    return parser.parse_args()

if __name__ == "__main__":
    args = init_parser()

    tv = TranslationValidator(validation_file=args.validation_file,
                              separator=args.separator,
                              detailed=args.detailed,
                              percentage=args.percentage,
                              verbose=args.verbose)

    tv.add_directory(args.input)

    if args.translator:
        tv.write_analysis_by_translator(args.translator)
    if args.term:
        tv.write_analysis_by_term(args.term)