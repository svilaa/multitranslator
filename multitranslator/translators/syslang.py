# -*- coding: utf-8 -*-

from query_wrapper import do_get, Buffer
from translation_utils import *
from translator import Translator
import xmltodict
import time
from error_codes import *

class Syslang(Translator):
    """
    Syslang/Frengly translator.
    The queries for this translator have a delay of 3 seconds.

    """
    supported_languages = {"zh": "zh-CN"}
    content_type = "Content-type: text/xml"
    out_format = "xml" # json, xml

    def __init__(self, email, password, verbose=False):
        """
        :param email: User email
        :type email: string
        :param password: User password
        :type password: string
        :param verbose: Show information
        :type verbose: bool

        """
        super(Syslang, self).__init__(verbose)
        self.email = email
        self.password = password

    def get_language(self, lang):
        return lang if lang not in self.supported_languages else self.supported_languages[lang]

    def get_translation(self, term, source_language, target_language):

        tgt_lang = self.get_language(target_language)
        params = {'src':source_language, 'dest':tgt_lang, 'text':term, 'email':self.email, 'password':self.password, 'outformat':self.out_format}
        b = Buffer()
        response_code = do_get("http://frengly.com?",
               params,
               [self.content_type],
               b.callback)
        time.sleep(3) # API must be called with a difference of 3 seconds or more
        if response_code is OK:
            c = xmltodict.parse(b.content)
            if "root" in c:
                return [c["root"]["translation"]], response_code
            else:
                return [], NO_CONTENT
        else:
            return[], TIMEOUT

    def get_languages(self):
        return set(["en", "es", "it", "fr", "ru", "de", "pt", "nl", "ar", "zh"])

    def get_name(self):
        return "SysLang"

if __name__ == "__main__":
    from keys import syslang_email, syslang_password
    syslang = Syslang(syslang_email, syslang_password)
    translatorTask = TranslatorTask("hello", target_languages=["es"])
    translations = syslang.translate(translatorTask)
    print translations.__unicode__()