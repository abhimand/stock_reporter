import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

from datetime import date,timedelta
from dateutil.parser import parse 


tomorrow = date.today() + timedelta(days=1)
today = date.today() + timedelta(days=0)
yesterday = date.today() - timedelta(days=1)

# set ticker
gme = yf.Ticker("GME")
bb = yf.Ticker("BB")
pltr = yf.Ticker("")
# get stock info
print(gme.info)
print(bb.info)
print(pltr.info)
# get historical market data
histGME = gme.history(period="1d")
histBB = bb.history(period="1d")
histPLTR = pltr.history(period="1d")

# Plot everything by leveraging the very powerful matplotlib package
histGME['Close'].plot(figsize=(16, 9))
histPLTR['Close'].plot(figsize=(16, 9))
histBB['Close'].plot(figsize=(16, 9)

plt.show()


data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "GME BB ABNB PLTR",
        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",
        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",
        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',
        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,
        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,
        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,
        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )
data.to_csv('combined.csv')
