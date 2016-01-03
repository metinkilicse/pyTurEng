pyTurEng v0.1.3.162030
==================

	This script searches meaning of specified word or wordlist(not supported yet)
on www.tureng.com webpage and receives first 5 results if there are. If not, it receives first result or says "No Result".

Usage
==================

python pyTurEng.py tren tr merhaba
or
python pyTurEng.py tren tr "merhaba dünya"
or
python pyTurEng.py tren en wordlist.txt ( not supported yet )

Dictionary options
==================
tren = for Turkish<->English Dictionary
deen = for German<->English Dictionary
esen = for Spanish<->English Dictionary
fren = for French<->English Dictionary

if your word will be searched is in english use "en" after dictionary option.
if your word is in other languages specify it with "tr","de","es" or "fr".

Examples :
python pyTurEng.py deen en hello
python pyTureng.py deen de viel

Requests
==================
Python3, requests and BeautifulSoup


