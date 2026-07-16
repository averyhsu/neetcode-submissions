class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        
        #DP[x][y] = longest subsequence from text x to end & y to end
            #if one[x] ==two[y]: max (1+dp[x+1][y+1], dp[x][y+1], dp[x+1][y])
            #if one[x]!=two[y]: max(dp[x+1][y+1], dp[x][y+1], dp[x+1][y])
        memo={}#dictionary
        def dp(x, y):
            if x>=len1 or y>= len2:
                return 0
            if (x,y) in memo: return memo[(x,y)]
            if text1[x]==text2[y]: 
                memo[(x,y)] = (1+dp(x+1,y+1))
            else:
                memo[(x,y)] = max (dp(x,y+1), dp(x+1,y))
            return memo[(x,y)]
        return dp(0,0)
        #brute force, one ptr stays & match with the whole of other word, repeat till end
        #fuckallow
        #flpallow