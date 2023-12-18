import requests

url ='https://www.ibm.com/'
r=requests.get(url)
print(r.status_code)
print(r.request.headers)

header = r.headers
print (header ['date'])
print (header ['Content-Type'])
#modify 
url_get ='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)

print(r.url)