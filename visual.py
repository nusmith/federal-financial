import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot

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

# Plot
# fig, axs = plt.subplots(figsize=(12, 4))
# plt.xlabel("Time")
# plt.ylabel("Value")
# every_nth = 4
# for n, label in enumerate(axs.xaxis.get_ticklabels()):
#     if n % every_nth != 0:
#         label.set_visible(False)
# axs.plot(sp500['Date'], (sp500['Price'])/1000, "o", markersize=2, c="b", label="SP 500 Closing")
# #axs.plot(bond_spread['Date'], bond_spread['Spread'], marker="o", markersize=2, markerfacecolor='blue', label="10-2 Year Spread")
# #axs.plot(ir['Date'], ir['CPI'], marker="o", markersize=2, markerfacecolor='pink', label="CPI Level")
# axs.legend()
# plt.show()

plt.plot(sp500['Date'], (sp500['Price'])/1000, "o", markersize=2, c="b", label="SP 500 Closing")
plt.plot(bond_spread['Date'], bond_spread['Spread'], marker="o", markersize=2, markerfacecolor='blue', label="10-2 Year Spread")
plt.plot(ir['Date'], ir['CPI'], marker="o", markersize=2, markerfacecolor='pink', label="CPI Level")
plt.xticks(ticks = ['1976-06-01', '1981-06-01', '1990-06-01', '1996-06-03', '2001-06-01', '2006-06-01', '2010-06-01', '2016-06-01', '2023-03-01'],
           labels = ['1976', '1981', '1990', '1996', '2001', '2006', '2010', '2016', '2023'])
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
