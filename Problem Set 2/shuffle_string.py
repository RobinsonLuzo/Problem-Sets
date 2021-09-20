from typing import List
import unittest

def restore_string(s: str, indicies: List[int]) -> str:
    """
    Given a string s and indicies, shuffle the string until the indicies 
    (and thus characters) are ordered correctly by index. I.e from smallest to biggest number.
    """
    answer = ""

    for i in range(len(indicies)):
        answer += s[indicies.index(i)]
        print(indicies.index(i), indicies[i])
    
    return answer


class TestShuffle(unittest.TestCase):
    def test_restore_string(self):
        self.assertEqual(restore_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")