#!/usr/bin/env python

from __future__ import absolute_import


from TurEng import TurEng
import sys
import os


args = sys.argv

if len(args) != 4:
    print("Use as :\n'python pyTurEng.py tren tr merhaba\nor\n"
          "python pyTurEng.py tren en \"go away\"\nor\n"
          "python pyTurEng.py tren en wordlist.txt")
else:
    dic = args[1]
    lang = args[2]
    query = args[3]
    if os.path.exists(query):
        pass
    else:
        dic_obj = TurEng()
        dic_obj.change_url(dic)
        if lang == "en":
            result = dic_obj.get_meaning(query,"tr ts")
        else:
            result = dic_obj.get_meaning(query,"en tm")
        types, meaning = result[0],result[1]
        if len(meaning)==5:
            for i in range(5):
                print("{} : {}".format(types[i].text,meaning[i].text))
        else:
            if len(meaning)==0:
                print("No Result")
            else:
                print("{} : {}".format(types[1].text,meaning[0].text))