from bs4 import BeautifulSoup as bs
from .models import Price_List, Metals, Currencies
import requests as r
import pandas as pd
import datetime as dt

metals = ['XAU', 'XAG']
currencies = ['USD', 'GBP', 'EUR']

base_url = 'https://www.exchangerates.org.uk/commodities/'
base = r.get(base_url)
soup = bs(base.text, features="html.parser")


def oz_to_gram(i):
    return float(i) / 31.10348
#TODO ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package

def get_data():
    df_data = []
    for metal in metals:
        for currency in currencies:
            m, created = Metals.objects.get_or_create(metal)
            c, created = Currencies.objects.get_or_create(currency)
            url = f'{base_url}{metal}-{currency}-history.html'
            base = r.get(url)
            soup = bs(base.text, features="html.parser")
            tbl = soup.find('table')
            Last_updated = tbl.find('i').text
            tbl_rows = tbl.find_all('tr')[2:]
            for row in tbl_rows:
                data = row.find_all('td')
                rowdate = dt.datetime.strptime(data[0].text, '%A %d %B %Y')
                rowamt = data[2].text
                rowgram = oz_to_gram(rowamt)
                rowdata = (rowdate, rowamt, metal, currency, rowgram)
                df_data.append(rowdata)
                pl = Price_List(metal=m, currency=c, date=rowdate, price=float(rowamt))
                pl.save()
    return df_data


da = pd.DataFrame(get_data())
da.to_csv('metal.csv')
