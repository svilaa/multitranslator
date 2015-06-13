import os
import sys
import time

from multitranslator.translators.translation_utils import languages, get_language_name

formats = set(['tsv', 'html', 'psql', 'rst', 'latex'])

def get_write_file_descriptor(path, extension, default_path):
    """
    Return a file description depending of the type of path

    :param path: A file or a directory
    :type path: string
    :param extension: The file extension
    :type extension: string
    :param default_path:
    :return: if path is stdout, return sys.stdout,
             if path is default, return the file descriptor of default_path file
             if path is a directory, return the description file of the path+default_path file,
                and if the directory doesn't exists, it will be created
             if path is a file, return the descriptor file of this file
             if path is None, return None
    :rtype: file descriptor

    """
    if path is None:
        return None

    if path == "stdout":
        return sys.stdout
    elif path == "default":
        new_path = _get_path_with_extension(default_path, extension)
        return open(new_path, 'w')
    elif path[-1] is os.sep:
        _create_path_if_not_exists(path)
        new_path = os.path.join(path, _get_path_with_extension(default_path, extension))
        return open(new_path, 'w')
    else:
        new_path = _get_path_with_extension(path, extension)
        return open(new_path, 'w')

def write_utf8_encoded(file_descriptor, content):
    """
    Write content with UTF-8 encoding in file_descriptor

    :param file_descriptor:
    :type file_descriptor:
    :param content: Text to be wrote
    :type content: string

    """
    print >>file_descriptor, content.encode('utf-8')

def _get_path_with_extension(path, extension):
    return path + '.' + extension

def _create_path_if_not_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

def get_time():
    """
    Obtain a string that formats the current date

    :return: A formatted date string
    :rtype: string

    """
    return time.strftime("%d-%m-%y_%H-%M")

def _get_float_text_rounded(num, decimals):
    return ("{0:."+str(decimals)+"f}").format(num)

def _get_formatted_word_list(lis, delim):
    formatted_list = ""
    if not lis:
        return formatted_list
    for elem in lis[:-1]:
        formatted_list += elem + delim
    formatted_list += lis[-1]
    return formatted_list

def _language_codes_to_languages(language_codes):
    return [get_language_name(code) for code in language_codes]

def get_formatted_task_table(task):
    """
    Obtain the headers and a formatted table for task

    :param task: The
    :type task: TranslatorTask
    :return: A tuple with the necessary data to create a table with Tabulate
    :rtype: tuple (List of string, List of string)

    """
    headers = ["Term", "Source language", "Target languages"]
    tabulated = [[task.term, _language_codes_to_languages([task.source_language])[0],
                 ', '.join(_language_codes_to_languages(task.target_languages))]]
    return headers, tabulated

def get_formatted_translation_table(translation, languages, add_time=False, time_decimals=16):
    """
    Obtain the headers and the formatted table for translations

    :param translation: The translations to generate the table
    :type translation: Translation
    :param languages: The languages used for the table
    :type languages: List of string
    :param add_time: Add a new column with the
    :type add_time: bool
    :param time_decimals: Number of decimals for time column
    :type time_decimals: int
    :return: A tuple with the necessary data to create a table with Tabulate
    :rtype: tuple (List of string, List of string)

    """
    headers = ["Translator"] + _language_codes_to_languages(languages)
    if(add_time):
        headers.append("Time " + _get_float_text_rounded(translation.get_total_time(), time_decimals))
    tabulated = []
    for job in translation.jobs:
        row = []
        row.append(job.translator_name)
        for lang, translation_list in job.translations.iteritems():
            if lang in languages:
                row.append(_get_formatted_word_list(translation_list, ", "))
        tabulated.append(row)
        if(add_time):
            row.append(_get_float_text_rounded(job.execution_time, time_decimals))
    return headers, tabulated

def close_file_descriptor(descriptor):
    """
    Close descriptor if it is not sys.stdout

    :param descriptor: The file descriptor to be closed
    :type descriptor: file descriptor

    """
    if descriptor is not sys.stdout:
        descriptor.close()

def get_format(table_format):
    """
    Try to obtain a format from Tabulate formats

    :param table_format: The wanted file extension
    :type table_format: string
    :return: The required file extension if it exists, otherwise it is "txt"
    :rtype: string

    """
    if table_format in formats:
        return table_format
    return "txt"