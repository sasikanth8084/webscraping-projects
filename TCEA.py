from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://register.tcea.org/exhibitor_exhibitor_list.cfm'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
table = page_soup.find('table', attrs={'id': 'exh_list'})
rows = table.findAll('tr', class_='')
c_name= []
for row in rows:
    cols = row.findAll('td')
    if len(cols) == 2:
        print(cols[1].u.a.text)
        c_name.append(cols[1].u.a.text)
    else:
        print("--- ( "+cols[0].b.text+" ) ----")
    # break

print(len(c_name))
print(len(c_name))


series_pd = pd.DataFrame({
    'Company': c_name,

})

csv_data = series_pd.to_csv('TCEA.csv')
print("------------ DONE -----------------")
