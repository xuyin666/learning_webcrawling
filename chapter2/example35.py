# about proxy

import requests

# the below example are not tested, they will not work

# proxies = {
#     'http': 'http://10.10.10.10:1080',
#     'https': 'https://10.10.10.10:1080',
# }

# requests.get('https://www.httpbin.org/get', proxies=proxies)

# proxies = {
#     'https': 'https://user:password@10.10.10.10:1080',
# }
# requests.get('https://www.httpbin.org/get', proxies=proxies)


# proxy for socks protocol
proxies = {
    'http' : 'socks5://user:password@host:port',
    'https' : 'socks5://user:password@host:port',
} 
requests.get('https://www.httpbin.org/get', proxies=proxies)
