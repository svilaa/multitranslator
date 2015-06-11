from write_utils import *
import json

def json_output(translations, filename, default_filename):
    """
    Stores the translations inside the chosen filename using the JSON format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the JSON data will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string

    """
    json_structure = {}
    task = {"term": translations.translator_task.term,
            "source_language": translations.translator_task.source_language,
            "target_languages": translations.translator_task.target_languages,
            "total_time": translations.get_total_time().__str__()}
    json_structure["task"] = task
    jobs = []
    for translator_job in translations.jobs:
        job = {}
        job["name"] = translator_job.translator_name
        job["execution_time"] = translator_job.execution_time.__str__()
        languages = []
        for job_language in translator_job.translations:
            language = {}
            language["code"] = job_language
            language["translations"] = translator_job.translations[job_language]
            languages.append(language)
        job["languages"] = languages
        jobs.append(job)
    json_structure["jobs"] = jobs
    f = get_write_file_descriptor(filename, "json", default_filename)
    out_json = json.dumps(json_structure, ensure_ascii=False, indent=4) # ensure_ascci to print UTF-8 correctly
    write_utf8_encoded(f, out_json)
    close_file_descriptor(f)