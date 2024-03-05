import requests


class CoinApiConsumer:
    BASE_URL = "https://rest.coinapi.io"
    EXCHANGE = "BINANCE_SPOT"

    def __init__(self, api_key: str):
        self.headers = {"Accept": "text/plain", "X-CoinAPI-Key": api_key}

    def get_historical_data(self, crypto: str, moment_to_consult: str):
        url = f"{self.BASE_URL}/v1/quotes/{self.EXCHANGE}_{crypto}_USDT/history?time_start={moment_to_consult}&limit=1"
        req = requests.request("GET", url, headers=self.headers, data={})
        return req.json()[0]

    def get_current_data(self, crypto: str):
        url = f"{self.BASE_URL}/v1/quotes/latest?filter_symbol_id={self.EXCHANGE}_{crypto}_USDT&limit=1"
        req = requests.request("GET", url, headers=self.headers, data={})
        return req.json()[0]
