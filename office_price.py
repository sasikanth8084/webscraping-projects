from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time

urls = []
for i in range(0, 19):
    url = 'https://www.offpriceshow.com/lasvegas/exhibitor-list?page={}'.format(i)
    r = get(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup = BeautifulSoup(r.content, 'html.parser')
    con = page_soup.findAll('div', class_='exhibitor-list basic')
    for det in con:
        view_profile = det.find('li', class_='url')
        print("https://www.offpriceshow.com" + view_profile.a['href'])
        urls.append("https://www.offpriceshow.com" + view_profile.a['href'])
    print("------------------------------- "+str(i)+" -----------------------------")
    time.sleep(2)
c_name=[]
c_url =[]
for url1 in urls:
    r = get(url1, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    })
    page_soup2 = BeautifulSoup(r.content, 'html.parser')
    vcard = page_soup2.find('div', class_='vcard')
    name = vcard.find('h1', class_='fn org region-row')
    print(name.text)
    web_con = page_soup2.find('ul', class_='content-btn')
    web = web_con.findAll('li')

    if len(web) == 1:
        print("no website")
        c_url.append("NO WEBSITE")
    else:
        print(web[1].a['href'])
        c_url.append(web[1].a['href'])
    c_name.append(name.text)

    time.sleep(2)
    # break

print(len(c_name))
print(len(c_name))


series_pd = pd.DataFrame({
    'Company': c_name,
    'Website': c_url,

})

csv_data = series_pd.to_csv('office_price.csv')
print("------------ DONE -----------------")

# url1 = 'https://www.offpriceshow.com/lasvegas/exhibitor/2-blue-denim-co-llc'
# r = get(url1, headers={
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
#     })
# page_soup2 = BeautifulSoup(r.content, 'html.parser')
# vcard = page_soup2.find('div', class_='vcard')
# name = vcard.find('h1', class_='fn org region-row')
# print(name.text)
# web_con = page_soup2.find('ul', class_='content-btn')
# web = web_con.findAll('li')
# print(len(web))
# if len(web)==1:
#     print("no website")
# else:
#     print(web[1].a['href'])
# c_name.append(name.text)
#
# time.sleep(2)
