import time
import forexscanner.constants as constants
from forexscanner.oandaclient import OandaClient
from forexscanner.indicators.ema import EMA
from forexscanner.indicators.atr import ATR
from forexscanner.mailer import Mailer


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

    def calculate_weekly_trend(self, candles):
        slow_ema = EMA(constants.FX_SLOW_EMA_PERIOD).calculate(candles)
        fast_ema = EMA(constants.FX_FAST_EMA_PERIOD).calculate(candles)
        offset_ratio = abs(fast_ema - slow_ema) / ATR(14).calculate(candles)
        if fast_ema > slow_ema and offset_ratio >= constants.FX_ATR_OFFSET_RATIO_W:
            return 1
        if fast_ema < slow_ema and offset_ratio >= constants.FX_ATR_OFFSET_RATIO_W:
            return -1
        return 0
    

def main():
    print('Loading candle data...')
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
    print('Running scanner...')
    scanner = ForExScanner(candle_data)
    scanner.start()


if __name__ == '__main__':
    main()