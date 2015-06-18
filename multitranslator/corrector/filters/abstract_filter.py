from abc import ABCMeta, abstractmethod

class AbstractFilter(object):
    """
    Abstract class that declares the apply method that every filter must implement

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def apply(self, term):
        """
        Correct the term using the current filter

        :param term: The text to be corrected
        :type term: string

        """
        pass