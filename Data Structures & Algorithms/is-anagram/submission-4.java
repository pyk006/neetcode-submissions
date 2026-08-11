class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> map = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int j = 0; j < t.length(); j++) {
            map2.put(t.charAt(j), map2.getOrDefault(t.charAt(j), 0) + 1);
        }

        for (Character ch : map.keySet()) {
            if (!map2.containsKey(ch) || map.get(ch) != map2.get(ch)) return false;
        }
        for (Character ch : map2.keySet()) {
            if (!map.containsKey(ch) || map2.get(ch) != map.get(ch)) return false;
        }
        return true;
    }
}
