#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

url = "https://google.com"

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
#    res = BeautifulSoup(html.read(),"html5lib")
    res = BeautifulSoup(html.read(),"html.parser")
    if res.title is None:
        print("Tag  not found")
    else:
        print(res.title)

