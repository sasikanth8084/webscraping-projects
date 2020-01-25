from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.astastrings.org/NationalConference/Sponsors/NationalConference/Exhibitors.aspx?hkey=00f2d71a-e237-46b9-a3b3-2ad2a69644c2'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
main_table = page_soup.find('table', attrs={'id':'ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Grid1_ctl00'})
t_body = main_table.find('tbody')
rows = t_body.findAll('tr')
c_name = []
c_url = []
for row in rows:
    cols = row.findAll('td')
    print(" name "+cols[0].text)
    print(" url "+cols[1].text)
    c_name.append(cols[0].text)
    c_url.append(cols[1].text)
print(len(c_name))
print(len(c_url))

series_pd = pd.DataFrame({
    'Company': c_name,
    'WEBSITE': c_url,
})

csv_data = series_pd.to_csv('ASTA.csv')
print("------------ DONE -----------------")