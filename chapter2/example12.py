# urlparse

from urllib.parse import urlparse

# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result))
# print(result)

# scheme://netloc/path;params?query#fragment

# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)

# result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
# print(result)

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1])