import oandapyV20

from oandapyV20.endpoints.accounts import AccountDetails

import forexscanner.constants as constants

client = oandapyV20.API(
    access_token=constants.FX_API_KEY, environment=constants.FX_ENVIRONMENT)

request = AccountDetails(accountID=constants.FX_ACCOUNT_ID)
response = client.request(request)

print(response)
