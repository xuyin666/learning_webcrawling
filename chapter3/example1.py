# xpath rules
# all nodes or child nodes

from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 所有的节点
# result = html.xpath('//*')
# print(result)

# 所有的li节点
# result = html.xpath('//li')
# print(result)
# print(result[0])

# li节点的所有直接子节点a
# result = html.xpath('//li/a')
# print(result)

# 所有ul节点下的所有子孙节点a
# result = html.xpath('//ul//a')
# print(result)

# 所有ul节点下的所有子节点a
result = html.xpath('//ul/a')
print(result)