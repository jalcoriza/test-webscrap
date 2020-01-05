from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/")
#res = BeautifulSoup(html.read(),"html5lib")
res = BeautifulSoup(html.read(), "html.parser")


# import ipdb; ipdb.set_trace() # BREAKPOINT

print(res.title)

