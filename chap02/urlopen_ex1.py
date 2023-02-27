from urllib.request import urlopen

f = urlopen("https://www.example.com")
print(f.read(500).decode('utf-8'))
