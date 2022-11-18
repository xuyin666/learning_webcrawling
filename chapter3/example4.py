# xpath rules
# 属性多值匹配 和 多属性匹配

from lxml import etree
# text = '''
# <li class="li li-first"><a href="link1.html">first item</a></li>
# '''
# html = etree.HTML(text)
# NOT OK
# result = html.xpath('//li[@class="li"]/a/text()')

# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)