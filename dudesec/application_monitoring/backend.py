from urllib.request import urlopen
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup
import requests 


def monitoringBackend(link):
    r = ping(link)
    if r == False or r == None:
        return False
    else:
        resp = requests.get("http://"+link)
        if resp.status_code == 200:
            return True
        else:
            return False