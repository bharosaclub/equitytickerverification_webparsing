from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import numpy as np
from similarity_checker import *
data = pd.read_csv('data.csv')
names = []
for name in data['display_name'].tolist():
    names.append(name)
names_with_ticker = []

test_list = ['Nestle SA', 'Wal-Mart Stores Inc']
removals = ['Amalgamated','Private', 'Limited', 'Ltd.', 'Inc.', 'Inc', 'Ltd', 'Corp']
for name in names[:(len(names)-1)]:
    try:
        for removal in removals:
            name = name.replace(removal, '')
            name = name.strip()
        search_query = f"https://www.google.com/search?q={name.replace(' ','+').replace('(', '').replace(')', '')}+yahoo+finance"
        raw = requests.get(search_query)
        soup = BeautifulSoup(raw.text, "lxml")
        headers = soup.findAll("h3")
        match = False
        for header in headers:
            text = header.string
            remove_irrelevant_brackets = lambda text: re.sub('\([A-Za-z][a-z]*\)', '', text)
            text = remove_irrelevant_brackets(text)
            match = re.search(r'(.*)\((\S*?)\)', text)
            if match == None:
                ticker = False
            else:
                ticker = match.group(2)
                response = match.group(1)
                for removal in removals:
                    response = response.replace(removal, '')
                    response = response.strip()
                break
        if not ticker:
            print(f"{name} had no match")
            names_with_ticker.append([name, response, 'undefined', 0])
        else:
            print(f"{name} had {ticker.upper()} as ticker symbol")
            similarity = similarity_checker(name, response)
            names_with_ticker.append([name, response, ticker.upper(), similarity[2]])
    except:
        print(f"\n \n \n {name} could not be read from csv \n \n \n")
        names_with_ticker.append([name, "none", "none", "none", "none"])

print(names_with_ticker)
df = pd.DataFrame(names_with_ticker)
df.to_csv('output.csv')