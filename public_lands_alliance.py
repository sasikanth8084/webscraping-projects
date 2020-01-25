from bs4 import BeautifulSoup
from requests import get
import time

url = 'https://na.eventscloud.com/ehome/index.php?eventid=466693&tabid=948372'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
sum_url = []
page_soup = BeautifulSoup(r.content, 'html.parser')
main_table = page_soup.findAll('table', attrs={'id': 'outer_table'})
inner_table = main_table[0].find('table')
rows = inner_table.findAll('tr')
for row in rows:
    cols = row.findAll('td')
    if len(cols) == 1:
        continue
    else:
        print(cols[0].text+"  ---------- "+cols[1].text)

