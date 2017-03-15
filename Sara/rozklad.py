#-*- coding: utf-8 -*-
#!/usr/bin/env python
try:
    # For Python 3.0 and later
   import bs4 as bs
except ImportError:
    # Fall back to Python 2
    from bs4 import BeautifulSoup as bs

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2
    from urllib2 import urlopen
from datetime import datetime


hour = datetime.now().strftime('%H')
str_hour=str(hour)
if len(str_hour)==1:
    str_hour="0"+str_hour

minutes = datetime.now().strftime('%M')
data = datetime.now().strftime("%Y-%m-%d")
link = 'http://www.mazowieckie.com.pl/pl/jsearch?station_from=T%C5%82uszcz&station_from_id=37507&station_to=Warszawa+Wile%C5%84ska&station_to_id=37440&date='+data+'&hour='+str_hour+'%3A'+str(minutes)+'&by%5Bstation_by%5D%5B0%5D=&by%5Bstation_by_id%5D%5B0%5D=&op=Szukaj'

source = urlopen(link).read()
soup = bs.BeautifulSoup(source,'lxml')

for div in soup.find_all('div', class_='center'):
    print(div.text)
    break;


