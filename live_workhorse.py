#The CLAPP (Climate App)
from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt
import numpy as np
from urllib.request import Request, urlopen

date_list = []
avg_temp_list = []


#Establish the necessary values for the URL
zip_code = input("Enter a 5-digit zip code:")
month = input("Enter a 2-digit month:")
day = input("Enter a 2-digit day:")

#No leap years
if month == "02" and day == "29":
    day = "28"

#Get data points from almanac website
for year in range(1945, 2022):

    #set the URL string
    url = 'https://www.almanac.com/weather/history/zipcode/{}/{}-{}-{}'.format(zip_code, year,month, day)

    #open the URL page
    #page = requests.get(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #sneak past the server as a firefox browser
    page = urlopen(req).read()


    soup = BeautifulSoup(page, 'lxml')

    # get all temperature values
    values = soup.find_all('span', class_='value')
    print(values)

    #get average temperature for given day and trim excess html
    avg_temp = str(values[1])
    avg_temp = avg_temp[20:-7]


    #append the current date and avg temp to their respective lists
    date_list.append(year)
    avg_temp_list.append(float(avg_temp))


    # live plotting #this is not optimized and redraws the entire graph for each new data point but it looks cooler
    plt.title('Average Temps in zip code {} for the date {}-{}-YYYY from 1945-2021'.format(zip_code, month, day))
    plt.ylabel('Average Temperature')
    plt.xlabel('Years')
    plt.scatter(date_list, avg_temp_list)
    #plt.scatter(avg_temp_list, date_list)
    plt.pause(0.01)



#line of best fit
x = np.array(date_list)
y1 = np.array(avg_temp_list)

#plt.scatter(x, y1)

a, b = np.polyfit(x, y1, 1)
plt.plot(x, a * x + b)

plt.show()
