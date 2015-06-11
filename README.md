# MultiTranslator

This repository contains a set of tools to translate, correct and validate terms.

The main application is Transfusion, it provides the basic mechanism to obtain translations.

To use Transfusion in a better way was created Transfuse, a friendly command line application for users and automatized scripts.
It has a lot of options to configure source language, target language, translators, outputs and flags.

<h3>Installation</h3>
Inside multitranslator/translators there are two configuration files: keys.py and settings.py.
In keys.py can be added the API keys provided by each translator service.
In settings.py can be configured which translators are activated and their initialization (some translators have additional configurations).

This configuration is used by transfuse.py and transfusion if any translator is provided, that is, if multitranslator is used as a module, the keys and the translators can be configured independently in your own application, importing the desired translators and using these directly or with a Transfusion instance.

After the configuration, execute python setup.py install at the repository root.

Now you are able to import multitranslator as a module, and execute as scripts: transfuse.py, grouper.py and validator.py.

With this basic configuration now you have access to all the functionalities except concurrent execution of the translation process. If you desire this optional feature, you must install [pathos](https://github.com/uqfoundation/pathos). The process to install this library could be difficult, so it's recommended to download the pathos repository and install it with python setup.py install, probably some libraries fail, in the external directory there are some .zip with libraries, they could be useful.

<h3>Supported translators:</h3>
*	[Google](https://translate.google.com/)
*	[Bing](https://www.bing.com/translator/)
*	[SDL](https://languagecloud.sdl.com/)
*	[OneHourTranslation](https://www.onehourtranslation.com/)
*	[Yandex](http://mymemory.translated.net/)
*	[Yandex dictionary](https://tech.yandex.com/dictionary/)
*	[MyMemory](http://mymemory.translated.net/)
*	[Syslang/Frengly](http://www.frengly.com/)
*	[WorldLingo](http://www.worldlingo.com/)
*	[Dict.cc](http://www.dict.cc/)
*	[Hablaa](http://hablaa.com/)
*	[Glosbe](https://glosbe.com/)
*	[Baidu](http://translate.baidu.com/)
*	[iTranslate4](http://itranslate4.eu/)
