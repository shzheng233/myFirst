#encoding:utf-8

import os
import requests
from bs4 import BeautifulSoup

def getContent(url3):
    text_Code = requests.get(url3)
    text_Cotext = text_Code.text
    text_Soup = BeautifulSoup(text_Cotext)
    text_Title = text_Soup.title
    text_Final = text_Soup.find(id='readerFs').text
    text_Ga = text_Final.replace('document.getElementById("readerFs").className = "rfs_" + rSetDef()[3]','')
    fw = open(file='D:\sheisg\shizheng.txt',mode='a',encoding='utf-8')
    fw.write(text_Title.text)
    fw.write(text_Ga)
    fw.write('\n')
    fw.close()

url = 'http://book.zongheng.com/showchapter/770577.html'

res = requests.get(url)
content = res.text

soup = BeautifulSoup(content)
manager = soup.findAll('td')
for i in manager:
    url2 = i.find('a')['href']
    getContent(url3=url2)
    print(url2)