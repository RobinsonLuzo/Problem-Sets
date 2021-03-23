# Decode ways - dynamic programming method:

# A message containing letters A-Z is being encoded to numbers using the following mapping:
# A -> 1
# B -> 2
# ......
# Z -> 26

# Given a non empty string of digits return the number of ways to decode it.
# E.g. "12" should return 2 as there are 2 ways to decode it: "AB" (1, 2) or "L" (12)
# Note: "01" should return 0.

# Look at the last k letters of the msg
def decode_ways(msg: str, k: int, inter_result):
    """
    Returns number of ways last k letters of msg can be decoded. Helper method to num_decodings().
    """
    if k == 0:
        return 1

    start_indx = len(msg) - k
    if msg[start_indx] == "0":     # E.g. "011"
        return 0

    if inter_result[k] != None:
        return inter_result[k]

    result = decode_ways(msg, k - 1, inter_result)
    # If there are at least 2 digits and the 2 retrieved digits are less than 26
    if k >=2 and int(msg[start_indx:start_indx+2]) <= 26:
        result += decode_ways(msg, k - 2, inter_result)

    inter_result[k] = result
    return result


def num_decodings(msg: str):
    """How many ways can a given string be decoded. Returns an integer."""
    intermediate_results = [None] * (len(msg) + 1)
    return decode_ways(msg, len(msg), intermediate_results)


# test cases:
print(num_decodings("12"))  # Expects: 2
print(num_decodings("111")) # Expects: 3