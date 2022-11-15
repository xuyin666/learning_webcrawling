# timeout setting

import requests

# the total timeout
# r = requests.get('https://www.httpbin.org/get', timeout=1)

# timeout for connecting, timeout for reading 
# r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))

# Without timeout
# r = requests.get('https://www.httpbin.org/get', timeout=None)
r = requests.get('https://www.httpbin.org/get')

print(r.status_code)
