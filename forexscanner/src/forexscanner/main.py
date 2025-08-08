import time
import forexscanner.constants as constants
from forexscanner.oandaclient import OandaClient
from forexscanner.mailer import Mailer
from forexscanner.indicators.ema import EMA
from forexscanner.indicators.atr import ATR


# with OandaClient() as client:
#     # print(client.historical_candles('EUR_USD', granularity='D', start_date='2020-01-01T00:00:00Z'))
#     print(client.get_latest_candles('EUR_USD', granularity='D', count=1))
# with Mailer() as mailer:
#     mailer.send('OandaClient.get_latest_candles()', 'Success!')


class ForExScanner:
    NONE = 0
    UP = 1
    DOWN = -1

    def __init__(self, candle_data):
        self._candle_data = candle_data

    def start(self):
        try:
            for symbol in self._candle_data.keys():
                latest_weekly_candles = self._candle_data[symbol]['W']
                while True:
                    trend = self.calculate_weekly_trend(latest_weekly_candles)
                    if trend == ForExScanner.UP:
                        print('weekly trend is up')
                    elif trend == ForExScanner.DOWN:
                        print('weekly trend is down')
                    elif trend == ForExScanner.NONE:
                        print('no weekly trend')
                    else:
                        pass
                    time.sleep(2)
        except KeyboardInterrupt:
            print('quiting...')

    def get_weekly_candles(self, symbol):
        return self._candle_data[symbol]['W']

    def get_daily_candles(self, symbol):
        return self._candle_data[symbol]['D']

    def calculate_weekly_trend(self, candles):
        slow_ema = EMA(constants.FX_SLOW_EMA_PERIOD).calculate(candles)
        fast_ema = EMA(constants.FX_FAST_EMA_PERIOD).calculate(candles)
        offset_ratio = abs(fast_ema - slow_ema) / ATR(14)
        if fast_ema > slow_ema and offset_ratio >= 0.5:
            return 1
        if fast_ema < slow_ema and offset_ratio >= 0.5:
            return -1
        return 0
    

def main():
    with OandaClient() as client:
        candle_data = {}
        for symbol in constants.FX_SYMBOLS:
            candle_data[symbol] = {
                'W': client.get_latest_candles(
                        symbol, 
                        granularity='W', 
                        count=constants.FX_SLOW_EMA_PERIOD,
                    ),
                'D': client.get_latest_candles(
                        symbol, 
                        granularity='D', 
                        count=constants.FX_SLOW_EMA_PERIOD,
                    ),
            }
    scanner = ForExScanner(candle_data)
    scanner.start()


if __name__ == '__main__':
    main()