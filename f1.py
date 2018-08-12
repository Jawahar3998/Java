from bs4 import BeautifulSoup
import requests, re, urllib


visitedlinks = set()
needtocrawllinks = []

#arg stringurl in string and returns a html document in string format
def gethtmlobj(stringurl):
 try:
      htmlobj = requests.get(stringurl)
      if (htmlobj.status_code == requests.codes.ok):
          return htmlobj.text

 except requests.RequestException:
        print('dont do anything')


#arg htmlobj in html data and return soup object
def getsoupobj(htmldata):
    soupobj = BeautifulSoup(htmldata, 'html.parser')
    return soupobj

def bfsonsoupobj(soupobj):
    for link in soupobj.find_all('a'):
        print(link.get('href'))
        urlstring = link.get('href')
        if(urlstring not in visitedlinks):
           needtocrawllinks.append(urlstring)

def crawling(seed):
    htmlobj = gethtmlobj(seed)
    if(htmlobj is not None):
      soupobj = getsoupobj(htmlobj)
      bfsonsoupobj(soupobj)
    while(not needtocrawllinks is False):
        urlstring = needtocrawllinks.pop(0)
        if(urlstring in visitedlinks):
           continue
        htmlobj = gethtmlobj(urlstring)
        if (htmlobj is not None):
         soupobj = getsoupobj(htmlobj)
         bfsonsoupobj(soupobj)
         visitedlinks.add(urlstring)

seedurl = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
crawling(seedurl)


