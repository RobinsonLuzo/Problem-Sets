from typing import List
import unittest

# Leetcode 1436: Destination City
def dest_city(paths: List[List[str]]) -> str:
    """
    Given an array 'paths', where paths[i] = [cityA, cityB] and means there is a direct path between the 2.
    Return the destination city - meaning the city without any paths outbound ot another city.

    For this we need to unpack the city paths. Then add the cities to a dict. 
    A city that has a destination but also origin point will usually be set to 0 first then 1,
    meaning any city with a count of 0 is the destination that does not appear to go elsewhere.
    """
    outgoing_count = {}
    for path in paths:
        city_a, city_b = path
        outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
        outgoing_count[city_b] = outgoing_count.get(city_b, 0)

    for city in outgoing_count:
        if outgoing_count[city] == 0:
            return city


def dest_city_alt(paths: List[List[str]]) -> str:
    """
    Alternative version using unzipping and sets.
    """
    A, B = map(set, zip(*paths))
    return (B-A).pop()


# Test cases:
class TestDestCity(unittest.TestCase):
    def test_dest_city(self):
        self.assertEqual(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]), "Sao Paulo")
        self.assertEqual(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]), "A")

    def test_dest_city_alt(self):
        self.assertEqual(dest_city_alt([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]), "Sao Paulo")
        self.assertEqual(dest_city_alt([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
