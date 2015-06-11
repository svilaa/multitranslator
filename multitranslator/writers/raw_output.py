from write_utils import get_write_file_descriptor, write_utf8_encoded, close_file_descriptor

def show_raw_output(translations, filename, default_filename):
    """
    Stores the translations inside the chosen filename using the raw format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the raw data will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string

    """
    f = get_write_file_descriptor(filename, "out", default_filename)
    write_utf8_encoded(f, translations.__unicode__())
    close_file_descriptor(f)