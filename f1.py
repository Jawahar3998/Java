from bs4 import BeautifulSoup
import urllib3

html = urllib3.PoolManager()
visitedlinks = set()
needtocrawllinks = []

seedurl = html.request('GET', 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/')

def gethtmlobj(stringurl):
    htmlobj = html.request('GET', stringurl)
    if(htmlobj.status != 200):
      return htmlobj.data

def getsoupobj(htmlobj):
    soupobj = BeautifulSoup(htmlobj, 'html.parser')
    return soupobj

def bfsonsoupobj(soupobj):
    for link in soupobj.find_all('a'):
        print(link.get('href'))
        urlstring = link.get('href')
        if(urlstring not in visitedlinks):
           needtocrawllinks.append(urlstring)

def crawling(seed):
    htmlobj = gethtmlobj(seed)
    soupobj = getsoupobj(htmlobj)
    bfsonsoupobj(soupobj)
    while(needtocrawllinks.isEmpty() is not True):
        urlstring = needtocrawllinks.popleft()
        if(urlstring in visitedlinks):
           continue
        htmlobj = gethtmlobj(urlstring)
        soupobj = getsoupobj(htmlobj)
        bfsonsoupobj(soupobj)

