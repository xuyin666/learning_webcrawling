# 获取属性,获取文本

html = '''
<div class="wrap">
    <div id="container"> 
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)

# a = doc('a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)
# for item in a.items():
#     print(item.attr('href'))

# a = doc('.item-0.active a')
# print(a)
# print(a.text())

li = doc('.item-0.active')
print(li)
print(li.html())
