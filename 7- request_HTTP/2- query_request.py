import requests


url_get = 'http://httpbin.org/get'

payload = {"name":"Enes","ID":"123"}


r = requests.get(url_get,params=payload)

print(r.url) # http://httpbin.org/get?name=Enes&ID=123
print(r.request.body) # None
print(r.status_code) # 200 : OK
print(r.text)
'''
result of r.text:
{
  "args": {
    "ID": "123", 
    "name": "Enes"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.31.0", 
    "X-Amzn-Trace-Id": "Root=1-660eb9f5-0208b8c5612b1e33295dbb4b"
  }, 
  "origin": "XXX.XXX.XXX.XXX", 
  "url": "http://httpbin.org/get?name=Enes&ID=123"
}
'''

print(r.headers['Content-Type']) # application/json