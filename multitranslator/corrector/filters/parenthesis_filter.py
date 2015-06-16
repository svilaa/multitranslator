# -*- coding: utf-8 -*-

import re
from abstract_filter import AbstractFilter

default_symbols = u'[\[\（\(].*?[\]\）\)]'

class ParenthesisFilter(AbstractFilter):
    """__init__(self, symbols=<default symbols>)
    Remove all the text between parenthesis and brackets

    """
    def __init__(self, symbols=default_symbols):
        super(ParenthesisFilter, self).__init__()
        self.symbols = symbols

    def apply(self, term):
        return re.sub(self.symbols, '', term).strip()


if __name__ == "__main__":
    lcf = ParenthesisFilter()
    print lcf.apply(u"hello")
    print lcf.apply(u"geH")
    print lcf.apply(u"HELLO")
    print lcf.apply(u"[Hello] World")
    print lcf.apply(u'Привет (test)')