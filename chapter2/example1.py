import urllib.parse
import urllib.request

# data = bytes(urllib.parse.urlencode({'name': 'gremey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))

response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# read() 直接的返回值是bytes
# 需要用decode('utf-8')来翻译成utf-8
print(response.read())
