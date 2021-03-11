package Java_Problems.Problems;

public class findLongestSubarrayByS {
    
    public static int[] findLongestSubarrayBySum(int s, int[] arr) {
        int result[] = new int[]{-1};
        int total_sum = 0;
        int left = 0;
        int right = 0;

        while (right < arr.length) {
            total_sum += arr[right];
            while (left < right && total_sum > s) {
                total_sum -= arr[left++];
            }
            if (total_sum == s && (result.length == 1 || result[1] - result[0] < right - left)) {
                result = new int[] {left + 1, right + 1};
            }

            right++;
        }
        return result;
    }

}
