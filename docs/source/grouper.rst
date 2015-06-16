Grouper
=======

The main task of grouper is to parse lot of translations 
to display these based on the requirements and chosen options 
by the user, offering three types of output and two criteria.

Arguments
---------

| -s | --sort: Criterion used to sort the translations. Options: source, score
|
| -i | --input: The JSON file or path (with JSON files) where are found the translations
|
| -c | --conf-file: The settings about the sources and their scores
|
| -v | --verbose: Show information about the current state of the execution using the error output
|
| -nt | --num-translations: Number of maximum translations displayed for output and output-languages
|
| -o | --output: Must be a file. Write all the translations for each term and language in the TSV file
|
| -ol | --output-languages: Must be a path. Write a set of files with the translations inside the path, each file contains one language
|
| -r | --results: Write a detailed report about the number of sources and the score of each term for every language

Examples
--------

Creates a information file called results using the translation 
files inside translations_directory with the configuration file 
grouper_configuration.json::

    grouper.py -i translations_directory -c grouper_configuration.json -r results

Creates a translation report called translations using the 
translation files inside translations_directory with the 
configuration file grouper_configuration.json, with verbose 
and the translations are sorted by score::

    grouper.py -i translations_directory -c grouper_configuration.json -o translations -v -s score

Creates a folder called languages_folder with the double 
translation columns using the translation files inside 
translations_directory with the configuration file 
grouper_configuration.json, with verbose and the translations 
are sorted by source, with 2 as a maximum number of translations 
per term::

    grouper.py -i translations_directory -c grouper_configuration.json -ol languages_folder -s source -nt 2
