import requests
from bs4 import BeautifulSoup

URL='https://www.bbc.com/news'
response=requests.get(URL)
print("The response code is: ", response)

#parse the html document
soup=BeautifulSoup(response.content, 'html.parser')
print(soup)
#Extract news headlines from html
headlines=soup.find_all('h3')
for headline in headlines:
    print(headline.text,"\n")
 