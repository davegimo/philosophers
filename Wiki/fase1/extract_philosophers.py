import urllib.request
import urllib.parse
import re

url =  'https://en.wikipedia.org/wiki/List_of_philosophers_(A%E2%80%93C)'
values = {'s':'basics', 'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)

respData = resp.read()

paragraphs = re.findall(r'<li><a href="/wiki/(.*?)" title', str(respData))

for par in paragraphs:
    if '" class' in par:
        par = par.split('" class')[0]
    print(par)
