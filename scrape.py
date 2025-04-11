from bs4 import BeautifulSoup
import requests

with open("index.html") as html_file:
    soup=BeautifulSoup(html_file,'lxml')
    # print(soup)
    paragraphs=soup.find_all('div',class_='article')
    for para in paragraphs:
     print(para.p.text)