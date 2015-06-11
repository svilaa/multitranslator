# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 
from write_utils import *

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

width, height = letter
margin = 0.5*inch
mwidth = width - 2*margin
mheight = height - margin
vertical_space = -0.3*inch
first_row = margin
second_row = mwidth*2/5
current_height = 0
languages_per_row = 5

def _set_configuration(c):
    global current_height
    c.translate(0,mheight-vertical_space)
    c.setFont("Arial",14)
    current_height = vertical_space

def _draw(c, text, row, jump_factor):
    global current_height
    if(-current_height > mheight):
        c.showPage()
        _set_configuration(c)
    c.drawString(row, current_height, text.encode('utf-8'))
    current_height += jump_factor*vertical_space

def _draw_line(c, size):
    global current_height
    c.setLineWidth(size)
    c.line(0.5*inch , current_height, width - 0.5*inch, current_height)
    _draw(c, "", first_row, 1)

def _add_task(c, task):
    _draw(c, u"Term", first_row, 0)
    _draw(c, task.term, second_row, 1)
    _draw(c, u"Source Language", first_row, 0)
    _draw(c, get_language_name(task.source_language), second_row, 1)
    _draw(c, u"Target Languages", first_row, 0)
    languages = [get_language_name(code) for code in task.target_languages]
    wrote_languages = 0
    while(wrote_languages < len(languages)):
        _draw(c, ", ".join([get_language_name(code)
            for code in task.target_languages[wrote_languages:wrote_languages+languages_per_row]]), second_row, 1)
        wrote_languages+=languages_per_row
    _draw_line(c, 2)

def _add_translations(c, translations):
    for lang in translations.translator_task.target_languages:
        _draw(c, u"Translator", first_row, 0)
        _draw(c, get_language_name(lang), second_row, 1)
        for job in translations.jobs:
            _draw(c, job.translator_name, first_row, 0)
            for translation in job.translations[lang]:
                _draw(c, translation, second_row, 1)
        _draw_line(c, 1)

def _fill_canvas(c, translations):
    _set_configuration(c)
    _add_task(c, translations.translator_task)
    _add_translations(c, translations)

def pdf_output(translations, filename, default_filename):
    """
    Stores the translations inside the chosen filename using the PDF format

    :param translations: The data that will be stored
    :type translations: Translation
    :param filename: The filename where the PDF data will be stored
    :type filename: string
    :param default_filename: The default filename if a valid descriptor file can't be obtained
    :type default_filename: string

    """
    f = get_write_file_descriptor(filename, "pdf", default_filename)
    c = canvas.Canvas(f, pagesize=letter)
    _fill_canvas(c, translations)
    c.showPage()
    c.save()