import requests
from bs4 import BeautifulSoup

url = ""
soup = BeautifulSoup(url,"lxml")

l = []

for p in soup.find_all('p'):
    string = p.text.replace("\"","\\\"")
    l.append(string)

total_content = "\n".join(l)