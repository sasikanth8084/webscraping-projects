from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://www.joc-tpm.com/attendees'
r = get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
})
page_soup = BeautifulSoup(r.content, 'html.parser')
main_container = page_soup.findAll('div', id='comp-jurgyz81')
p_tags = main_container[0].findAll('p')
c_name = []
for names in p_tags:
    if names.span.span is None:
        print(names.span.text)
        c_name.append(names.span.text)
    else:
        print(names.span.span.text)
        c_name.append(names.span.span.text)

print(len(c_name))
series_pd = pd.DataFrame({
    'Company': c_name,

})

csv_data = series_pd.to_csv('JOC-Events.csv')