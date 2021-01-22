from urllib.request import urlopen
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup
import requests 


def monitoringFrontend(link):
    r = ping(link)
    if r == False or r == None:
        return False
    else:
        html = urlopen("http://"+link)
        res = BeautifulSoup(html.read(),"html5lib")
        if res.title != "":
            return True
        else:
            return False