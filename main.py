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
def get_ticker(name):
    """
    Function to encapsulate for loop and execute every time to get ticker symbol
    Also check whether direct match or indirect, and list all further matches as well
    """
    
for name in names[:50]:
    search_query = f"https://www.google.com/search?q={name.replace(' ','+').replace('(', '').replace(')', '')}+yahoo+finance"
    # print(search_query)
    raw = requests.get(search_query)
    soup = BeautifulSoup(raw.text, "lxml")
    headers = soup.findAll("h3")
    match = False
    for header in headers:
        text = header.string
        # print(text)
        # print('__')
        remove_irrelevant_brackets = lambda text: re.sub('\([A-Za-z][a-z]*\)', '', text)
        text = remove_irrelevant_brackets(text)
        # print(text)
        match = re.search(r'\((\S*?)\)', text)
        if match == None:
            ticker = False
        else:
            ticker = match.group(1)
            # print('match found')
            break
    if not ticker:
        print(f"{name} had no match")
        names_with_ticker.append([name, 'undefined'])
    else:
        print(f"{name} had {ticker.upper()} as ticker symbol")
        names_with_ticker.append([name, ticker.upper()])

df = pd.DataFrame(names_with_ticker)
df.to_csv('output.csv')