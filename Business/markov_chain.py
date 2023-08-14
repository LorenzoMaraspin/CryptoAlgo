import pandas as pd
import numpy as np
import logging

logger =  logging.getLogger("CryptoAlgo")

class MarkovTheorem():
    def __init__(self):
        pass


    def build_markov_chain(self, len_state):
        #transitions = ['A', 'B', 'B', 'C', 'B', 'A', 'D', 'D', 'A', 'B', 'A', 'D']
        transitions = ['A', 'A', 'B', 'A']

        # convert transition letter in numbers
        T = [self.rank(c) for c in transitions]
        #create matrix of zeros
        M = [[0]*len_state for _ in range(len_state)]

        # create an array of tuple with current value and next value of an array of transition
        obj = list(zip(T,T[1:]))
        print(obj)
        for (i,j) in zip(T,T[1:]):
            M[i][j] += 1

        for row in M:
            # sum values of the same matrix row
            n = sum(row)
            if n > 0:
                row[:] = [f/sum(row) for f in row]

        #print M:

        for row in M:
            print(row)

        return M

    def build_markov_chain_of_coin(self, len_state, transition_matrix, thesold):
        # convert transition letter in numbers
        T = [self.rank_coin_close_price(c, thesold) for c in transition_matrix]
        #create matrix of zeros
        M = [[0]*len_state for _ in range(len_state)]

        # create an array of tuple with current value and next value of an array of transition
        obj = list(zip(T,T[1:]))
        print(obj)
        for (i,j) in zip(T,T[1:]):
            M[i][j] += 1

        for row in M:
            # sum values of the same matrix row
            n = sum(row)
            if n > 0:
                row[:] = [f/sum(row) for f in row]

        #print M:

        for row in M:
            print(row)

        return M

    def rank(self, c):
        return ord(c) - ord('A')

    def rank_coin_close_price(self, coin_price, thesold):
        rank_state = 0
        if coin_price > thesold:
            rank_state = 1
        elif coin_price < thesold:
            rank_state = 0
        else:
            raise("Value error")

        return rank_state

    def rank_coin_close_price_with_len_state(self, coin_price, thesold, len_state):
        state_value_list = []
        for j in range(0, len(coin_price), 1):
            coin_value = coin_price[j]
            for i in range(0, len_state, 1):
                if coin_value > thesold[i]:
                    if coin_value < thesold[i+1]:
                        state_value = i + 1
                        state_value_list.append(state_value)
                        break
                else:
                    state_value = i
                    state_value_list.append(state_value)
                    break
        logger.info(f"StateValueList: {state_value_list}")
        return state_value_list


    def define_state_range(self, support, resistance, range_state):
        state_list = []
        diff_s_r = resistance - support
        range_state_set = diff_s_r / range_state

        for i in range(1,range_state,1):
            range_state_value = support + (range_state_set * i)
            logger.info(f"RangeStateIndex [{i}] - {range_state_value}")
            state_list.append(range_state_value)

        logger.info(f"State list: {state_list}")

        return {"len_state_list":len(state_list), "state_list":state_list}

