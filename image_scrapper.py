import requests
from bs4 import BeautifulSoup
import pandas as pd

# Extract
def extract(page):
	headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
	url = f"https://it.indeed.com/jobs?q=data+analyst&l=Italia&sort=date&lang=en&start={page}"
	r = requests.get(url, headers)
	soup = BeautifulSoup(r.content, "html.parser")
	return soup
