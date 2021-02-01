# Sorted squared array

# Given a sorted array of integers, return a sorted array of the squared values of those integers.
# E.g. arr=[1, 2, 3, 4], output=[1, 4, 9, 16] 
# NOTE: elements can be negative: -10,000 <= i <= 10,000
from typing import List

def sort_squared_array(arr: List[int]):
    """
    Iterates a given sorted array from right to left. 
    Compares the absolute values of leftmost and rightmost elements in the array. 
    
    If the leftmost is bigger absolutely then it will result in a larger number when squared.
    So we square it and put it at the end of our output array. Else put the rightmost. 
    
    Whichever value was not bigger will remain at
    the same index position while the other moves 1 step toward the centre of the array.
    """
    length  = len(arr)
    # Predefined empty arrays so we can use indexing
    output  = [None] * length
    left = 0
    right = length -1

    # Move in -1 decrements
    for i in range(length-1, -1, -1):
        if abs(arr[left]) > abs(arr[right]):
            output[i] = arr[left] * arr[left]
            left += 1
        else:
            output[i] = arr[right] * arr[right]
            right -= 1
    return output

print(sort_squared_array([1, 2, 3, 4]))           # Expects: [1, 4, 9, 16] 
print(sort_squared_array([-3, -2, -1]))           # Expects: [1, 4, 9] 

