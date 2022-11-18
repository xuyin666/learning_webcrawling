# re.sub

import re

# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view='5">
<a href="/6.mp3" singer="邓丽君">但思人长久</a>
</li>
</ul>
</div>
'''

# # \s*? 非贪婪模式的匹配空白字符
# # (<a.*?>)? 匹配最少的<a.*?>
# # \w+ 匹配一个单词
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])
#     # print(result[0], result[1], result[2])

# <a.*?>|</a> 意味匹配<a.*?> 或者 </a>都可以
html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())