# -*- coding: utf-8 -*-
from sys import maxint
from abstract_filter import AbstractFilter

class LengthFilter(AbstractFilter):
    """__init__(self, max_length=maxint)
    If the term is longer than max_length, the term is removed

    """
    def __init__(self, max_length=maxint):
        super(LengthFilter, self).__init__()
        self.max_length = max_length

    def apply(self, term):
        if len(term) > self.max_length:
           return u''
        return term

if __name__ == "__main__":
    lcf = LengthFilter(max_length=4)
    print lcf.apply(u"hello")