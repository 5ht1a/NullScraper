# +++++++++++++++WebScraper -py edition+++++++++++++++
# Basic Web Scraper Made In Python
# Feel free to use this code, but give credit to NULLBOT plz

import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = raw_input("Type a url to be scraped/crawled ")
br = mechanize.Browser()
urls = [url]
visited = [url]
while len(urls)>0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url,link.url)
            b1 = urlparse.urlparse(newurl).hostname
            b2 = urlparse.urlparse(newurl).path
            newurl =  "http://"+b1+b2
            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                print newurl
                print len(urls)
    except:
        print ("error")
        print("URLS FOUND: " + str(len(visited)))
        urls.pop(0)
