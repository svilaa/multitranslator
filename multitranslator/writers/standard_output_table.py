from write_utils import *
from tabulate import tabulate, tabulate_formats

def show_standard_output(translation, filename, default_filename, add_time=False, time_decimals=16, table_format='fancy_grid'):
    """
    Stores the translations inside the chosen filename using a table for the task
    and another table for the translations with a specified Tabulate table format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the tables will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string
    :param add_time: Add a new column with the time spent for each translator
    :type add_time: bool
    :param time_decimals: Number of decimals for the times
    :type time_decimals: int
    :param table_format: The table format used by Tabulate
    :type table_format: string

    """
    if time_decimals <=0:
        time_decimals = 16
    task_headers, task_info = get_formatted_task_table(translation.translator_task)
    headers, translations = get_formatted_translation_table(translation, translation.translator_task.target_languages, add_time, time_decimals)
    f = get_write_file_descriptor(filename, get_format(table_format), default_filename)
    task = tabulate(task_info, headers=task_headers, tablefmt=table_format)
    table = tabulate(translations, headers=headers, tablefmt=table_format) # Alignment: stralign="center"
    write_utf8_encoded(f, task)
    write_utf8_encoded(f, '')
    write_utf8_encoded(f, table)
    close_file_descriptor(f)