from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("url")
data = html.read()
html = data.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

title = soup.find("title")
body = soup.find("body")

print("title: " + title.text)
print("body: " + body.text)
