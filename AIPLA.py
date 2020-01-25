from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.aipla.org/MWI20/attendees'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
main_con = page_soup.find('ul', class_="item-list")
li_items = main_con.findAll('li', class_="item-list__item")
# print(li_items[0])
name =[]
org = []
for p_ta in li_items:
    pt = p_ta.findAll('p')
    n = pt[0].text
    print(n.strip())
    name.append(n.strip())

    print(pt[1].text)
    org.append(pt[1].text)

    print("--------------------------------------------------")
    # break
print(len(name))
print(len(org))

series_pd = pd.DataFrame({
    'Company': name,
    'WEBSITE': org,
})

csv_data = series_pd.to_csv('AIPLA.csv')
print("------------ DONE -----------------")
