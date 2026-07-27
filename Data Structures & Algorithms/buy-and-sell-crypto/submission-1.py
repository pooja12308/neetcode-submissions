class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB=prices[0]
        maxP=0
        for i in prices:
            maxP=max(maxP,i-minB)
            minB=min(minB,i)
        return maxP
        