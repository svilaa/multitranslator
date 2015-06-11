languages = {"en": "English",
             "es": "Spanish",
             "it": "Italian",
             "fr": "French",
             "pt": "Portuguese",
             "de": "German",
             "nl": "Dutch",
             "ru": "Russian",
             "zh": "Chinese",
             "ar": "Arabic"}

def get_language_name(code):
    """
    Obtain the name of the language from its code

    :param code: The ISO 639-1 code that identifies a language
    :return: The name of the language
    :rtype: string

    """
    return languages[code]

class TranslatorTask:
    """
    A TranslatorTask stores which text will be translated from a source language to a list of target languages.

    """
    def __init__(self, term, source_language="en", target_languages=languages.keys()):
        """
        It's recommended the use of quotes for term if term has multiple words.

        :param term: Text to be translated
        :type term: string
        :param source_language: The original language of term
        :type source_language: string
        :param target_languages: The languages of the translations. The default value is all the available languages in the languages dictionary.
        :type target_languages: List of string

        """
        self.term = term
        self.source_language = source_language
        self.target_languages = target_languages

    def __unicode__(self):
        """
        Mandatory the use of this representation instead of __str__
        A TranslatorTask is composed by the term, the source language and the target languages

        :return: The text representation of TranslatorTask
        :rtype: unicode string
        """
        return "Term: " + self.term.decode('utf-8') + \
               " Source language: " + \
               self.source_language + \
               " Target languages: " + \
               ",".join(self.target_languages)

class TranslatorJob:
    """
    A TranslatorJob stores the name of the translator, who made a translation,
    the list of translations as a dictionary and the time spend on these.
    The keys of the translation dictionary are language codes  and the values,
    lists with the translations, for example:
    {
        "es": ["hola", "saludo"],
        "it": ["ciao"],
        "fr": ["bonjour", "salut"]
    }

    """
    def __init__(self, translator_name, translations, execution_time):
        """
        :param translator_name: The name of the translator
        :type translator_name: string
        :param translations: The list of translation classified by language
        :type translations: dictionary
        :param execution_time: Time spent by the translator to create this TranslatorJob
        :type: float

        """
        self.translator_name = translator_name
        self.translations = translations
        self.execution_time = execution_time

    def __unicode__(self):
        """
        Mandatory the use of this representation instead of __str__

        :return: The text representation of TranslatorJob
        :rtype: unicode string
        """
        return "Translator: " + self.translator_name + \
        " Translations: " + "}; ".join([get_language_name(k)+": "+ "{" + ", ".join(v) for k,v in self.translations.items()]) + "}"  + \
        " Execution time: " + self.execution_time.__str__()

class Translation:
    """
    A Translation is the combination of a TranslatorTask and a list of TranslatorJob,
    that is, the modeling of a translation process, containing what is wanted,
    and the results for each translator.

    """
    def __init__(self, translator_task, translations):
        self.translator_task = translator_task
        self.jobs = translations

    def get_total_time(self):
        """
        Obtain the sum of the execution times for each TranslatorJob

        :return: The sum of the execution times
        :rtype: float

        """
        return sum(job.execution_time for job in self.jobs)

    def __unicode__(self):
        """
        Mandatory the use of this representation instead of __str__

        :return: The represenation of a Translation, that is the combination of the
         TranslatorTask and the list of TranslatorJob, including the execution time
        :rtype: unicode string

        """
        return " Task: {" + self.translator_task.__unicode__() + "}" + \
        " Total time: " + self.get_total_time().__str__() + \
        " Jobs: " + "; ".join([job.__unicode__() for job in self.jobs])