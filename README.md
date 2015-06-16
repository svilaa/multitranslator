# MultiTranslator

This repository contains a set of tools to translate, correct and validate terms.

The main application is Transfusion, it provides the basic mechanism to obtain translations.

To use Transfusion in a better way was created Transfuse, a friendly command line application for users and automatized scripts.

Finally, there are two other scripts: grouper, to create readable and revisable documents with translations, and validator, to perform reports about the efficiency of the translators and the accuracy of the translations.

<h3>Cloning the repository</h3>
Execute the next command:

```git clone --recursive https://github.com/svilaa/multitranslator.git```

The recursive flag must be present or the submodules for dict.cc and bing don't be downloaded.

<h3>Installation</h3>
Inside multitranslator/translators there are two configuration files: keys.py and settings.py.
In keys.py can be added the API keys provided by each translator service.
In settings.py can be configured which translators are activated and their initialization (some translators have additional configurations).

This configuration is used by transfuse.py and transfusion if any translator is provided, that is, if multitranslator is used as a module, the keys and the translators can be configured independently in your own application, importing the desired translators and using these directly or with a Transfusion instance.

After the configuration, execute ```python setup.py install``` at the repository root.

Now you are able to import multitranslator as a module, and execute as scripts: transfuse.py, grouper.py and validator.py.

<h4>PyCurl</h4>
It's recommended the installation of some required libraries for pycurl with:

```sudo apt-get install libcurl4-gnutls-dev librtmp-dev```

<h4>ReportLab</h4>
Could be problems with this PDF library if during the installation the arial.ttf font is not found. Sadly, there isn't a generic solution that solves this issue.

<h4>Concurrency</h4>
With this basic configuration now you have access to all the functionalities except concurrent execution of the translation process. If you desire this optional feature, you must install [pathos](https://github.com/uqfoundation/pathos). The process to install this library could be difficult, so it's recommended to download the pathos repository and install it with python setup.py install, probably some libraries fail, in the external directory there are some .zip with libraries, they could be useful.

<h3>How to use</h3>

```import multitranslator```

The available scripts are:
* transfuse
* grouper
* validator

<h3>Documentation</h3>

[Sphinx](http://sphinx-doc.org/) must be installed to generate the documentation.
Go to the docs directory and execute:

```make html```

After the generation, the mainpage is located at docs/build/html/index.html

The help can be displayed with the argument ```-h```

<h3>Supported translators</h3>
*	[Google](https://translate.google.com/) (Thanks to [zhuoqiang](https://bitbucket.org/zhuoqiang))
*	[Bing](https://www.bing.com/translator/) (Thanks to [wronglink](https://github.com/wronglink))
*	[SDL](https://languagecloud.sdl.com/)
*	[OneHourTranslation](https://www.onehourtranslation.com/)
*	[Yandex](http://mymemory.translated.net/)
*	[Yandex dictionary](https://tech.yandex.com/dictionary/)
*	[MyMemory](http://mymemory.translated.net/)
*	[Syslang/Frengly](http://www.frengly.com/)
*	[WorldLingo](http://www.worldlingo.com/)
*	[Dict.cc](http://www.dict.cc/) (Thanks to [rbaron](https://github.com/rbaron))
*	[Hablaa](http://hablaa.com/)
*	[Glosbe](https://glosbe.com/)
*	[Baidu](http://translate.baidu.com/)
*	[iTranslate4](http://itranslate4.eu/)

<h3>License</h3>

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/es/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/3.0/es/88x31.png" /></a><br />Esta obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/es/">licencia de Creative Commons Reconocimiento-NoComercial-SinObraDerivada 3.0 España</a>.
