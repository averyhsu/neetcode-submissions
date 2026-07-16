class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows, n = columns
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # first is row(m), second is colums(n)
        for x in range(n):
            dp[0][x]=1
        for i in range(n):
            for j in range(1,m):
                if i==0: 
                    print("hi")
                    dp[j][i]=1
                else: 
                    dp[j][i]=dp[j-1][i]+dp[j][i-1]
                print(j,i)
                print(dp[j][i])

        return dp[m-1][n-1]