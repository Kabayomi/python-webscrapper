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

# Transform
def transform(soup):
	divs = soup.find_all("div",class_= "jobsearch-SerpJobCard")
	for element in divs:
		title = element.find("a").text.strip()
		company = element.find("span", class_="company").text.strip()
		try:
			location = element.find("span", class_="location").text.strip()
			salary = element.find("span", class_="salaryText").text.strip()
		except:
			location = ""
			salary = ""
		summary = element.find("div", {"class": "summary"}).text.strip().replace('\n', "")
		
		job = {
			"title": title,
			"company": company,
			"location": location,
			"salary": salary,
			"summary": summary
		}
		joblist.append(job)
	return 

# Load
joblist = []

for i in range(0,40,10):
	print(f"Getting page, {i}")
	c = extract(0)
	transform(c)
	print(joblist)

# To pandas
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('job.csv')