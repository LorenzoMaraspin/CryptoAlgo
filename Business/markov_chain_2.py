import pandas as pd
import numpy as np
import logging

logger =  logging.getLogger("CryptoAlgo")

class MarkovImplementation():
    def __init__(self, len_state: int, list_candle_prices: list):
        self.len_state = len_state
        self.states = [0] * self.len_state
        self.price = [0] * self.len_state
        self.list_candle_prices = list_candle_prices
        self.tuple_checks = []
        self.matrix = [[0 for _ in range(2)] for _ in range(2)]


    def init_matrix_and_lists(self, row):
        matrix = [[0 for _ in range(row)] for _ in range(row)]
        print(matrix)

        return matrix


    def fit_transition_matrix(self):
        check = False
        for i in range(1, self.len_state, 1):
            if self.list_candle_prices[i] > self.list_candle_prices[i-1]:
                check = True
                self.states[i]=1
            else:
                check = False
                self.states[i]=0
            logger.info(f"Array comparison: [{i}]: {self.list_candle_prices[i]} > [{i-1}]: {self.list_candle_prices[i-1]} - outcome: {check}")
            self.price[i] = self.list_candle_prices[i]

            self.check_state_change(i)

        logger.info(f"Tuple of state changes: {self.tuple_checks}")
        logger.info(f"Length of list of tuples: {len(self.tuple_checks)}")
        #self.extract_tuples_with_highest_value(1)
        logger.info(f"MATRIX of OCCURENCES of STATE CHANGE {self.matrix}")
        #self.extract_tuples_with_value(self.tuple_checks, 1)
        #self.extract_tuples_with_value(self.tuple_checks, 0)

        #return {"states":self.states,"price":self.price, "diff_tuple":self.tuple_checks}
        return self.tuple_checks

    def check_state_change(self, i):
        prices = self.price
        states = self.states

        if states[i] != states[i-1]:
            x,y = states[i-1], states[i]
            self.matrix[x][y] += 1
        self.tuple_checks.append((states[i], float(prices[i])))

        #[(states[i], prices[i]) for i in range(1, len(prices)) if states[i] != states[i - 1]]

    def extract_tuples_with_value(self, arr, value):
        result = [item for item in arr if item[0] == value]
        print(result)

        return result

    def extract_tuples_with_highest_value(self, value):
        filtered_data = [(int(val[0]), float(val[1])) for val in self.tuple_checks if val[0] == value]
        tuple_with_highest_number = max(filtered_data, key=lambda x: x[1])

        logger.info(f"HIGH: {value} - {tuple_with_highest_number}")
    def extract_tuples_with_lowest_value(self, value):
        filtered_data = [(int(val[0]), float(val[1])) for val in self.tuple_checks if val[0] == value]
        tuple_with_lowest_number = min(filtered_data, key=lambda x: x[1])

        logger.info(f"LOW: {value} - {tuple_with_lowest_number}")