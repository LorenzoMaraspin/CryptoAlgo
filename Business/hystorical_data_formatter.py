import logging
import json
import pandas as pd
import numpy as np


logger = logging.getLogger("CryptoAlgo")

class HystoricalDataFormatter():
    def __init__(self):
        pass
    def format_klines_request(self, data):
        print(data)
        df = pd.DataFrame(data, columns = [
              "open_time",
              "open_price",
              "high_price",
              "low_price",
              "close_price",
              "volume",
              "close_time",
              "quote_asset_volume",
              "mumber_of_trades",
              "taker_buy_volume",
              "taker_sell_volume",
              "ignore"
        ])
        df_typed = self.set_dataframe_type(df)
        return df

    def set_dataframe_type(self, df):
        # Set the data type for the "Open" column
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        df["open_price"] = df["open_price"].astype("float")
        df["high_price"] = df["high_price"].astype("float")
        df["low_price"] = df["low_price"].astype("float")
        df["close_price"] = df["close_price"].astype("float")
        df["volume"] = df["volume"].astype("float")
        df["quote_asset_volume"] = df["quote_asset_volume"].astype("float")
        df["mumber_of_trades"] = df["mumber_of_trades"].astype("int")
        df["taker_buy_volume"] = df["taker_buy_volume"].astype("float")
        df["taker_sell_volume"] = df["taker_sell_volume"].astype("float")
        df["ignore"] = df["ignore"].astype("float")

        return df
