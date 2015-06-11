# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='multitranslator',
    version='1.0',
    license='',
    description='Translation tool that groups a set of translator APIs to obtain better translations. \
                 Additional tools are provided to correct, group and validate translations.',
    author='Sergi Vila Almenara',
    author_email='svilaalmenara@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests==2.5.3',
        'tabulate==0.7.4',
        'pycurl==7.19.5.1',
        'httplib2==0.9',
        'simplejson==3.6.5',
        'goslate==1.4.0',
        'xmltodict==0.9.2',
        'beautifulsoup4==4.3.2',
        'futures==2.2.0',
        'six==1.3.0',
        'dill==0.2.2',
        'reportlab==3.1.44'
    ],
    scripts=["multitranslator/transfuse.py",
             "multitranslator/validator.py",
             "multitranslator/grouper.py"]
)
