import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.yahoo.com/")
result.status_code
print (result)
result.headers
c = result.content
soup = BeautifulSoup(c)
print (soup)


