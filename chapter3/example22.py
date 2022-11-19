# 查找父节点, 兄弟节点，遍历节点

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
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

# parents = items.parents()
# print(type(parents))
# print(parents)

# parent = items.parents('.wrap')
# print(parent)

# 选择class为list的节点内部的class为item-0和active的节点
li = doc('.list .item-0.active')
# print(li.siblings())
print(li.siblings('.active'))

