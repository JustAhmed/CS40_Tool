import re
import os
import requests
from bs4 import Comment
from bs4 import BeautifulSoup
from menuPrinter import HPrinter

def main5():
    domain = input("Domain (domainName.com)  --> ")
    resp = requests.get("http://www." + domain)
    src = resp.content
    soup = BeautifulSoup(src , "lxml")
    links = soup.find_all('a')
    complete = [a.get('href') for a in soup.find_all('a', href=True)]
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    tags = [tag.name for tag in soup.find_all()]
    unq_tags = list(set(tags))
    print(type(complete))
    print(complete)
    for link in links: 
        if domain in link.attrs['href']:
            s = link.attrs['href'][:link.attrs['href'].index(domain)]
            obj=re.compile(r'http[s]?://(\w.+).')
            url = obj.findall(s)
            url = list(url)
            
    t1List = ["\n\nParsing Complete!", "1. Display Output", "2. Save it to file (/root/Desktop/scrapedData.txt)"]
    opt = HPrinter(t1List, 2)

    if opt == 1:
        print('\n\n#-------------URLs found on Your Website-------------------')
        for lnk in range(len(complete)):
            print(f"{lnk}. {complete[lnk]}")

        print('\n\n#-------------Tags found on Your Website-------------------')
        for tag in range(len(unq_tags)):
            print(f"{tag}. <{unq_tags[tag]}>")

        print('\n\n#-------------SubDomains found on Your Website-------------------')
        for i in range(len(url)):
            print(f"{i}. {url[i]}")

        print('\n\n#-------------Comments-------------------#')
        for comnt in range(len(comments)):
            print(f"{comnt}. {comments[comnt]}")
    else:
        f = open("/root/Desktop/scrapedData.txt", "w")
        f.write('\n\n#-------------URLs found on Your Website-------------------')
        for lnk in range(len(complete)):
            f.write(f"{lnk}. {complete[lnk]}\n")

        f.write('\n\n#-------------Tags found on Your Website-------------------')
        for tag in range(len(unq_tags)):
            f.write(f"{tag}. <{unq_tags[tag]}>\n")

        f.write('\n\n#-------------SubDomains found on Your Website-------------------')
        for i in range(len(url)):
            f.write(f"{i}. {url[i]}\n")

        f.write('\n\n#-------------Comments-------------------#')
        for comnt in range(len(comments)):
            f.write(f"{comnt}. {comments[comnt]}\n")