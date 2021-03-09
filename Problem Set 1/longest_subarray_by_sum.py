# Find the longest sub-array by sum

# We get an array of numbers and a value s.
# We want to find the longest section of array where the sum is equal to the value s. 
# We should return the places in the array between which this subarray exists. 
# Or -1 if the subarray does not exist in the prodived arr.

# E.g. for array [1, 2, 3, 7, 5] we should expect [2, 4] as 2 + 3 + 7 = 12.
# 7 + 5 also = 12, but is shorter.

def find_longest_subarray_by_sum(arr, s):
    """
    Takes in:
    - arr: an array of integers
    - s: an int target we want the subarray to sum to.

    Uses 2 pointers starting from left. Iterates over list until s is met or exceeded.
    When it is, it subtracts the left value from the current total and moves that 'window'
    one position to the right. Updates return values as it find a position longer than the previous held.
    """
    result = [-1]
    total_sum = 0
    left = 0
    right = 0

    # As the right pointer will reach the end first we use that in the condition
    while right < len(arr):
        total_sum += arr[right]
        while left < right and total_sum > s:
            total_sum -= arr[left]
            left += 1
        
        if total_sum == s and (len(result) == 1 or result[1] - result[0] < right - left):
            result = [left+1, right+1]

        right += 1

    return result



# Test cases:
print(find_longest_subarray_by_sum([1, 2, 3, 7, 5], 12))                          # Expects: 2, 4
print(find_longest_subarray_by_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))          # Expects: 1, 5
print(find_longest_subarray_by_sum([1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], 15)) # Expects: 1, 8