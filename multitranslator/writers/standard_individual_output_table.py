from write_utils import *
from tabulate import tabulate, tabulate_formats

def show_standard_output_individual(translation, filename, default_filename, table_format='fancy_grid'):
    """
    Stores the translations inside the chosen filename using a table for the task
    and one table for each language with a specified Tabulate table format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the tables will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string
    :param table_format: The table format used by Tabulate
    :type table_format: string

    """
    f = get_write_file_descriptor(filename, get_format(table_format), default_filename)
    task_headers, task_info = get_formatted_task_table(translation.translator_task)
    task = tabulate(task_info, headers=task_headers, tablefmt=table_format)
    write_utf8_encoded(f, task)
    write_utf8_encoded(f, '')
    for lang in translation.translator_task.target_languages:
        headers, translations = get_formatted_translation_table(translation, [lang])
        table = tabulate(translations, headers=headers, tablefmt=table_format) # Alignment: stralign="center"
        write_utf8_encoded(f, table)
        write_utf8_encoded(f, '')
    close_file_descriptor(f)