# request

import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:100])
# print(r.cookies)

r = requests.get('https://www.httpbin.org/get')
r = requests.get('https://www.httpbin.org/post')
r = requests.get('https://www.httpbin.org/put')
r = requests.get('https://www.httpbin.org/delete')
r = requests.get('https://www.httpbin.org/patch')
