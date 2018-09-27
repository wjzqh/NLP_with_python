# -*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import nltk

url = "http://www.sohu.com"
html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
raw = soup.get_text()
tokens = nltk.word_tokenize(raw)
tokens = tokens[:100]
text = nltk.Text(tokens)
text.concordance('function')