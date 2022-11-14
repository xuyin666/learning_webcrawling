# request get method with headers
import requests

headers = {
    'User-Agent' : 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
}
r = requests.get('https://ssr1.scrape.center/', headers=headers)
print(r.text)