import requests
r = requests.get("url")
print(r.text)
print(r.status_code)
url = "WWW.something.com"
data = {
     "p1" : 4,
     "p2" : 8
 }

 r2 = requests.post(url = url, data = data)