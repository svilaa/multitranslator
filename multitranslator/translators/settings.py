from google import Google
from bing import Bing
from mymemory import MyMemory
from sdl import SDL
from worldlingo import WorldLingo
from yandex import Yandex
from yandex_dictionary import YandexDict
from onehourtranslation import OneHourTranslation
from syslang import Syslang
from hablaa import Hablaa
from itranslate4 import ITranslate
from glosbe import Glosbe
from dict_cc_wrapper import Dict_CC
from baidu import Baidu

from keys import *

"""
The list of translators, their keys and initializations must be added here

"""

default_translators = {
               "google": Google(),
               #"mymemory": MyMemory(mymemory_key),
               #"bing": Bing(bing_client_id, bing_client_secret),
               #"sdl": SDL(sdl_auth),
               "worldlingo": WorldLingo(worldlingo_key),
               #"yandex": Yandex(yandex_private_key),
               #"yandex_dict": YandexDict(yandex_dict_private_key),
               #"onehour": OneHourTranslation(onehour_account, onehour_public_key, onehour_secret_key),
               #"syslang": Syslang(syslang_email, syslang_password),
               "hablaa": Hablaa(),
               #"itranslate": ITranslate(itranslate_key),
               "glosbe": Glosbe(),
               "dictcc": Dict_CC(exactly_term=False),
               #"baidu": Baidu(baidu_api_key),
              }