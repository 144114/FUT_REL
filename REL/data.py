import yfinance as yf

ticker_MNQ = "NQ=F"   # E-mini Nasdaq-100 (as an alternative to MNQ)
ticker_MES = "ES=F"   # E-mini S&P 500 (as an alternative to MES)
ticker_CL = "CL=F"    # Crude Oil
ticker_GC = "GC=F"    # Gold
ticker_ZC = "ZC=F"    # Corn
ticker_ZB = "ZB=F"    # U.S. Treasury Bond

MNQ = yf.download(tickers=ticker_MNQ, interval="5m", period="60d")
MES = yf.download(tickers=ticker_MES, interval="5m", period="60d")
CL = yf.download(tickers=ticker_CL, interval="5m", period="60d")
GC = yf.download(tickers=ticker_GC, interval="5m", period="60d")
ZC = yf.download(tickers=ticker_ZC, interval="5m", period="60d")
ZB = yf.download(tickers=ticker_ZB, interval="5m", period="60d")

def set_timezone(data, timezone='America/New_York'):
    if data.index.tz is None:
        data = data.tz_localize('UTC')  
    return data.tz_convert(timezone)

MNQ = set_timezone(MNQ, timezone='America/New_York')
MES = set_timezone(MES, timezone='America/New_York')
CL = set_timezone(CL, timezone='America/New_York')
GC = set_timezone(GC, timezone='America/New_York')
ZC = set_timezone(ZC, timezone='America/New_York')
ZB = set_timezone(ZB, timezone='America/New_York')