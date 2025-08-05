import datetime
import oandapyV20
import pandas as pd
import forexscanner.constants as constants
from oandapyV20.endpoints.accounts import AccountDetails
from oandapyV20.endpoints.instruments import InstrumentsCandles


class OandaClient:
    def __init__(self):
        self._client = None

    def __enter__(self):
        self._client = oandapyV20.API(
            access_token=constants.FX_API_KEY, environment=constants.FX_ENVIRONMENT)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client = None

    def account_details(self):
        request = AccountDetails(accountID=constants.FX_ACCOUNT_ID)
        response = self._client.request(request)
        return response

    def historical_candles(self, instrument, granularity, start_date):
        all_candles = []
        date_start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
        date_now = datetime.datetime.now()
        while date_start < date_now:
            params = {
                'granularity': granularity,
                'from': date_start.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'count': 5000,
                'price': 'M',
            }
            data = InstrumentsCandles(instrument=instrument, params=params)
            self._client.request(data)
            candles = data.response['candles']
            if not candles:
                break
            all_candles.extend(candles)
            date_start = datetime.datetime.strptime(candles[-1]['time'], '%Y-%m-%dT%H:%M:%S.%f000Z')
            date_start += datetime.timedelta(seconds=1)
            if len(candles) < 5000:
                break
        completed_candles = [c for c in all_candles if c['complete']]
        df = pd.DataFrame([{
            'time': c['time'],
            'open': float(c['mid']['o']),
            'high': float(c['mid']['h']),
            'low': float(c['mid']['l']),
            'close': float(c['mid']['c']),
        } for c in completed_candles])
        return df
    
    def latest_candles(self, instrument, granularity, count=1):
        params = {
            'granularity': granularity,
            'count': count + 1,
            'price': 'M',
        }
        data = InstrumentsCandles(instrument=instrument, params=params)
        self._client.request(data)
        candles = data.response['candles']
        completed_candles = [c for c in candles if c['complete']]
        selected_candles = completed_candles[-count:]
        df = pd.DataFrame([{
            'time': c['time'],
            'open': float(c['mid']['o']),
            'high': float(c['mid']['h']),
            'low': float(c['mid']['l']),
            'close': float(c['mid']['c']),
        } for c in selected_candles])
        return df