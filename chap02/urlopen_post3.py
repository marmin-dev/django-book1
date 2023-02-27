from urllib.request import HTTPBasicAuthHandler, build_opener

auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm='ksh', user='shkim', passwd='shkmad',
                          uri='https://127.0.0.1:8000/auth/')
opener = build_opener(auth_handler)
resp = opener.open('https://127.0.0.1/auth/')
print(resp.read().decode('utf-8'))
