class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) 

        preMini = prices[0] 
        totalProfit = 0 

        for i in range(1, n):
            cost = prices[i] - preMini 
            totalProfit = max(totalProfit, cost) 
            preMini = min(preMini, prices[i]) 

        return totalProfit 