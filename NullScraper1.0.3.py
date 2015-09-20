# +++++++++++++++WebScraper -python+++++++++++++++
# Basic Web Scraper Made In Python
# I AM NEW TO PYTHON, SO KEEP THAT IN-MIND
# constructive crticism is encouraged
# Feel free to use this code, but give credit to NULLBOT plz
#EDIT-1.03= Now with color

import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

print '\033[1;34m-------------------------\033[1;m'
print '\033[1;36mWELCOME TO NULLSCRAPER: MADE BY NULLBOT\033[1;m'
print '\033[1;36mBTW... Search engines cannot be crawled\033[1;m'
url = raw_input("Type a url to be scraped/crawled: ")
br = mechanize.Browser()
urls = [url]
visited = [url]
while len(urls) > 0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url, link.url)
            b1 = urlparse.urlparse(newurl).hostname
            b2 = urlparse.urlparse(newurl).path
            newurl = "http://"+b1+b2
            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                print newurl
                print len(urls)
    except:
        print '\033[1;34m-------------------------\033[1;m'
        found = ("URLS FOUND: " + str(len(visited)))
        print found
        urls.pop(0)

if len(visited) == 1:
    print '\033[1;31mAn Error Occurred: Url could be invalid or encrypted with an asymmetric algorithm\033[1;m'
else:
    print '\033[1;32mSUCCESS: ALL URLS HAVE BEEN FOUND \033[1;m'
