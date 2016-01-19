pyTurEng v0.5.0119160225
==================

This script searches meaning of specified word or wordlist(New Feature, See CHANGELOG.md)<br/>
on www.tureng.com webpage and receives first 5 results if there are. If not, it receives first result or says "No Result".

Usage
==================

python pyTurEng.py tren tr merhaba<br/>
or<br/>
python pyTurEng.py tren tr "merhaba dünya"<br/>
or (For WordLists)<br/>
python pyTurEng.py tren en wordlist.txt outlist.txt<br/>

Dictionary options
==================
tren = for Turkish<->English Dictionary<br/>
deen = for German<->English Dictionary<br/>
esen = for Spanish<->English Dictionary<br/>
fren = for French<->English Dictionary

if your word will be searched is in english use "en" after dictionary option.<br/>
if your word is in other languages specify it with "tr","de","es" or "fr".<br/>

Examples :<br/>
python pyTurEng.py deen en hello<br/>
python pyTureng.py deen de viel<br/>

Requests
==================
Python3, requests and BeautifulSoup


