from Business.hystorical_data_formatter import HystoricalDataFormatter
from Business.markov_theorem import MarkovTheorem
from Api.binance_api import BinanceApi
from Utility.timer import Timer
import pandas as pd
import logging
import time
import schedule

logging.basicConfig(format='%(asctime)s : %(message)s', level = logging.INFO)
logger = logging.getLogger("CryptoAlgo")


class Worker():
    def __init__(self, candles_len, symbol, timeframe):
        self.data_formatter = HystoricalDataFormatter()
        self.coin_api = BinanceApi(symbol, timeframe, candles_len)
        self.candles_len = candles_len
        self.symbol = symbol
        self.timeframe = timeframe

    def init_variables(self):
        logger.info("---------------- VARIABLE INITIALIZATION ---------------- ")
        coin_data = self.data_formatter.format_klines_request(self.coin_api.get_klines()).to_dict(orient='records')

        return coin_data

    def output_history(self, history):
        for item in history:
            for k,v in item.items():
                if k == "candles_data":
                    for i,j in item[k].items():
                        logger.info(f"\t{i}:{j}")
                else:
                    logger.info(f"{k}:{v}")
            logger.info("--------------------------------------")



    def run(self):
        coin_data = self.init_variables()
        markov_theorem = MarkovTheorem(self.candles_len, coin_data)
        history = markov_theorem.check_state_change()

        self.output_history(history)

worker = Worker(50,"BTCUSDT","1m")
worker.run()