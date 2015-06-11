# -*- coding: utf-8 -*-

from abstract_filter import AbstractFilter

class StripFilter(AbstractFilter):
    """
    Remove all the spaces, tabulations and other separator characters on the left and on the right

    """
    def __init__(self, chars=None):
        super(StripFilter, self).__init__()
        self.chars = chars

    def apply(self, term):
        if self.chars is None:
            return term.strip()
        else:
            return term.strip(self.chars)


if __name__ == "__main__":
    lcf = StripFilter(chars=".")
    print lcf.apply(u"hello")
    print lcf.apply(u"geH")
    print lcf.apply(u"HELLO")
    print lcf.apply(u"Hello World")
    print lcf.apply(u'Привет')