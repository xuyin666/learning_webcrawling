# xpath rules
# parents nodes, attribut filter

from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

# class为item-0的li节点的内容
html = etree.parse('./test.html', etree.HTMLParser())
# 记过为'\n    ' 是因为/只算子节点 子节点里面的文字只有换行符了
# result = html.xpath('//li[@class="item-0"]/text()')
# result = html.xpath('//li[@class="item-0"]/a/text()')
# 所有的文字node
result = html.xpath('//li[@class="item-0"]//text()')
print(result)
