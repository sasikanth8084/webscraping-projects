from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time


url = 'https://southernshows.com/sfs/exhibitors'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
con = page_soup.find('div', class_='padMainTop')
links = con.findAll('a', string='Learn More')
print(len(links))
inner_urls = []
for link in links:
    inner_urls.append("https://southernshows.com"+link['href'])
c_name =[]
c_url = []
for urls in inner_urls:
    url1 = urls
    r = get(url1, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup = BeautifulSoup(r.content, 'html.parser')
    name = page_soup.find('h2', class_='sfs')
    link = page_soup.find('div', class_='table margin')
    print(name.span.text)
    c_name.append(name.span.text)
    if link is None:
        print("no website")
        c_url.append("no website")
    else:
        print(link.a['href'])
        c_url.append(link.a['href'])
    time.sleep(2)

print(len(c_name))
print(len(c_url))


series_pd = pd.DataFrame({
    'Company': c_name,
    'Website': c_url,

})

csv_data = series_pd.to_csv('southern_farm_show.csv')
print("------------ DONE -----------------")
