import urllib.request

url = 'https://www.example.com'
proxyServer = 'https://www.proxy.com:3128/'

# 프록시 서버를 통해 웹 서버로 요청을 보낸다
proxy_handler = urllib.request.ProxyHandler({'http': proxyServer})

# 프록시 서버 설정을 무시하고 웹 서버로 요청을 보낸다
# proxy_hander = urllib.request.ProxyHandler({})

# 프록시 서버에 대한 인증을 처리한다
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

# 2개의 핸들러를 오프너에 등록한다
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# opener.open() 대신 urlopen 사용
f = urllib.request.urlopen(url)

print('geturl():', f.geturl())
print(f.read(500).decode('utf-8'))
