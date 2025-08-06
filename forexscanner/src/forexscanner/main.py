from forexscanner.oandaclient import OandaClient
from forexscanner.mailer import Mailer

with OandaClient() as client:
    # print(client.historical_candles('EUR_USD', granularity='D', start_date='2020-01-01T00:00:00Z'))
    print(client.get_latest_candles('EUR_USD', granularity='D', count=1))
    with Mailer() as mailer:
        mailer.send('OandaClient.get_latest_candles()', 'Success!')