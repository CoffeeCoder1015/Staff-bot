import random
import re

import requests
from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor

header = {
    'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'none',
    'Accept-Language':'en-US;q=0.8',
    'Connection':'keep-alive'
}

def scrape(url):
    data = requests.get(url).content
    text_ele = BeautifulSoup(data,features='html.parser').text
    ope = text_ele.replace(" ","").split("\n")
    for i in ope:
        if i == "" or "." in i:
            ope.remove(i)
    return ope

def get_noun():
    tpx =ThreadPoolExecutor(24)
    l1 = tpx.submit(scrape,"https://raw.githubusercontent.com/martinsvoboda/nouns/master/nouns/en_nouns.txt")
    l2 = tpx.submit(scrape,"https://raw.githubusercontent.com/broeneatsdinner/list-noun/master/Lists/Fish/fish.txt")
    tpx.shutdown(wait= True)
    NOUNS = []
    for i in l1.result():
        NOUNS.append(i)
    for i in l2.result():
        NOUNS.append(i)

    NOUNS.insert(0,"")
    noun = random.choice(NOUNS)
    return noun

noun = get_noun()

def fetcher():
    global noun
    URL = "https://www.google.com/search?hl=en&tbm=isch&source=hp&q=%s meme"%(noun)
    page = requests.get(URL,headers=header).text
    f_jpg = ["https://%s.jpg"%(i) for i in re.findall("https://(.+).jpg",page)]
    
    for i in f_jpg[:]:
        
        if "<" in i or ">" in i or "data:image" in i:
            print(i)
            f_jpg.remove(i)

    link = random.choice(f_jpg)
    return link
