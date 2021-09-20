from collections import Counter
import unittest

# Leetcode 409: Longest Palindrome


def longest_palindrome(s: str) -> int:
    """
    Given a string of both upper and lowercase letters, 
    return the longest case-sensitive palindrome that can be made.

    The trick for this is counting the number of occurences of each character. 
    If the count if even for that char then it can be used. 
    If there is an odd number then we just add 1 to the final result.
    """
    final_count = 0
    odd_is_present = False # flag to indicate if an odd number has occured for final total.
    char_count = Counter(s)

    # check character occurences and add to final total if valid.
    for char in char_count:
        if char_count[char] % 2 == 0:
            final_count += char_count[char]
        else:
            # in case of a character occuring an odd number of times but > 1 add the count but subtract 1 so it is even.
            final_count += (char_count[char] - 1)
            odd_is_present = True

    # If there is at least 1 odd number increment final result by 1
    if odd_is_present == True:
        return final_count + 1
    else:
        return final_count


# Test cases:
class TestLongestPalin(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("abccccdd"), 7)  # Should be: "dccaccd"
        self.assertEqual(longest_palindrome("s"), 1)
        self.assertEqual(longest_palindrome("ccc"), 3)
