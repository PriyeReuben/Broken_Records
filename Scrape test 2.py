from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


#page = requests.get('https://www.almanac.com/weather/history/zipcode/33125/1945-03-02')
url = 'https://www.almanac.com/weather/history/zipcode/33125/1945-03-02'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

#content = webpage.read()
#print(content)

soup = BeautifulSoup(webpage, 'lxml')
print(soup.prettify())

fields = soup.find_all('h3')
values = soup.find_all('span', class_='value')
zip_code = soup.find(attrs={"name": "location"})
date = soup.find(attrs={"name": "date"})

print("Zipcode: " + str(zip_code))
print(date)
print(fields)
print(values[0])
x = str(values[0])
x = x[20:-7]
print(x)
