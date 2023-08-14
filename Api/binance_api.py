from binance.spot import Spot
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger("CryptoAlgo")
class BinanceApi:
    def __init__(self, symbol, interval, limit):
        self.symbol = symbol
        self.interval = interval
        self.limit = limit
        self.client = Spot()

    def get_klines(self):
        try:
            coin_klines = self.client.klines(self.symbol, self.interval, limit=self.limit)
        except Exception as err:
            logger.info(err)

        return coin_klines

    def get_current_candle_data(self, symbol, interval, limit):
        try:
            coin_klines = self.client.klines(symbol, interval, limit=limit)
        except Exception as err:
            logger.info(err)

        return coin_klines

    def get_coin_thesold(self, close_price_array):
        sum_coin = 0
        len_coin_price_array = len(close_price_array)
        average_coin = 0

        for i in range(0,len_coin_price_array,1):
            #logger.info(f"CoinArrayIndex[{i}] --> {close_price_array[i]}")
            sum_coin += close_price_array[i]

        average_coin = sum_coin / len_coin_price_array

        logger.info(f"Coin: ({self.symbol}) - Candel timeframe: ({self.interval}) - Candel limit data: ({self.limit}) ----> THESOLD: {average_coin}")

        return average_coin

    def plot_support_resistance(self, df):
        # Calcola i livelli di supporto e resistenza
        support = df["low_price"].rolling(window=50).min()
        resistance = df["high_price"].rolling(window=50).max()

        max_support = support.iloc[-1]
        max_resistance = resistance.iloc[-1]

        return {"support":max_support, "resistance":max_resistance}