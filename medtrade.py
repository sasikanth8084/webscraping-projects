from bs4 import BeautifulSoup
from requests import get
import time
import pandas as pd

url = 'https://medtrade.a2zinc.net/Spring2020/Public/exhibitors.aspx?Index=All&ID=21830'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
# print(page_soup)
table = page_soup.find('table', attrs={'class': 'table table-striped table-hover'})
table_body = table.find('tbody')
# print(table_body)
rows = table_body.findAll('tr')
# print(rows[0])
links = []
for row in rows:
    cols = row.findAll('td')
    # https://medtrade.a2zinc.net/Spring2020/Public/
    links.append("https://medtrade.a2zinc.net/Spring2020/Public/"+cols[1].a['href'])
c_name = []
c_url = []
for urls in links:
    url2 = urls
    r = get(urls, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup2 = BeautifulSoup(r.content, 'html.parser')

    booth_info = page_soup2.find('div', class_='panel-body')
    # print(booth_info)
    h1 = booth_info.find('h1')
    print(h1.text)
    c_name.append(h1.text)
    website = booth_info.find('span', class_='BoothContactUrl')
    if website is None:
        print("http://www.NOWEBSITE.com")
        c_url.append("http://www.NOWEBSITE.com")
    else:
        print(website.a.text)
        c_url.append(website.a.text)
    time.sleep(2)
print(len(c_name))
print(len(c_url))

series_pd = pd.DataFrame({
    'Company': c_name,
    'WEBSITE': c_url,
})

csv_data = series_pd.to_csv('med-trade.csv')
print("------------ DONE -----------------")

