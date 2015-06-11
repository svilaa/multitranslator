# -*- coding: utf-8 -*-

import HTMLParser
from query_wrapper import do_get, JSONBuffer
from translation_utils import *
from translator import Translator
from error_codes import *

class OneHourTranslation(Translator):
    """
    OneHourTranslation translator

    """
    content_type = "Content-type: application/json"

    supported_languages = {"zh": "zh-cn-cmn-s"}

    parser = HTMLParser.HTMLParser()

    def __init__(self, account, public_key, secret_key, verbose=False):
      """
      :param account: User account
      :type account: string
      :param public_key: Public key
      :type public_key: string
      :param secret_key: Secret key
      :type secret_key: string
      :param verbose: Show information
      :type verbose: bool

      """
      super(OneHourTranslation, self).__init__(verbose)
      self.account = account
      self.public_key = public_key
      self.secret_key = secret_key

    def _get_language(self, lang):
        return lang if lang not in self.supported_languages else self.supported_languages[lang]

    def _parse(self, term):
        return self.parser.unescape(term)

    def get_translation(self, term, source_language, target_language):
        params = {'account': self.account,
                  'secret_key': self.secret_key,
                  'public_key': self.public_key,
                  'source_language': source_language,
                  'target_language': self._get_language(target_language),
                  'source_content': term}

        b = JSONBuffer()
        response_code = do_get("http://www.onehourtranslation.com/api/2/mt/translate/text?",
               params,
               [self.content_type],
               b.callback)
        if response_code is OK:
          translation_code = b.content[u'status'][u'code']
          if translation_code is 0 and b.content[u'status'][u'msg'] == u'ok':
            return [self._parse(b.content[u'results'][u'TranslatedText'])], response_code
          else:
            return [], translation_code
        else:
          return [], response_code


    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "OneHourTranslation"

if __name__ == "__main__":
    from keys import onehour_account, onehour_secret_key, onehour_public_key
    oneHour = OneHourTranslation(onehour_account, onehour_public_key, onehour_secret_key)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = oneHour.translate(translatorTask)
    print translations.__unicode__()