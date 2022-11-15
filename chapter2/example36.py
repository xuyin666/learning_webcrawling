from requests import Request, Session

url = 'https://www.httpbin.org/post'
data = {'name' : 'germey'}
headers = {
    'User-Agent' : 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)