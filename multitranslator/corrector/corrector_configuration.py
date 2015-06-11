from collections import OrderedDict
from filters.abstract_filter import AbstractFilter
from filters.lowercase_filter import LowercaseFilter
from filters.parenthesis_filter import ParenthesisFilter
from filters.punctuation_symbols_filter import PunctuationSymbolsFilter
from filters.strip_filter import StripFilter

"""
The default corrector can be configured here.
The default_filters dictionary stores in order the sets of filters that will be applied with apply_all.

"""

# Take care with the order of the filters
initial_filters = [ParenthesisFilter(),
                   PunctuationSymbolsFilter(),
                   StripFilter(),
                   LowercaseFilter(),
                  ]
last_filters = []
default_filters = OrderedDict([
                    ("initial", initial_filters),
                    ("last", last_filters),
                  ])

corrector_available_languages = set(['en', 'es' ,'it', 'fr', 'pt', 'de', 'nl', 'zh', 'ru', 'ar'])