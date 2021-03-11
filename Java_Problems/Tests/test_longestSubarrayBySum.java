package Java_Problems.Tests;

import Java_Problems.Problems.findLongestSubarrayByS;

import org.junit.Assert;
import org.junit.Test;


public class test_longestSubarrayBySum {

    @Test
    public void testlongestSubarrayBySum() {
        int[] testArray = {1, 2, 3, 7, 5};
        int s = 12;
        int[] result = {2, 4};
        Assert.assertArrayEquals(result, findLongestSubarrayByS.findLongestSubarrayBySum(s, testArray));

        int[] testArray2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int s2 = 15;
        int[] result2 = {1, 5};
        Assert.assertArrayEquals(result2, findLongestSubarrayByS.findLongestSubarrayBySum(s2, testArray2));

        int[] testArray3 = {1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10};
        int[] result3 = {1, 8};
        Assert.assertArrayEquals(result3, findLongestSubarrayByS.findLongestSubarrayBySum(s2, testArray3));
    }
    
}
