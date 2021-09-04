from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import urllib.request
import urllib.parse

#read data
data = pd.read_csv('data.csv')

#create company name array and add names to it
names = []
for name in data['display_name'].tolist():
    names.append(name)

#initialize final output data array
final = []

url = "https://www.google.com/search"
values = {
    'q': names[0]
}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
response = response.read()
print(response)
error = "https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping"