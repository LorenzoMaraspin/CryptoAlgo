from Api.binance_api import BinanceApi
from Business.hystorical_data_formatter import HystoricalDataFormatter
import logging

logger = logging.basicConfig(format='%(asctime)s : %(message)s', level = logging.INFO)

binance_api = BinanceApi("BTCUSDT", "1m", 50)
hst_data_formatter = HystoricalDataFormatter()

btc_data = binance_api.get_klines()

btc_data_formatted = hst_data_formatter.format_klines_request(btc_data)

binance_api.get_coin_thesold(btc_data_formatted["close_price"].tolist())