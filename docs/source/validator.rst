Validator
=========

Validator was created to generate automatic reports about 
the accuracy of the translators and the success rate of the 
terms. Additionally, with these information can be created 
more realistic scores for grouper.

Arguments
---------

| -i | --input: Directory with the JSON files that contain the translations
|
| -tr | --report-by-translator: Do an analysis focused on the accuracy of the translators
|
| -te | --report-by-term: Do an analysis focused on the success rate of the terms
|
| -vf | --validation-file: The JSON file with the required information for the analysis
|
| -v | --verbose: Show information about the current state of the execution
|
| -d | --detailed: Show more information about the statistics
|
| -s | --separator: Add extra lines for a better readability
|
| -p | --percentage: The percentages are showed in a most readable style

Examples
--------

Creates a report about the accuracy of the translators, 
with detailed information about which terms are accepted, 
with readable percentages::

    validator.py -i translations_directory -tr translators_validation -d -p

Creates a report about the success rate of the terms, 
with verbose, with additional spaces::

    validator.py -i translations_directory -te terms_validation -v -s 
