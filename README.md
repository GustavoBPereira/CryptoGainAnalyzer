# Crypto Gain Analyzer

## Overview

This Python project is designed to visualize the results of cryptocurrency investments in a simple manner. By providing investment data in the `cryptos_to_analyze.txt` file, the script processes the information and generates a visualization of the investment outcomes.

## Setup

1. **Clone the Repository:**
   ```
   git clone git@github.com:GustavoBPereira/CryptoGainAnalyzer.git
   ```
   
2. **Navigate to the Project Directory:**
   ```
   cd CryptoGainAnalyzer
   ```

3. **Create a Virtual Environment:**
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Required Libraries:**
   ```
   pip install -r requirements.txt
   ```

6. **Create a `.env` File:**
   - Create a file named `.env` in the project root directory.
   - Add the following line to the `.env` file, replacing `123` with your CoinAPI key:
     ```
     coin_api_key=123
     ```

7. **Obtain CoinAPI Key:**
   - Get your CoinAPI key from [CoinAPI](https://www.coinapi.io/).



## Add investment data for analysis

Add investment data to the `cryptos_to_analyze.txt` file in the following format:

```
<investment_amount> <crypto_symbol> <time_of_investment>
```

- `<investment_amount>`: The amount invested (e.g., R$1500.0) (BRL only for now).
- `<crypto_symbol>`: The symbol of the cryptocurrency (e.g., BTC, ETH, etc.).
- `<time_of_investment>`: The time of investment in the format `HH:MM-DD/MM/YYYY` (e.g., 2:00-22/12/2019).


| In current `cryptos_to_analyze.txt` file, you have a lot of examples, you can change or remove them.

## Running the Script

To run the script, follow these steps:

1. **Navigate to the Project Directory (if not already there):**
   ```
   cd path/to/crypto-investment-analyzer
   ```

2. **Run the Script:**
   ```
   python main.py
   ```

## Output

After running the script, the visualization of investment outcomes will be displayed.

## TODO's

- [ ] Add support for dollar (current just works in BRL)
- [ ] Gets automatically dollar and brl value to be used in conversion.
- [ ] Make the print prettier
- [ ] Refact main.py at the root project