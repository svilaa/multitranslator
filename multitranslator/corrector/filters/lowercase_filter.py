# -*- coding: utf-8 -*-

from abstract_filter import AbstractFilter

class LowercaseFilter(AbstractFilter):
    """
    If all the characters are capitalize, uncapitalize all.
    If the first character is capitalized, but not the rest, uncapitalize the first character

    """
    def __init__(self):
        super(LowercaseFilter, self).__init__()

    def _uncapitalize(self, term):
        return term[:1].lower() + term[1:]

    def apply(self, term):
        try:
            if term.isupper(): return term.lower()
            elif not term.islower() and term[0].isupper(): return self._uncapitalize(term)
            else: return term
        except IndexError:
            return term


if __name__ == "__main__":
    lcf = LowercaseFilter()
    print lcf.apply(u"hello")
    print lcf.apply(u"geH")
    print lcf.apply(u"HELLO")
    print lcf.apply(u"Hello World")
    print lcf.apply(u'Привет')