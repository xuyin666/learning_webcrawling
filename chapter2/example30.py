# session example

import requests

# requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = requests.get('https://www.httpbin.org/cookies')
# print(r.text)

s = requests.Session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)