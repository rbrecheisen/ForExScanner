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