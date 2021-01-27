# Q:1.1 - Tape Equilibrium

# A non empty array A of N integers is given. A position P is given, which splits the array into 2.
# We sum the values on the lest and the values on the right of this divide point P. 
# We then get the absolute difference between the 2 subtracted and move P along another position
# E.g. say A = [3, 1, 2, 4, 3]
# for P = 0, we would like to see the absolute difference between 3 - (1 + 2 + 4 + 3) which = 7
from typing import List

def tape_equilibrium(A: List[int]):
    N = len(A)
    largest_diff = 0

    for splitpoint in range(1, N):
        # abs() result assigned to a variable temporarily for clarity
        absolute_diff = abs(sum(A[:splitpoint]) - sum(A[splitpoint:]))
        if absolute_diff > largest_diff:
            largest_diff = absolute_diff

    return largest_diff


# Test case:
print(tape_equilibrium([3, 1, 2, 4, 3]))       # expects 7
print(tape_equilibrium([3, 10, 6, 4, 8]))      # expects 16
print(tape_equilibrium([13, 7, 5, 21, 19, 2])) # expects 63