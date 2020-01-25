from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.vinexponewyork.com/exhibitor-list/'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
table = page_soup.find('table')
tbody = table.find('tbody')
rows = tbody.findAll('tr')
company = []
country = []
for row in rows:
    cols = row.findAll('td')
    company.append(cols[0].p.text)
    country.append(cols[1].p.text)
    print(cols[1].p.text)
    # break

series_pd = pd.DataFrame({
    'Company': company,
    'Country' : country,

})

csv_data = series_pd.to_csv('vineExpo.csv')