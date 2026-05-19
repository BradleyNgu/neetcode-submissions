class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        M = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                M = max(M, profit)
            else:
                left = right
            right += 1
        return M
        