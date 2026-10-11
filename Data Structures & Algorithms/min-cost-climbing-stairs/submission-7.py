class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min cost to get to nth floor of a staircase
        #dp[i] = min(dp[i-1], dp[i-2])
        #base case if i = 0 or i =1  return
        #answer dp(n)
        n = len(cost)
        memo = [-1]*(n+1)

        def dp(i:int):
            if i==0 or i==1:
                return 0
            if memo[i]==-1:
                memo[i] = min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])
            return memo[i]


        return dp(n);