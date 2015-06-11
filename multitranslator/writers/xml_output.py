from write_utils import *
from xml.etree import ElementTree as ET

def _indent(elem, level=0):
  """
  copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
  it basically walks your tree and adds spaces and newlines so the tree is
  printed in a nice way
  """
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      _indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

def xml_output(translations, filename, default_filename):
    """
    Stores the translations inside the chosen filename using the XML format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the XML data will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string

    """
    root = ET.Element("root")
    task = ET.SubElement(root, "task")
    ET.SubElement(task, "term").text = translations.translator_task.term
    ET.SubElement(task, "source_language").text = translations.translator_task.source_language
    target_languages = ET.SubElement(task, "target_languages")
    for target_language in translations.translator_task.target_languages:
        ET.SubElement(target_languages, "target_language").text = target_language
    ET.SubElement(task, "total_time").text = translations.get_total_time().__str__()
    jobs = ET.SubElement(root, "jobs")
    for translator_job in translations.jobs:
        job = ET.SubElement(jobs, "job")
        translator = ET.SubElement(job, "translator")
        ET.SubElement(translator, "name").text = translator_job.translator_name
        ET.SubElement(translator, "execution_time").text = translator_job.execution_time.__str__()
        languages = ET.SubElement(job, "languages")
        for job_language in translator_job.translations:
            language = ET.SubElement(languages, "language")
            ET.SubElement(language, "code").text = job_language
            language_translations = ET.SubElement(language, "translations")
            for job_translation in translator_job.translations[job_language]:
                ET.SubElement(language_translations, "translation").text = job_translation
    _indent(root)
    f = get_write_file_descriptor(filename, "xml", default_filename)
    ET.ElementTree(root).write(f, encoding="UTF-8", xml_declaration=True, method="xml")
    close_file_descriptor(f)