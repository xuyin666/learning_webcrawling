# urlsplit don't handler params

from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result)

print(result.scheme, result[0])