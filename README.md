# ForExScanner
Scanner for ForEx candlestick formations

# How it works
The scanner retrieves the last N candles from OANDA for any given symbol. It checks whether the last candle
matches one or more candlestick formations that could be interesting buying or selling opportunities. If it
finds such a formation, it alerts the user visually and by email. It shows the date when this candle occurred.
Normally, that would be today's or yesterday's date. Then the user can open MT5 and check the whole price chart
and see whether he can place an order or not. 

To test the scanner it can search for candidate formations in historical data as well. It will also output a
date where it thinks an interesting formation occurs. The user can use a special EA script to jump to this 
date in MT5, or use ForEx Simulator to fix the price chart at that date. Then the user can place buy/sell stops,
stop losses and take profit levels and step forward one candle at a time to see what happens. 

# Trading opportunities
The scanner first determines whether the weekly chart is trending or not. It does this using the MACD histogram
or a fast/slow EMA crossover.

If the weekly chart is trending the scanner will then look for buying or selling big shadow candles (in the daily
chart) with their respective properties: engulfing the previous candles, biggest candle in a while, lots of room 
to the left and a closing/opening price close to the high/low.

# Technical aspects
- Weekly EMA 20+50 cross-over + ADX(14) for momentum

# ATX(14)

Using python how can I calculate ATX(14)?


ChatGPT said:
To calculate ATX(14) (Average True Range Exponential Moving Average with period 14), you can follow these steps in Python using Pandas:

Steps to Calculate ATX(14):
Calculate True Range (TR).

Calculate Average True Range (ATR(14)).

Calculate the Exponential Moving Average (EMA) of ATR(14) — this is ATX(14).

Python Code Example:
python
Copy
Edit
import pandas as pd

# Example DataFrame with OHLC
data = {
    'High': [120, 125, 130, 128, 132, 135, 138, 140, 142, 145, 147, 150, 152, 155, 158],
    'Low': [115, 118, 125, 124, 128, 130, 134, 136, 138, 140, 142, 145, 148, 150, 153],
    'Close': [118, 123, 128, 126, 130, 133, 136, 138, 140, 143, 145, 148, 150, 153, 156]
}
df = pd.DataFrame(data)

# 1. Calculate True Range (TR)
df['prev_close'] = df['Close'].shift(1)
df['tr1'] = df['High'] - df['Low']
df['tr2'] = abs(df['High'] - df['prev_close'])
df['tr3'] = abs(df['Low'] - df['prev_close'])
df['TR'] = df[['tr1', 'tr2', 'tr3']].max(axis=1)

# 2. Calculate ATR(14)
df['ATR14'] = df['TR'].rolling(window=14).mean()

# 3. Calculate EMA of ATR(14) --> This is ATX(14)
df['ATX14'] = df['ATR14'].ewm(span=14, adjust=False).mean()

print(df[['TR', 'ATR14', 'ATX14']])
Key Point:
ATX(14) is essentially an EMA of ATR(14).

If you're coding for live trading, you probably want a function that updates this dynamically with each new candle.

Do you want me to give you a version that works directly with Pandas DataFrames from a TradingView export CSV?