Transfuse
=========

Transfuse is a command-line application that uses Transfusion and the writers to provide 
a better user interface to made and store translations. All the parameters are optional, 
that is, the user must ensure the introduced arguments will do what he want.

Arguments
---------

| -t | --term: Text to be translated, it's recommended the use of quotes to avoid problems with spaces. By default is "hello", only used for testing.
|
| -sl | --source-language: Language code provided by Transfusion. By default it is English.
|
| -tl | --target-languages: List of language codes provided by Transfusion. If this argument is not present, it's assumed all the language will be used except the source language.
|
| -tr | --translators: List of names of the translators. The names are obtained using the default translators dictionary keys from settings.py. If this argument is not present, it's assumed all the default translators will be used.
|
| -so | --standard: Outputs the tasks in a table and the translators for each language in another.
|
| -soi | --standard-individual: Outputs the tasks in a table and each language has a table, it's more readable in some cases.
|
| -j | --json: Outputs the JSON representation of the translation.
|
| -x | --xml: Outputs the XML representation of the translation.
|
| -p | --pdf: Outputs the PDF representation of the translation, it must require a parameter, that is the filename where the data will be stored.
|
| -ro | --raw-output: Outputs the default Unicode representation of the translation.
|
| -s | --show: Offers specific help about a topic, the options are:
|   •   translators: Shows the available translator names for -tr.
|   •   languages: Shows the available language codes and its name for -sl and -tl.
|   •   table-formats: Shows the available table formats provided by tabulate.
|   •   all: Shows all the previous information.
|
| -v | --verbose: Active the verbose flag for Transfusion.
|
| -c | --correct: Active the correction flag for Transfusion.
|
| -h | --help: Shows the help provided by argparse.
|
|
| Special arguments compatible with -so | --standard:
|
| -ti | --time: Add a new column with the total time execution and the time for each translator.
|
| -td | --time-decimals: Changes the number of decimals for a best fit.
|
| Special arguments compatible with -so | --standard and -soi | --standard-infividual:
|
| -tf | --table-format: Changes the table format used by tabulate. By default is "fancy_grid".
|
|
| Arguments for concurrency:
|
| -co | --concurrent: Active the concurrent execution of the translators.
|
| -nt | --num-threads: Sets the number of threads used for the concurrent execution.

Examples
--------

Show help::

    transfuse.py --help

Show available options::

    transfuse.py --show all

Show available translators::

    transfuse.py --show translators

Translate "hello" from English to Spanish and Italian 
using all the translators, standard output and verbose::

    transfuse.py --term "hello" -tl es it -so -v

Translate "dog" from English to Russian using Google, 
Yandex and Bing, standard output individual with tsv 
table format and with the corrector::

    transfuse.py --term "dog" -tl ru -tr google yandex bing -soi -tf tsv -c


Translate "cat" from English (explicit) to German using 
Google, OneHourTranslation, SDL and Hablaa, standard output, 
json output in the file "json_test", xml output with default 
filename in the folder "new_directory", raw output in a 
default filename, with concurrency and 4 threads::

    transfuse.py --term "cat" -sl en -tl de -tr google onehour sdl hablaa -so --json json_test --xml new_directory/ -ro default -co -nt 4
