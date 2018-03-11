import requests
from bs4 import BeautifulSoup


def get_content(url):
    url = requests.get(url)
    soup = BeautifulSoup(url.content, "lxml")
    l = []
    for p in soup.find_all('p'):
        string = p.text.replace("\"", "\\\"").replace("\'", "\\'")
        l.append(string)
    return " ".join(l)

