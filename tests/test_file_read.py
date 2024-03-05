from cryptogainanalyzer import FileManager


def test_correct_file_format_should_return_correct_data_structure(correct_file_return):

    assert FileManager(correct_file_return).currencies_to_consult == [
        {"investment": 120, "currency": "BTC", "time": "2020-01-01T18:30:00Z"},
        {"investment": 1500.0, "currency": "ETH", "time": "2019-12-21T23:00:00Z"},
    ]
