# urlunparse needs 6 arguments

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'commnet']
print(urlunparse(data))