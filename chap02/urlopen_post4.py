from urllib.request import Request, HTTPCookieProcessor, build_opener

url = 'http://127.0.0.1:8000/cookie/'

# first request (GET) with cookie Handler

cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)

req = Request(url)
resp = opener.open(req)

print('first response')
print(resp.headers)
print(resp.read().decode('utf-8'))

# second request (POST) with Cookie header
print('----------------')
data = 'language=python&framework=django'
encData = bytes(data, encoding='utf-8')

req = Request(url, encData)
resp = opener.open(req)

print('second response')
print(resp.headers)
print(resp.read().decode('utf-8'))
