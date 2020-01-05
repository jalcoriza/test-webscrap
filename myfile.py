from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

#website = "https://www.python.org"
website = "https://www.kkpis.org"

try:
    html = urlopen(website)
    
except HTTPError as e:
    print(e)
    
except URLError:
    print("Server down or incorrect domain")
    
else:
    #res = BeautifulSoup(html.read(),"html5lib")
    res = BeautifulSoup(html.read(), "html.parser")
    # import ipdb; ipdb.set_trace() # BREAKPOINT
    print(res.title)

