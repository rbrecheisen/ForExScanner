import oandapyV20

from oandapyV20.endpoints.accounts import AccountDetails

API_KEY = 'a856b96f70cfe8fc507765857fa98b56-94e46be1ae266b09fa59fb259ec9dcd5'
ACCOUNT_ID = '101-004-30581840-001'
API_URL = "https://api-fxpractice.oanda.com"  # Use 'https://api-fxtrade.oanda.com' for LIVE accounts

client = oandapyV20.API(access_token=API_KEY, environment="practice")  # use 'live' for live trading

request = AccountDetails(accountID=ACCOUNT_ID)
response = client.request(request)

print(response)
