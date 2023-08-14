import logging
import json
import pandas as pd
import numpy as np


logger = logging.getLogger("CryptoAlgo")

class HystoricalDataFormatter():
    def __init__(self):
        pass
    def format_klines_request(self, data):
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
        df["open_price"] = df["open_price"].astype("float").map('{:,.4f}'.format)
        df["high_price"] = df["high_price"].astype("float").map('{:,.4f}'.format)
        df["low_price"] = df["low_price"].astype("float").map('{:,.4f}'.format)
        df["close_price"] = df["close_price"].astype("float")
        df["volume"] = df["volume"].astype("float").map('{:,.4f}'.format)
        df["quote_asset_volume"] = df["quote_asset_volume"].astype("float").map('{:,.4f}'.format)
        df["mumber_of_trades"] = df["mumber_of_trades"].astype("int").map('{:,.4f}'.format)
        df["taker_buy_volume"] = df["taker_buy_volume"].astype("float").map('{:,.4f}'.format)
        df["taker_sell_volume"] = df["taker_sell_volume"].astype("float").map('{:,.4f}'.format)
        df["ignore"] = df["ignore"].astype("float").map('{:,.4f}'.format)

        return df
