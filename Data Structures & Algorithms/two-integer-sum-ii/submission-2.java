class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;

        while (start < end) {
            if (start > 0 && numbers[start] == numbers[start - 1]) {
                start++;
            } else if (end < numbers.length - 1 && numbers[end] == numbers[end + 1]) {
                end--;
            } else {
                if (numbers[start] + numbers[end] == target) {
                    return new int[]{start + 1, end + 1};
                } else if (numbers[start] + numbers[end] > target) {
                    end--;
                } else {
                    start++;
                }                
            }
        }
        return new int[]{-1, -1};
    }
}
