from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.progreenexpo.com/Sponsors-&-Exhibitors/2020-Exhibitors'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
print(page_soup)
# table = page_soup.find('table', attrs={'class', 'dataTable no-footer'})
# print(table)