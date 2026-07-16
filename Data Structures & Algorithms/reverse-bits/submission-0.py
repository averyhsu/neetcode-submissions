class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        for i in range(31, -1, -1):
            mult = 2**i
            cur = n%2
            ans = ans+mult*cur
            n = int(n/2)
        return ans