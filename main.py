import selenium
from bs4 import BeautifulSoup
import requests
import pandas as pd
# raw = requests.get("https://www.google.com")
# print(raw.content)
# soup = BeautifulSoup(raw.content, "lxml")
# links = soup.findAll("a")
# for index, link in enumerate(links):
#     print("link {index}: {link}".format(link=link, index=index+1))
# names = data['name'].tolist()
# print(type(names[0]))
#name, display_name
data = pd.read_csv('data.csv')
names = []
for name in data['name'].tolist():
    names.append([name.replace(' ', '+')])

for index, name in enumerate(data['display_name'].tolist()):
    names[index].append(name.replace(' ', '+'))

test = names[0][0]
search_query = f"https://www.google.com/search?q={test}"
raw = requests.get(search_query)
soup = BeautifulSoup(raw.content, "lxml")
links = soup.findAll("a")
for index, link in enumerate(links):
    print(f"link {index}: {link}")
# for name, display_name in names:
#     search_query = f"https://www.google.com/search?q={name}"
#     raw = requests.get(search_query)
#     soup = BeautifulSoup(raw.content, "lxml")
#     links = soup.findAll("a")
