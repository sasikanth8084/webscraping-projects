from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.routesonline.com/events/208/routes-americas-2020/attending-delegates/all/?list_order=#attendeeList'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
ul_con = page_soup.find('ul', class_='attendeeContainer')
li_con = ul_con.findAll('li', class_='tile memberTile')
print(li_con[0].p.strong.text)
print(li_con[0])
