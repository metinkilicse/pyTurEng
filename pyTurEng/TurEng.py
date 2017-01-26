#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import sys

class TurEng(object):
	def __init__(self):
		self.url = "http://tureng.com/tr/turkce-ingilizce/"

	def get_meaning(self,word,lang_class):

		request = requests.get(self.url+str(word))
		content = request.content
		soup = BeautifulSoup(content, "html.parser")
		meaning_types = soup.findAll("td",{"class" : re.compile(r'\bhidden-xs\b')})
		meanings = soup.findAll("td", {"class" : lang_class})
		if len(meanings)>=5:
			return meaning_types[1:15:3],meanings[:5]
		else:
			if meanings != None and meaning_types != None:
				return meaning_types,meanings
			else:
				return None,None


	def change_url(self,dic):
		if dic == "tren":
			self.url = "http://tureng.com/tr/turkce-ingilizce/"
		elif dic == "deen":
			self.url = "http://tureng.com/en/german-english/"
		elif dic == "esen":
			self.url = "http://tureng.com/en/spanish-english/"
		elif dic == "fren":
			self.url = "http://tureng.com/en/french-english/"
			pass

	def tag_to_str(self,r_list):
		res = []
		try:
			for r in r_list:
				res.append(r.text)
			return res
		except:
			print("Error : {}".format(e))
			exit()

	def remove_duplicates(self,m_list):
		new_list = []
		for m in m_list:
			if m not in new_list:
				new_list.append(m)
		return new_list

	def search_from_file(self,input_file,output_file,lang_class):
		try:
			with open(input_file,"r", encoding="utf-8") as input_f:
				input_lines = input_f.readlines()
		except Exception as e:
			print("Error : {}".format(e))
			exit()
		try:
			out_f = open(output_file,"a", encoding="utf-8")
			for line in input_lines:
				r_list = self.get_meaning(line.split("\n")[0],lang_class)[1]
				if len(r_list) == 1:
					res = r_list.text
				elif len(r_list) > 1:
					res = ", ".join(self.remove_duplicates(self.tag_to_str(r_list)))
				elif r_list == None:
					res = " "
				else:
					res = " "
				out_f.write(line.split("\n")[0] + " = " + str(res) + "\n")
			out_f.close()
			print(str(len(input_lines)) + " word(s) were searched.")
		except Exception as e:
			print("Error : {}: line : {}".format(e,sys.exc_info()[2].tb_lineno))
			exit()
		return True
