import pandas as pd
import numpy as np
import logging

logger =  logging.getLogger("CryptoAlgo")


class MarkovTheorem():
    def __init__(self, candles_len, candles_data):
        self.candles_len = candles_len
        self.candles_data = candles_data
        self.min_price = self.candles_data[-1]['close_price']
        self.max_price = self.candles_data[-1]['close_price']
        self.resistances = []
        self.supports = []
        self.states = [0] * self.candles_len
        self.price = [0] * self.candles_len
        self.transitions = [[0 for _ in range(2)] for _ in range(2)]

    def shift_array(self, new_item):
        array = self.candles_data
        array.pop(0)
        array.append(new_item)

        return array

    def check_state_change(self):
        history_list = []
        history = {}

        for index in range(1,self.candles_len, 1):
            item = self.candles_data[index]
            logger.info(f"item[{index}] - close_price: {item['close_price']} close_time: {item['close_time']}")

            if self.candles_data[index]['close_price'] < self.candles_data[index-1]['close_price']:
                self.states[index] = 1
            else:
                self.states[index] = 0

            if self.states[index] != self.states[index-1]:
                current_transition = self.transitions[self.states[index]][self.states[index-1]]
                self.transitions[self.states[index]][self.states[index-1]] = current_transition + 1
                if self.states[index-1] == 0 and self.candles_data[index-1]['close_price'] < self.min_price:
                    self.min_price = self.candles_data[index-1]['close_price']
                    history = {"price_towards":"MIN", "candles_data":self.candles_data[index-1], "price":self.min_price}
                    self.supports.append(self.min_price)
                if self.states[index-1] == 1 and self.candles_data[index-1]['close_price'] > self.max_price:
                    self.max_price = self.candles_data[index-1]['close_price']
                    history = {"price_towards":"MAX", "candles_data":self.candles_data[index-1], "price":self.max_price}
                    self.resistances.append(self.max_price)
            history_list.append(history)
        history["supports"] = self.supports
        history["resistances"] = self.resistances

        return history_list