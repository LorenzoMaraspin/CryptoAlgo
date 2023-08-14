from Api.binance_api import BinanceApi
from Business.hystorical_data_formatter import HystoricalDataFormatter
from Business.markov_chain import MarkovTheorem
from Business.markov_chain_2 import MarkovImplementation
from Utility.timer import Timer
import logging
import time
import schedule

logging.basicConfig(format='%(asctime)s : %(message)s', level = logging.INFO)
logger = logging.getLogger("CryptoAlgo")

result_run = {}

def run(index):
    timer = Timer()
    timer.start()
    hst_data_formatter = HystoricalDataFormatter()
    candle_numbers = 100
    logger.info(f"Execution[{index}] ---------------- START RUN EXECUTION ---------------- ")

    btc_15m_api = BinanceApi("BTCUSDT", "1m", candle_numbers)

    btc_15m_data = btc_15m_api.get_klines()
    btc_15m_data_formatted = hst_data_formatter.format_klines_request(btc_15m_data)

    markov_implementation = MarkovImplementation(candle_numbers,btc_15m_data_formatted["close_price"].tolist() )
    # Test the function
    result = markov_implementation.fit_transition_matrix()
    markov_implementation.extract_tuples_with_highest_value(1)
    markov_implementation.extract_tuples_with_lowest_value(0)

    result_run[index] = result
    elapsed_time = timer.stop()
    logger.info(f"Execution[{index}] : Time elapsed: {elapsed_time} ---------------- END RUN EXECUTION ---------------- ")

def calculate_state_changes(price_list):
    state_changes = []
    changed_states = []

    for i in range(1, len(price_list)):
        if price_list[i] > price_list[i - 1]:
            state_changes.append(1)
            changed_states.append((price_list[i], 1))
        else:
            state_changes.append(0)
            changed_states.append((price_list[i], 0))

    return state_changes, changed_states
"""
# Esempio di lista di prezzi
price_list = [100, 105, 103, 108, 106, 110, 108, 115, 120, 118]

# Calcola le variazioni di stato e i cambiamenti di stato
state_changes, changed_states = calculate_state_changes(price_list)

# Stampa le variazioni di stato
print("Variazioni di stato:", state_changes)

# Stampa i cambiamenti di stato (prezzo, stato)
print("Cambiamenti di stato:", changed_states)
# Estrai il valore massimo quando lo stato è 1 e il valore minimo quando lo stato è 0
max_state_1 = max([price for price, state in changed_states if state == 1])
min_state_0 = min([price for price, state in changed_states if state == 0])

# Stampa i valori massimo e minimo
print("Valore massimo (stato 1):", max_state_1)
print("Valore minimo (stato 0):", min_state_0)
"""

for i in range(0,3,1):
    run(i)
    time.sleep(59)
