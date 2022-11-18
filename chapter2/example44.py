import httpx

# with httpx.Client() as client:
#     response = client.get('https://www.httpbin.org/get')
#     print(response)

# client = httpx.Client()
# try:
#     response = client.get('https://www.httpbin.org/get')
#     print(response)
# finally:
#     client.close()

# url = 'https://www.httpbin.org/get'
# headers = {
#     'User-Agent' : 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
# }
# with httpx.Client(headers=headers) as client:
#     r = client.get(url)
#     print(r.json()['headers']['User-Agent'])

client = httpx.Client(http2=True)
response = client.get('https://www.httpbin.org/get')
print(response.text)
print(response.http_version)