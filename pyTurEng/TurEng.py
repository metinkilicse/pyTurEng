import requests
from bs4 import BeautifulSoup
import re


class TurEng(object):
    def __init__(self):
        self.url = "http://tureng.com/tr/turkce-ingilizce/"

    def get_meaning_own(self,word):

        request = requests.get(self.url+str(word))
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        meaning_types = soup.findAll("td",{"class" : re.compile(r'\bhidden-xs\b')})
        tr_meanings = soup.findAll("td", {"class" : "tr ts"})
        if len(tr_meanings)>=5:
            return meaning_types[1:15:3],tr_meanings[:5]
        else:
            if tr_meanings != None and meaning_types != None:
                return meaning_types[1],tr_meanings[0]

    def get_meaning_en(self,word):

        request = requests.get(self.url+str(word))
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        meaning_types = soup.findAll("td",{"class" : re.compile(r'\bhidden-xs\b')})
        tr_meanings = soup.findAll("td", {"class" : "en tm"})
        if len(tr_meanings)>=5:
            return meaning_types[1:15:3],tr_meanings[:5]
        else:
            if tr_meanings != None and meaning_types != None:
                return meaning_types,tr_meanings

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