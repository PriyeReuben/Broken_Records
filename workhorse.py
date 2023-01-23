from datetime import date
from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt
import numpy as np
from urllib.request import Request, urlopen


date_list = []
min_temp_list = []
avg_temp_list = []
max_temp_list = []

#start_date = date(1945, 1, 1)
#start_date_int = start_date.toordinal()

#end_date = date(1945, 1, 5)
#end_date_int = end_date.toordinal()

#today = date.today()
#today_date_int = today.toordinal()

zip_code = input("Enter a 5-digit zip code:")
month = input("Enter a 2-digit month:")
day = input("Enter a 2-digit day:")
#selected_month = input("Enter a month: 1-12")

#url_date = 1945

for year in range(1945, 2021):
    #url_date = date.fromordinal(day)

    url = 'https://www.almanac.com/weather/history/zipcode/' + str(zip_code) + '/' + str(year) + "-" + str(month) + "-" + str(day)

    #page = requests.get(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html.parser')
    print("first print")

    #fields = soup.find_all('h3')
    values = soup.find_all('span', class_='value')
    print("second print")
    #zip_code = soup.find(attrs={"name": "location"})
    #change this variable name#date = soup.find(attrs={"name": "date"})

    min_temp = str(values[0])
    min_temp = min_temp[20:-7]

    avg_temp = str(values[1])
    avg_temp = avg_temp[20:-7]

    max_temp = str(values[2])
    max_temp = max_temp[20:-7]

    #print(url_date, min_temp, avg_temp, max_temp)
    #date_list.append(int(url_date))
    date_list.append(year)
    avg_temp_list.append(float(avg_temp))
    min_temp_list.append(float(min_temp))
    max_temp_list.append(float(max_temp))

    #url_date +=1



print(date_list)
print(min_temp_list)
print(avg_temp_list)
print(max_temp_list)

x = np.array(date_list)
y1 = np.array(avg_temp_list)

plt.scatter(x, y1)

a,b = np.polyfit(x, y1, 1)
plt.plot(x, a*x+b)


plt.show()





