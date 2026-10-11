class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max amount of money I can rob from i to n houses
        #max(cur+dp[i+2], dp[i+1])
        n = len(nums)
        memo = [-1]*n
        def dp(i):
            if i>=n:
                return 0
            if memo[i]==-1:
                memo[i]= max(nums[i]+dp(i+2), dp(i+1))
            return memo[i]
        return dp(0)