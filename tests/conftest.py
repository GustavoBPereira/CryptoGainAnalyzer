from pytest import fixture


@fixture
def correct_file_return():
    with open("cryptos_to_analyze.test", "r") as f:
        return f.read()
