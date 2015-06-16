# -*- coding: utf-8 -*-

import re
from abstract_filter import AbstractFilter

default_symbols = u"[.,;:\-\_\^¨\+\-\*\/=\?¿¡!|@#~¬\\\n\t%&\"<>€£$]"

default_regular_exp = re.compile(default_symbols,re.UNICODE)

class PunctuationSymbolsFilter(AbstractFilter):
    """__init__(self, regular_exp=<default regular expression>)
    Remove punctuation symbols

    """
    def __init__(self, regular_exp=default_regular_exp):
        super(PunctuationSymbolsFilter, self).__init__()
        self.regular_exp = regular_exp

    def apply(self, term):
        return re.sub(self.regular_exp, '', term)


if __name__ == "__main__":
    lcf = PunctuationSymbolsFilter()
    print lcf.apply(u"hello.")
    print lcf.apply(u"geH")
    print lcf.apply(u"HELLO")
    print lcf.apply(u"Hello World")
    print lcf.apply(u'Привет')