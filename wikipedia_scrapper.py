import requests
from bs4 import BeautifulSoup
import pandas as pd

# US ELECTION RESULTS 2020


wiki_url = "https://en.wikipedia.org/wiki/2020_United_States_presidential_election"
table_id = "wikitable sortable jquery-tablesorter"
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

election_table = soup.find('div', attrs={'class': table_id})
df = pd.read_html(str(election_table))

#print(df.info)
print(df)
#df.to_csv('wiki_2020_election.csv')