import pandas as pd
import numpy as np
import logging

logger =  logging.getLogger("CryptoAlgo")

class MarkovTheorem():
    def __init__(self):
        pass


    def build_markov_chain(candlestick_data, num_states=10):
        """
        Builds a Markov chain from the closing prices of candlestick data.

        Parameters:
            candlestick_data (pd.DataFrame): A DataFrame containing candlestick data, with the 'Close' column representing the closing prices.
            num_states (int): Number of discrete states to use for the Markov chain.

        Returns:
            transition_matrix (np.ndarray): The transition matrix representing the Markov chain.
        """
        # Calculate the range of closing prices to determine the state intervals
        min_price, max_price = candlestick_data['close'].min(), candlestick_data['close'].max()
        price_range = max_price - min_price
        state_interval = price_range / num_states

        # Assign each closing price to a state
        candlestick_data['State'] = ((candlestick_data['Close'] - min_price) // state_interval).astype(int)

        # Initialize the transition matrix
        transition_matrix = np.zeros((num_states, num_states))

        # Count the transitions between states
        for i in range(len(candlestick_data) - 1):
            current_state = candlestick_data.at[i, 'State']
            next_state = candlestick_data.at[i + 1, 'State']
            transition_matrix[current_state, next_state] += 1

        # Normalize the transition matrix to get probabilities
        row_sums = transition_matrix.sum(axis=1, keepdims=True)
        transition_matrix = transition_matrix / row_sums

        return transition_matrix
