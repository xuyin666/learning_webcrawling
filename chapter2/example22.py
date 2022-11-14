# request get method

import requests

# r = requests.get('https://www.httpbin.org/get')
# print(r.text)

# data = {
#     'name': 'germey',
#     'age': '25'
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)

r = requests.get('https://www.httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))

