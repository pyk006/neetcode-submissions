class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, nums, new ArrayList<>(), 0, target, 0);
        return list;
    }

    public void backtrack(List<List<Integer>> list, int[] vals, List<Integer> currentList, int currentTotal, int target, int start) {
        if (currentTotal == target) {
            list.add(new ArrayList<>(currentList));
            return;
        }
        for (int i = start; i < vals.length; i++) {
            if (vals[i] + currentTotal > target) {
                continue;
            }
            currentList.add(vals[i]);
            backtrack(list, vals, currentList, currentTotal + vals[i], target, i);
            currentList.remove(currentList.size() - 1);
        }

    }
}
