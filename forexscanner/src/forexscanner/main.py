from forexscanner.oandaclient import OandaClient

with OandaClient() as client:
    # print(client.historical_candles('EUR_USD', granularity='D', start_date='2020-01-01T00:00:00Z'))
    print(client.latest_candles('EUR_USD', granularity='D', count=1))
