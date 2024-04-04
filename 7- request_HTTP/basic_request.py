import requests

url = 'https://www.ibm.com/'

r = requests.get(url)

print(r) # our response 
print(r.status_code) # our response code : 200