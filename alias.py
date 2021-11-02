from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


def getaliases(url):
    try:
        #page = urlopen(url)
        page = requests.get(url)
        #print("opened")
        soup = BeautifulSoup(page.text, 'html.parser')

        content = soup.find('section', {"class": "aliases"})
        aliases=[i.text for i in content.findAll('li')]
        aliases=list(map(lambda x: re.sub('\xa0',' ',x),aliases))
        aliases=list(map(lambda x: re.sub('[^a-zA-Z]',' ',x),aliases))
        aliases=list(map(lambda x: re.sub('^ *','',x),aliases))
        return aliases
    except:
        print("Error opening the URL")
        return []


    

