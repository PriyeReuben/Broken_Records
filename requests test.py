import requests

r = requests.get('https://www.almanac.com/weather/history/zipcode/33125/1945-03-02')
print(type(r.text))