class Solution {
    public int lengthOfLongestSubstring(String s) {
       int longest = Integer.MIN_VALUE;
       Set<Character> set = new HashSet<>();
       int left = 0;
       for (int right = 0; right < s.length(); right++) {
        char currentch = s.charAt(right);
            while (set.contains(currentch)) {
                set.remove(s.charAt(left));
                left++;
            }
            longest = Math.max(longest, right - left + 1);
            set.add(currentch);
       }
       return longest == Integer.MIN_VALUE ? 0 : longest; 
    }
}
