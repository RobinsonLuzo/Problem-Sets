from typing import List
import unittest

# Leetcode 1365: How many numbers are smaller than the current one in an array?
def smaller_than_current_num(nums:List[int]) -> List[int]:
    """
    Given an array of numbers, find for each position how many items in the array are smaller than it.

    For this: first create a sorted copy of the numbers. Then we go through these.

    By dint of being sorted smallest to largest, the index position will indicate 
    how many items are smaller than the number at the current index position.

    We do not specify an update for those already in the data dictionary as duplicates are not smaller.
    """
    sorted_nums = sorted(nums)
    data_dict = {}
    result = []

    for i in range(len(sorted_nums)):
        if sorted_nums[i] not in data_dict:
            data_dict[sorted_nums[i]] = i

    # now assign data in data dict to empty list
    for i in nums:
        result.append(data_dict[i])

    return result


# Test cases:
class TestSmallerThan(unittest.TestCase):
    def test_smaller_than(self):
        self.assertEqual(smaller_than_current_num([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])
        self.assertEqual(smaller_than_current_num([6, 5, 4, 8]), [2, 1, 0, 3])
        self.assertEqual(smaller_than_current_num([7, 7, 7, 7]), [0, 0, 0, 0])
