# -*- coding: utf-8 -*-

from translation_utils import *
from translator import Translator
from urllib import urlencode
import httplib2
import xml.etree.ElementTree as ET
from error_codes import *

class Glosbe(Translator):
    """
    Glosbe translator

    """
    format = "xml"
    pretty = "false"

    def __init__(self, verbose=False):
        """
        :param verbose: Show information
        :type verbose: bool

        """
        super(Glosbe, self).__init__(verbose)

    def get_translation(self, term, source_language, target_language):

        params = {'from': source_language,
                  'dest': target_language,
                  'phrase': term,
                  'format': self.format,
                  'pretty': self.pretty
                 }

        h = httplib2.Http(timeout=10)
        try:
          response, content = h.request("https://glosbe.com/gapi/translate?" + urlencode(params), "GET")
          tree = ET.fromstring(content)
          try:
            words = []
            it = tree.iter('com.google.common.collect.RegularImmutableMap')
            for elem in it:
              words.append(elem.find('values').find('string').text)
            return words, int(response['status'])
          except StopIteration:
            return [], NO_CONTENT
        except:
          return [], TIMEOUT

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "Glosbe"

if __name__ == "__main__":
    glosbe = Glosbe()
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = glosbe.translate(translatorTask)
    print translations.__unicode__()