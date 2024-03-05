import unittest
from unittest.mock import MagicMock, patch

from cryptogainanalyzer import CoinApiConsumer


class TestCoinApiConsumer(unittest.TestCase):
    @patch("requests.request")
    def test_get_historical_data(self, mock_request):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "symbol_id": "BINANCE_SPOT_BTC_USDT",
                "time_exchange": "2020-01-01T18:30:00.0156778Z",
                "time_coinapi": "2020-01-01T18:30:00.0155925Z",
                "ask_price": 7236.28,
                "ask_size": 0.060788,
                "bid_price": 7235.65,
                "bid_size": 0.134379,
            }
        ]
        mock_request.return_value = mock_response

        coin_api_consumer = CoinApiConsumer("api_key_for_test")
        moment_to_consult = "2020-01-01T18:30:00Z"

        result = coin_api_consumer.get_historical_data("BTC", moment_to_consult)
        expected_result = {
            "symbol_id": "BINANCE_SPOT_BTC_USDT",
            "time_exchange": "2020-01-01T18:30:00.0156778Z",
            "time_coinapi": "2020-01-01T18:30:00.0155925Z",
            "ask_price": 7236.28,
            "ask_size": 0.060788,
            "bid_price": 7235.65,
            "bid_size": 0.134379,
        }

        self.assertEqual(result, expected_result)
        mock_request.assert_called_once_with(
            "GET",
            f"https://rest.coinapi.io/v1/quotes/BINANCE_SPOT_BTC_USDT/history?time_start={moment_to_consult}&limit=1",
            headers={"Accept": "text/plain", "X-CoinAPI-Key": "api_key_for_test"},
            data={},
        )

    @patch("requests.request")
    def test_get_current_data(self, mock_request):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "symbol_id": "BINANCE_SPOT_BTC_USDT",
                "time_exchange": "2024-03-04T21:52:29.7280170Z",
                "time_coinapi": "2024-03-04T21:52:29.7280170Z",
                "ask_price": 67182.98,
                "ask_size": 2.8548,
                "bid_price": 67182.97,
                "bid_size": 1.92712,
            }
        ]
        mock_request.return_value = mock_response

        coin_api_consumer = CoinApiConsumer("api_key_for_test")
        result = coin_api_consumer.get_current_data("BTC")
        expected_result = {
            "symbol_id": "BINANCE_SPOT_BTC_USDT",
            "time_exchange": "2024-03-04T21:52:29.7280170Z",
            "time_coinapi": "2024-03-04T21:52:29.7280170Z",
            "ask_price": 67182.98,
            "ask_size": 2.8548,
            "bid_price": 67182.97,
            "bid_size": 1.92712,
        }

        self.assertEqual(result, expected_result)
        mock_request.assert_called_once_with(
            "GET",
            f"https://rest.coinapi.io/v1/quotes/latest?filter_symbol_id=BINANCE_SPOT_BTC_USDT&limit=1",
            headers={"Accept": "text/plain", "X-CoinAPI-Key": "api_key_for_test"},
            data={},
        )
