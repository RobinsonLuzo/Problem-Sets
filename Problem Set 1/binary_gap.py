# Binary Gap

# A positive integer N - count the consecutive 0s between 1s that appear in the binary representation of a number N
# E.g. 1041 would return 5 as its binary representation is 10000010001. 32 returns 0 as its representation is
# 100000 - no 1 at the other end. 
# 9 is 1001 so it would return 2
import re

def solution(n):
    """Presumes n is > 1"""
    max_count = 0
    bytes_rep = str(bin(n))[2:]

    try:
        # find all occurences between 1s, put into a list then return the max value of list of strings
        splits = re.findall("(?=1(.*?)1)", bytes_rep)
        return len(max(splits, key=len))
    except:
        return 0


print(solution(1041)) # Expect 5 - 10000010001.
print(solution(9))    # Expect 2
print(solution(32))   # Expect 0