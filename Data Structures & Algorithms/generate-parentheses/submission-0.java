class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<>();
        backtrack("", 0, 0, list, n);
        return list;
    }
    public void backtrack(String current, int open, int close, List<String> list, int n) {
        if (current.length() == n * 2) {
            list.add(current);
            return;
        }
        if (open < n) {
            backtrack(current + "(", open + 1, close, list, n);
        }
        if (close < open) {
            backtrack(current + ")", open, close + 1, list, n);
        }
    }
}
