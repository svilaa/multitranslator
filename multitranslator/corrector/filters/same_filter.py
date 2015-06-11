# -*- coding: utf-8 -*-

from abstract_filter import AbstractFilter

class SameFilter(AbstractFilter):
    """
    Additional filter to detect equal terms. It is directly integrated in Corrector
    """

    def __init__(self):
        super(SameFilter, self).__init__()

    def apply(self, term, original=u''):
        if term == original: return u''
        return term


if __name__ == "__main__":
    lcf = SameFilter()
    print lcf.apply(u"hello", u'hello')
    print lcf.apply(u"geH")
    print lcf.apply(u"HELLO")
    print lcf.apply(u"Hello World")
    print lcf.apply(u'Привет', u'Привет')