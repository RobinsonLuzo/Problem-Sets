# Change making problem

# Given a list of change, write an function that returns an array of the optimum amount of coins to make 
# a given amount of change
# E.g. using [1, 5, 10, 25] to make 12 the result should be 3 coins: 1, 1, 10

# Greedy method: highest coin values first and see if that goes into the change, moving succesively down.

def greedy_coin_change(change):
    """
    Greedy method of change making. 
    Given change take the highest value coins first and see if the coin goes into the change.
    When it doesn't move down a coin position.

    Return the minimum number of coins needed to make the given change.
    """
    coins = [25, 10, 5, 1]
    count = 0

    for coin in coins:
        while change >= coin:
            change = change - coin
            count += 1

    return count


# Test cases
print(greedy_coin_change(8))   # Expects: 4
print(greedy_coin_change(25))  # Expects: 1
print(greedy_coin_change(12))  # Expects: 3
print(greedy_coin_change(100)) # Expects: 4