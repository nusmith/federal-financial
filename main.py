from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
from datetime import date


# Live Data (Webscraped)
today = date.today()
today_str = str(today)
today_Ym = today_str[0:7]


# this is for finding items in html source. not currently used. using request for csv download instead of scraping
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

stock_prices = []
stock_dates = []
stock_content_url = "https://stooq.com/q/d/l/?s=^spx&i=d"
csv = requests.get(stock_content_url)
soup = BeautifulSoup(csv.content, features="html.parser")
data = soup.text.split()

for d in data[1:]:
    set = d.split(sep=',')
    stock_dates.append(datetime.strptime(set[0], '%Y-%m-%d').date())
    stock_prices.append(float(set[4]))

df = pd.DataFrame({'Date': stock_dates, 'Price': stock_prices})
df.to_csv('sp_close.csv', index=False, encoding='utf-8')



spread = []
spread_dates = []
spread_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=T10Y2Y&scale=left&cosd=1976-06-01&coed={}&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date={}&revision_date={}&nd=1976-06-01".format(today_str, today_str, today_str)
csv = requests.get(spread_url)
soup = BeautifulSoup(csv.content, features="html.parser")
data = soup.text.split()

for d in data[1:]:
    pair = d.split(sep=',')
    spread_dates.append(datetime.strptime(pair[0], '%Y-%m-%d').date())
    spread.append(float(pair[1] + '0'))

df = pd.DataFrame({'Date': spread_dates, 'Spread': spread})
df.to_csv('spread.csv', index=False, encoding='utf-8')



cpi = []
cpi_dates = []
cpi_content_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCSL&scale=left&cosd=1947-01-01&coed={}&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date={}&revision_date={}&nd=1947-01-01".format(today_Ym + "-01", today_str, today_str)
print(cpi_content_url)
csv = requests.get(cpi_content_url)
soup = BeautifulSoup(csv.content, features="html.parser")
data = soup.text.split()

for d in data[1:]:
    pair = d.split(sep=',')
    cpi_dates.append(datetime.strptime(pair[0], '%Y-%m-%d').date())
    cpi.append(float(pair[1]))

df = pd.DataFrame({'Date': cpi_dates, 'CPI': cpi})
df.to_csv('cpi.csv', index=False, encoding='utf-8')


# Read CSV data and get unif start date
start_date = '1976-06-01'
# Closing Prices of SP 500
sp500 = pd.read_csv('/Users/nicolesmith/PycharmProjects/InterestRateModeling/sp_close.csv')
sp500 = sp500[['Date', 'Price']]
mask = (sp500['Date'] >= start_date)
sp500 = sp500.loc[mask]
# 10-2 year bond spread: starts 1976-06-01
bond_spread = pd.read_csv('/Users/nicolesmith/PycharmProjects/InterestRateModeling/spread.csv')
bond_spread = bond_spread[['Date', 'Spread']]
mask = (bond_spread['Date'] >= start_date)
bond_spread = bond_spread.loc[mask]
# CPI data
ir = pd.read_csv('/Users/nicolesmith/PycharmProjects/InterestRateModeling/cpi.csv')
ir = ir[['Date', 'CPI']]
mask = (ir['Date'] >= start_date)
ir = ir.loc[mask]



