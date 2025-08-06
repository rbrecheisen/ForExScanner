import time
from forexscanner.oandaclient import OandaClient
from forexscanner.mailer import Mailer

with OandaClient() as client:
    # print(client.historical_candles('EUR_USD', granularity='D', start_date='2020-01-01T00:00:00Z'))
    print(client.get_latest_candles('EUR_USD', granularity='D', count=1))

with Mailer() as mailer:
    mailer.send('OandaClient.get_latest_candles()', 'Success!')


class ForExScanner:
    UP = 1
    DOWN = 2
    NONE = 0

    def __init__(self):
        pass

    def start(self):
        try:
            while True:
                trend = self.get_weekly_trend()
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

    def get_weekly_trend(self):
        return 0 # 0 = no trend, 1 = uptrend, 2 = downtrend


if __name__ == '__main__':
    scanner = ForExScanner()
    scanner.start()