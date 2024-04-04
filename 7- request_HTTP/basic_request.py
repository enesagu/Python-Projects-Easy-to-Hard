import requests

url = 'https://www.ibm.com/'

r = requests.get(url)

print(r) # our response 
print(r.status_code) # our response code : 200 : OK

print(r.headers) # we can get header 

print(r.request.body) # None


# we can see some detail in this request

header = r.headers

print(header['date']) # Thu, 04 Apr 2024 13:43:27 GMT

print(header['Content-Type']) # text/html;charset=utf-8

print(r.encoding) # utf-8



print(r.text[0:])
'''
result of r.text[0:100]:

<!DOCTYPE HTML>
<html lang="en-us">
<head>
    
    
    
    
    <meta charset="UTF-8"/>
  
''' # we can show more option with r.text[0:] or just r.texts 