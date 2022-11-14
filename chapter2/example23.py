# example web crawling

import requests
import re

r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
title = re.findall(pattern, r.text)
print(title)