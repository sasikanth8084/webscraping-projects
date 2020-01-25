from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'http://biomassconference.com/ema/ExhibitorList.aspx'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
table = page_soup.find('table',
                       attrs={'id': 'ctl00_ContentPlaceHolder1_grdExhibitors_ctl01'})
# print(table)
tbody = table.find('tbody')
rows = tbody.findAll('tr')
# print(rows[0])
c_name = []
c_url = []
for row in rows:
    cols = row.findAll('td')
    print(cols[0].a.text)
    if cols[0].a.get('href') is None:
        print("no website")
        c_url.append("no website")
    else:
        print(cols[0].a['href'])
        c_url.append(cols[0].a['href'])
    c_name.append(cols[0].a.text)

    # break


print(len(c_name))
print(len(c_url))


series_pd = pd.DataFrame({
    'Company': c_name,
    'Website': c_url,

})

csv_data = series_pd.to_csv('BIO-MASS.csv')
print("------------ DONE -----------------")
