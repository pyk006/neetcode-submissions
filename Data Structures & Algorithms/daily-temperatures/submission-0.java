class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        for (int current = 0; current < temperatures.length; current++) {
            int next = current + 1;
            while (next < temperatures.length) {
                if (temperatures[current] < temperatures[next]) {
                    result[current] = next - current;
                    break;
                }
                next++;
            }
        }
        return result;
    }
}
