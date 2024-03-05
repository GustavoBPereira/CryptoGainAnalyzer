from cryptogainanalyzer import FileManager, CoinApiConsumer
from decouple import config

from cryptogainanalyzer.constants import DOLAR_VALUE_IN_BRL, BRL_VALUE_IN_DOLAR

consumer = CoinApiConsumer(config("coin_api_key"))

with open("cryptos_to_analyze.txt", "r") as f:
    cryptos = FileManager(f.read()).currencies_to_consult

totals = {"investment": 0, "result": 0}

for crypto in cryptos:
    try:
        historical_data = consumer.get_historical_data(
            crypto["currency"], crypto["time"]
        )["bid_price"]
        current_value = consumer.get_current_data(crypto["currency"])["bid_price"]
        investment_result = (current_value * crypto["investment"]) / historical_data

        historical_data *= BRL_VALUE_IN_DOLAR
        current_value *= BRL_VALUE_IN_DOLAR
        investment_result *= BRL_VALUE_IN_DOLAR
        investment_in_brl = crypto["investment"] / DOLAR_VALUE_IN_BRL

        totals["investment"] += investment_in_brl
        totals["result"] += investment_result

        print(
            f"{investment_in_brl:.2f} in {crypto['currency']} -> {investment_result:.2f}"
        )
    except:
        print(f" Error on {crypto['currency']}")

print(
    f"\n -------- Totals --------\n Investments: {totals['investment']:.2f} \n Results: {totals['result']:.2f}"
)
