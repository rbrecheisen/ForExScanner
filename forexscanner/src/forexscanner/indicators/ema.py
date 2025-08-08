import pandas as pd


class EMA:
    def __init__(self, period):
        self._period = period

    def calculate(self, candles):
        ema_series = candles['close'].ewm(span=self._period, adjust=False).mean()
        return ema_series.iloc[-1]