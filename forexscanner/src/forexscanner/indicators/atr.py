import pandas as pd


class ATR:
    def __init__(self, period):
        self._period = period

    def calculate(self, candles):
        high_low = candles['high'] - candles['low']
        high_close = (candles['high'] - candles['close'].shift()).abs()
        low_close = (candles['low'] - candles['close'].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        atr_series = tr.ewm(alpha=1/self._period, adjust=False).mean()
        return float(atr_series.iloc[-1])
