class Solution {
    public int maxProfit(int[] prices) {
        int current = 0;
        int max_profit = Integer.MIN_VALUE;
        while (current < prices.length - 1) {
            for (int next = current + 1; next < prices.length; next++) {
                int difference = prices[next] - prices[current];
                max_profit = Math.max(difference, max_profit);
            }
            current++;
        }
        return max_profit < 0 ? 0 : max_profit;
    }
}
