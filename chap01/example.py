import urllib.request
print(urllib.request.urlopen("https://www.example.com").read().decode('utf-8'))
