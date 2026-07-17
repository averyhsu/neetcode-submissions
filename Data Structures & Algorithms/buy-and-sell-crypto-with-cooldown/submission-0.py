class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][x]: max profit day i to end, with x (0 or 1) coin currently
        #if i==0: return 0
        end = len(prices)-1
        # no coins
        #if x ==0: max(dp[i-1][1], dp[i-1][0] : buy or not buy
        #has coins
        #if x==1: max(sell+dp[i-2][0], dp[i-1][1])
        memo = {}
        def dp(i, x):
            if i>end:
                return 0
            if (i,x) in memo:
                return memo[(i,x)]
            if x==0:
                memo[(i,x)]=max(-prices[i]+dp(i+1,1), dp(i+1,0))
            if x==1:
                memo[(i,x)]=max(prices[i]+dp(i+2,0), dp(i+1,1))
            return memo[(i,x)]
        return dp(0,0)
