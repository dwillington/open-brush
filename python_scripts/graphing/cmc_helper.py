from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

def getCryptoData():
  BASE_URL = 'https://sandbox-api.coinmarketcap.com'
  endpoint = '/v2/cryptocurrency/quotes/latest'
  endpoint = '/ohlcv/historical'
  url = BASE_URL + endpoint
  
  parameters = {
      'id': '1', 'interval': 'hourly'
  }
# 'aux': 'num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,is_active,is_fiat'
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(json.dumps(data, indent=2))
  return data


def main():
  getCryptoData()

if __name__ == '__main__':
    main()

