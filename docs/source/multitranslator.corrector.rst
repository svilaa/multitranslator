Corrector
=========

The file corrector_configuration.py contains the used filters and the available languages. The  default_filters ordered dictionary is the structure sent to the corrector to apply the filters, the value for every string key must be a list of AbstractFilter instances. This special organization of the data has sense if are checked the apply_filters and apply_all functions in the Corrector class.

The OrderedDict must be provided in the constructor, by default it is default filters from corrector_configuration.py.

apply_filters iterate the list of filters identified by the key filters_type from self.filters and returns the chained output after the filtering. This function can be executed individually if only a set of filters is required.

apply_all sends the term to all the filters in self.filters in the specific provided order. Initially it is checked if the source term and the translation are the same (SameFilter behavior), after that are executed all the groups of filters and after each is checked again if the terms are equal, this allows an early return response if this event occurs, for example, it could be a first group of fastest filters, another more slowly, and finally a very heavy filters that take a lot of time, if the equality of terms can be detected before the execution of the second and the third group, the performance will be better.

The expected execution of the corrector is the creation of an instance of Corrector with the selected filters and languages and execute the apply_all function, that is all the filters must accomplish the AbstractFilter super class, because these will be executed in the same way. If some extra filters with other needs are required, these can be called individually by the programmer.

Filters
-------

.. toctree::

    multitranslator.corrector.filters

Corrector
---------

.. automodule:: multitranslator.corrector.corrector
    :members:
    :undoc-members:
    :show-inheritance:

Corrector configuration
-----------------------

.. automodule:: multitranslator.corrector.corrector_configuration
    :members:
    :undoc-members:
    :show-inheritance: