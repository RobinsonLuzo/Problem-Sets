import unittest

# Leetcode: 1678 - Goal parser intepretation
def interpret(command: str) -> str:
    """
    String 'command' consists of 'G', '()' and/or '(al)'.
    These should be intepreted as 'G', 'o' and 'al' respectively.
    Concatenate these in the order supplised with this mapping.
    """
    return command.replace("()", "o").replace("(al)", "al")


# Test case:
class TestInterpret(unittest.TestCase):
    def test_intepret(self):
        self.assertEqual(interpret("G()(al)"), "Goal")