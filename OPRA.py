from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time

url = 'https://opraonline.org/exhibitors/'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
con = page_soup.findAll('div', class_='vc_pageable-slide-wrapper vc_clearfix')
# inner_con = con[0].findAll('div', class_='vc_grid-item vc_clearfix vc_col-sm-4 vc_grid-item-zone-c-bottom vc_visible-item')
links = con[0].findAll('a', class_='vc_gitem-link')
urls = []
for link in links:
    # print(link['href'])
    urls.append(link['href'])
c_name = []
c_url = []
for nurl in urls:
    url2 = nurl
    r = get(url2, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup2 = BeautifulSoup(r.content, 'html.parser')
    name = page_soup2.find('h1', class_='title')
    print(name.text)
    c_name.append(name.text)
    # print(page_soup2)

    if (page_soup2.find('div', class_='wpb_wrapper')) is None:
        container = page_soup2.find('div', class_='the_content_wrapper')
        a_tags = container.findAll('a')
        print(a_tags[1].strong.text)
        c_url.append(a_tags[1].strong.text)
    else:
        container = page_soup2.find('div', class_='wpb_wrapper')
        print(container.a['href'])
        c_url.append(container.a['href'])

print(len(c_name))
print(len(c_url))

series_pd = pd.DataFrame({
    'Company': c_name,
    'WEBSITE': c_url,
})

csv_data = series_pd.to_csv('OPRA.csv')
print("------------ DONE -----------------")


