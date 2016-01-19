#!/usr/bin/env python

from __future__ import absolute_import


from TurEng import TurEng
import sys
import os


args = sys.argv

if len(args)==4:
	dic = args[1]
	lang = args[2]
	query = args[3]
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
elif len(args)==5:
	dic = args[1]
	lang = args[2]
	input_file = args[3]
	output_file = args[4]
	try:
		dic_obj = TurEng()
		dic_obj.change_url(dic)
		if os.path.exists(input_file):
			if lang == "en":
				dic_obj.search_from_file(input_file,output_file,"tr ts")
			else:
				dic_obj.search_from_file(input_file,output_file,"en tm")
	except Exception as e:
		print("Error : {}".format(e))
		exit()
else:
	print("Use as :\n'python pyTurEng.py tren tr merhaba\nor\n"
		  "python pyTurEng.py tren en \"go away\"\nor\n"
		  "python pyTurEng.py tren en wordlist.txt")