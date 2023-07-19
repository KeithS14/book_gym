from urllib import request

url = "https://example.com"
response = request.urlopen(url)
html = response.read().decode("utf-8")
print(html)
