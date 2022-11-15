# ssl certificate

import requests
from requests.packages import urllib3
import logging
# response = requests.get('https://ssr2.scrape.center/')
# print(response.status_code)

# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)

# urllib3.disable_warnings()
# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)

# response = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', '/path/server.key'))
# print(response.status_code)

