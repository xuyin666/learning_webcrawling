import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

file = open('movies.txt', 'w', encoding='utf-8')
for item in items:
    # movies name
    name = item.find('a > h2').text()
    file.write(f'名称：{name}\n')

    # categories
    categories = [item.text() for item in item.find('.categories button span').items()]
    file.write(f'类别：{categories}\n')
    
    # published_at
    published_at = item.find('.item:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    file.write(f'上映时间：{published_at}\n')

    # score
    score = item.find('p.score').text()
    file.write(f'评分：{score}\n')

    file.write(f'{"=" * 50}\n')

file.close()


with open('movies.text', 'w', encoding='utf-8') as file:
    file.write(f'名称：{name}\n')
    file.write(f'类别：{categories}\n')
    file.write(f'上映时间：{published_at}\n')
    file.write(f'评分：{score}\n')
