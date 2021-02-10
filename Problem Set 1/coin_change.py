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


# Dynamic programming method:

# Doesn't always find the optimum amount though. 
# For that we have to create a change matrix and use dynamic programming (i.e. using 'helper' methods).
# E.g. for [1, 5, 10] coin matrix will be:

#    0 |  1   2   3 ...9    10
#    --------------------------
#    1 |  1   2   3    9    10
#    5 |  0   0   0    1    2
#    10|  0   0   0    0    1

def _change_matrix(coin_set, change_amt):
    """
    Hidden helper function to generate a coin matrix for a given set of coins to a given amount of change. 

    Matrix will consist of: row length (columns) determined by change amount + 1
    Rows set by length of coin set + 1.
    """
    # Remember: range() doesn't take last value so add + 1
    matrix = [[0 for m in range(change_amt+1)] for m in range(len(coin_set)+1)]

    # Fill in first row of matrix:
    for i in range(change_amt + 1):
        matrix[0][i] = i
    
    return matrix


def dynamic_change_making(coins, change):
    """
    Dynamic method of finding the minimum number of coins to make a given amount of change.

    Returns minimum amount of coins required from given to set to make change amount.
    """
    matrix = _change_matrix(coins, change)

    # Remember: coins indexing starts at 0, while the other starts at 1
    for c in range(1, len(coins)+1):
        for r in range(1, change + 1):
            
            # If coin is equal to the value at r then it goes in just once
            if coins[c-1] == r:
                matrix[c][r] = 1

            # If the coin value is greater than the value that we need at the current spot in the matrix
            # then take previous position and set the current to be equal to it.
            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            # else the matrix at this position will be equal to whichever is smaller:
            # previous position or matrix in same row but previous position within that matrix
            else:
                matrix[c][r] = min(matrix[c-1][r], 1 + matrix[c][r - coins[c-1]])

    return matrix[-1][-1]


# Test cases:
# Variables passed: change set, value we're trying to get to
print("\nDynamic method:")
# Using greedy method the below example would have used 25, then 1 to return 8.
# Best method would be to use 3 10s and 2 1s for a total of 5.
print(dynamic_change_making([1, 10, 25], 32)) # Expects 5 -> 3x10, 2x1

print(dynamic_change_making([1, 10, 25], 72)) # Expects 6 -> 2x25, 2x10, 2x1
print(dynamic_change_making([1, 10, 25], 17)) # Expects 8 -> 1x10, 7x1