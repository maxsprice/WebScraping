from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

url = 'https://www.basketball-reference.com/draft/'
r = requests.get(url)
r.status_code
soup = BeautifulSoup(r.text)

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if 'draft/' in href:
        links.append(href)
# for i in range(1,len(links)):
#     links[i] = ''.join(str(links[i]))
links = ',https://www.basketball-reference.com'.join(links)
links = links.split(",")
links = links[1:77]
links

def directory_item(bs, tag, search, direct, col):
    item = bs.find_all(tag, {"data-stat": search})
    for info in item:
        direct[col].append(info.get_text())
        
        directory = {'Pick':[], 'Team':[], 'Player':[], 'College':[], 'Yrs Played':[], 'Min Per Game':[], 'Points Avg.':[], 'Rebounds Avg.':[], 'Assists Avg.':[]}
for url in links:
    r = requests.get(url)
    if r.status_code == 200:
        bs = BeautifulSoup(r.text)
        directory_item(bs, "td", "pick_overall",directory, 'Pick')
        directory_item(bs, "td", "team_id",directory, 'Team')
        directory_item(bs, "td", "player",directory, 'Player')
        directory_item(bs, "td", "college_name",directory, 'College')
        directory_item(bs, "td", "seasons",directory, 'Yrs Played')
        directory_item(bs, "td", "mp_per_g",directory, 'Min Per Game')
        directory_item(bs, "td", "pts_per_g",directory, 'Points Avg.')
        directory_item(bs, "td", "trb_per_g",directory, 'Rebounds Avg.')
        directory_item(bs, "td", "ast_per_g",directory, 'Assists Avg.')
Playerdf = pd.DataFrame(directory)

Playerdf.to_csv('DraftData.csv')
