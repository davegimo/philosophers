import urllib.request
import urllib.parse
import re


url = 'https://en.wikipedia.org/wiki/'
values = {'s' : 'basics',
          'submit' : 'search'
          }

#contents = urllib.request.urlopen(url).read()

#contents.


data = urllib.parse.urlencode(values)
data = data.encode('utf-8')


#print(respData)

f = open("link_filosofi_da_scremare.txt","r")

for line in f:
    link = url + line
    req = urllib.request.Request(link, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    paragraphs = re.findall(r'<table(.*?)</table>', str(respData))

    for eachP in paragraphs:
        if "Influences" or "Influenced" in eachP:
            #print(eachP)
            #print()
            r = re.findall(r'Influences(.*?)Influenced', str(eachP))
            #print("lunghezza influenti " + str(len(r)))
            for e in r:
                #print("LISTA INFLUENTI")
                influenze = re.findall(r'title="(.*?)"', str(e))
                #for i in influenze:
                    #print(i)
            
            p = re.findall(r'Influenced(.*?)colspan="2"', str(eachP))
            #print("lunghezza influenzati " + str(len(p)))
            for el in p:
                #print("---------------")
                #print("LISTA INFLUENZATI")
                influenzati = re.findall(r'title="(.*?)"', str(el))
                #for inf in influenzati:
                    #print(inf)

            if len(r) != 0 or len(p) != 0:
                print(link, end = '')
