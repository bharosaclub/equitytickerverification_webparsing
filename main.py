import selenium
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
data = pd.read_csv('data.csv')
names = []
for name in data['display_name'].tolist():
    names.append(name)
names_with_ticker = []
# print(names[:20])
# print (names)
# test_list = [names[0]]
test_list = ['Nestle SA', 'Wal-Mart Stores Inc']
# for name in ['Quantum Information Services']:
#     search_query = f"https://www.google.com/search?q={name.replace(' ','+')}+yahoo+finance"
#     raw = requests.get(search_query)
#     soup = BeautifulSoup(raw.text, "lxml")
#     links = soup.findAll("a")
#     match = False
#     for link in links:
#         # print(link.attrs['href'])
#         match = re.search(r'\w?\w?.?finance.yahoo.com/(\w*?)?/?(\w*)', link.attrs['href'], flags = 0)
#         if match == None:
#             ticker = False
#         else:
#             ticker = match.group(2)
#             # print(f"{name} had {match.group(2)} as ticker symbol")
#             break
#     if not ticker:
#         print(f"{name} had no match")
#         ticker = "none"
#         names_with_ticker.append([name, ticker])
#     else:
#         print(f"{name} had {ticker.upper()} as ticker symbol")
#         names_with_ticker.append([name, ticker.upper()])

for name in ['Toronto-Dominion Bank']:
    search_query = f"https://www.google.com/search?q={name.replace(' ','+').replace('(', '').replace(')', '')}+yahoo+finance"
    # print(search_query)
    raw = requests.get(search_query)
    soup = BeautifulSoup(raw.text, "lxml")
    headers = soup.findAll("h3")
    match = False
    for header in headers:
        text = header.string
        print(text)
        # print('__')
        remove_irrelevant_brackets = lambda text: re.sub('\([A-Za-z][a-z]*\)', '', text)
        text = remove_irrelevant_brackets(text)
        print(text)
        match = re.search(r'\((\S*?)\)', text)
        if match == None:
            ticker = False
        else:
            ticker = match.group(1)
            print('match found')
            break
    if not ticker:
        print(f"{name} had no match")
    else:
        print(f"{name} had {ticker.upper()} as ticker symbol")
        names_with_ticker.append([name, ticker.upper()])

print(names_with_ticker)
# print(names_with_ticker)
# df = pd.DataFrame(names_with_ticker)
# df.to_csv('output.csv')
    # print(links[0].attrs['href'])
# raw = requests.get("https://www.google.com")
# print(raw.content)
# soup = BeautifulSoup(raw.content, "lxml")
# links = soup.findAll("a")
# for index, link in enumerate(links):
#     print("link {index}: {link}".format(link=link, index=index+1))
# names = data['name'].tolist()
# print(type(names[0]))
#name, display_name
# data = pd.read_csv('data.csv')
# names = []
# for name in data['name'].tolist():
#     names.append([name.replace(' ', '+')])

# for index, name in enumerate(data['display_name'].tolist()):
#     names[index].append(name.replace(' ', '+'))

# test = names[0][0]
# search_query = f"https://www.google.com/search?q={test}"
# raw = requests.get(search_query)
# soup = BeautifulSoup(raw.content, "lxml")
# links = soup.findAll("a")
# for index, link in enumerate(links):
#     print(f"link {index}: {link}")
# for name, display_name in names:
#     search_query = f"https://www.google.com/search?q={name}"
#     raw = requests.get(search_query)
#     soup = BeautifulSoup(raw.content, "lxml")
#     links = soup.findAll("a")
