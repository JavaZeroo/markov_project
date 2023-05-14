import requests
from bs4 import BeautifulSoup
import re

htmfile='data/areas2.htm'
with open(htmfile, 'r') as f:
    html = f.read()
# get html
soup = BeautifulSoup(html, 'lxml')
# find all ol 
ol = soup.find('ol').find_all('ol')

region2code = {}

for li in ol:
    # find all li
    for l in li.find_all('li'):
        # find all a
        for a in l.find_all('a'):
            # get href
            href = a.get('href')
            # get text
            text = a.get_text()
            # print
            # print(text, href)
            # download
            # r = requests.get(href, allow_redirects=True)
            # open('data/'+text, 'wb').write(r.content)
            
            # match href with regex to get the region code like E31000001, E31000006
            match = re.search(r'([A-Z0-9]{9})', href)
            # print(match.group(1))
            region2code[text] = match.group(1)
print(region2code)
