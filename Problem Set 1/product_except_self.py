# Product of an array except for itself

# Given an array nums of n integers, where n > 1, return an output array.
# This array, for output[i], should contain the product of all numbers in num except nums[i]
# E.g. nums=[1, 2, 3, 4], position output[0] should be 24 as nums[1:] = 2x3x4
# Make a version that does this by division and another that does not.
from functools import reduce
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Initial simple version. Mulitply all elements in the array conscutively to get the product.
    Then divide that product by each element in the input array to get the result for output[i].

    For multiplying elements of a list consecutively see: https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
    
    O(2n) complexity.
    """
    product = reduce(lambda x, y: x*y, nums)
    output = [int(product / i) for i in nums]
    return output


# Test cases:
print(product_except_self([1, 2, 3, 4])) # Expects: [24, 12, 8, 6]
print(product_except_self([1, 5, 3, 9])) # Expects: [135, 27, 45, 15]
print(product_except_self([-5, 2, -4]))  # Expects: [-8, 20, -10]


def product_except_self2(nums: List[int]) -> List[int]:
    """
    Version without division. There are 3 loops here:
    1. Calculates all the produces left of position i.
    2. Calculates all the produces right of position i.
    3. multiplies left[i] * right[i] for output[i].

    O(3n) complexity.
    """
    length         = len(nums)
    # Predefined empty arrays so we can use indexing
    output         = [None] * length
    left_products  = [None] * length
    right_products = [None] * length

    # first element on left has nothing so value 1, ditto for rightmost element of right
    left_products[0]         = 1
    right_products[length-1] = 1

    # left product
    for i in range(1, length):
        left_products[i] = nums[i-1] * left_products[i-1]

    # right product - moves from r-l
    for i in range(length-2, -1, -1):
        right_products[i] = nums[i+1] * right_products[i+1]
    
    # output
    for i in range(0, length):
        output[i] = left_products[i] * right_products[i]


    return output


# Test cases
print("\nMethod without division:")
print(product_except_self2([1, 2, 3, 4])) # Expects: [24, 12, 8, 6]
print(product_except_self2([1, 5, 3, 9])) # Expects: [135, 27, 45, 15]
print(product_except_self2([-5, 2, -4]))  # Expects: [-8, 20, -10]