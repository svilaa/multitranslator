# -*- coding: utf-8 -*-

import json
import io
from query_wrapper import do_get
from translation_utils import *
from translator import Translator
from error_codes import *

allowedAuthors = set(["Wikipedia", "Matecat"])
quality = 80
subjects = set(["All", "Accounting","Aerospace","Agriculture_and_Farming",
               "Archeology","architecture","Art","Astronomy",
               "Automotive_Industry","Banking","Chemical",
               "Civil_Engineering","Computer_Science","Credit_Management",
               "Culinary","Finances","Forestry","General","History",
               "Insurance","Legal_and_Notarial","Literary_Translations",
               "Marketing","Matematics_and_Physics","Mechanical","Medical",
               "Music","Nautica","Pharmaceuticals","Religion","Science",
               "Social_Science","Tourism"])

class MyMemory(Translator):
    """
    MyMemory translator

    """
    content_type = "Content-type: application/json"

    def __init__(self, key=None, email=None, criteria=False, matchAll=False, allowedAuthors=allowedAuthors, subjects=subjects, quality=quality, verbose=False):
        """
        :param key: Secret key. The use of the key permits more translations per month, but the performance is worse
        :type key: string
        :param email: Email to verify the account
        :type email: string
        :param criteria: Filter translations by quality
        :type criteria: bool
        :param matchAll: Accept or not only allowed authors
        :type matchAll: bool
        :param allowedAuthors: Filter the translations by user
        :type allowedAuthors: set of string
        :param subjects: Glossaries where the translations must be found
        :type subjects: set of string
        :param quality: Minimum quality for the translations
        :type quality: int
        :param verbose: Show information
        :type verbose: bool

        """
        super(MyMemory, self).__init__(verbose)
        self.key = key
        self.email = email
        self.criteria = criteria
        self.match = (self._match_all if matchAll else self._match_at_least_one)
        self.allowedAuthors = allowedAuthors
        self.quality = quality
        self.subjects = subjects

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    # Not used
    def _show_user_translations(self, content):
        for user_translation in content[u'matches']:
            print 'Author:', user_translation[u'created-by'], \
                  'Quality:', user_translation[u'quality'], \
                  'Translation', user_translation[u'translation']

    def _get_quality(self, quality_string):
        return int(quality_string) if quality_string is not None else 0

    def _match_at_least_one(self, user_translation):
        return self._get_quality(user_translation[u'quality']) >= self.quality or user_translation[u'created-by'] in allowedAuthors or user_translation[u'subject'] in self.subjects

    def _match_all(self, user_translation):
        return self._get_quality(user_translation[u'quality']) >= self.quality and user_translation[u'created-by'] in allowedAuthors and user_translation[u'subject'] in self.subjects

    def _get_user_translations(self, content):
        words = []
        for user_translation in content[u'matches']:
          if not self.criteria or self.match(user_translation):
            word = user_translation[u'translation']
            if word is not None:
              words.append(user_translation[u'translation'])
        return words

    # Not used
    def _get_default_translation(self, content):
        return content[u'responseData'][u'translatedText']

    def get_translation(self, term, source_language, target_language):
        langpair = source_language+'|'+target_language
        params = {'q': term, 'langpair': langpair}
        if self.key is not None:
            params['key'] = self.key
        if self.email is not None:
            params['de'] = self.email

        e = io.BytesIO()
        response_code = do_get("http://api.mymemory.translated.net/get?",
               params,
               [self.content_type],
               e.write)

        if response_code is OK:
            content = json.loads(e.getvalue().decode('UTF-8'))
            words = set(self._get_user_translations(content))
            return list(words), response_code
        else:
            return [], response_code

    def get_name(self):
        return "MyMemory"

    def translate(self, translatorTask):
        return super(MyMemory, self).translate(translatorTask)

if __name__ == "__main__":
    from keys import mymemory_key, mymemory_email
    myMemory = MyMemory(email=mymemory_email)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = myMemory.translate(translatorTask)
    print translations.__unicode__()