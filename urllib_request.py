from urllib import request

response = request.urlopen('url')
content = response.read()
response.close()
html = content.decode()

title = html.split('<title>')[1].split('</title')[0]
print(title)