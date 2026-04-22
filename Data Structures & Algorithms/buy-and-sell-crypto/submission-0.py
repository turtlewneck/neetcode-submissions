class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        # one stores lowest, second iterates over next values, profit is calculated,
        # if higher, then is set to new value
        # first value does not matter for iteration
        profit = 0
        lowest = prices[0]
        for i in prices[1:]:
            if i < lowest:
                lowest = i
                continue
            curr = i - lowest
            if curr > profit:
                profit = curr
        return profit
            
