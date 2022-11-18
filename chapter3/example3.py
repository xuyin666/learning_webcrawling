# xpath rules
# getting attribut

from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有li节点下所有的a节点的href属性
result = html.xpath('//li/a/@href')
print(result)