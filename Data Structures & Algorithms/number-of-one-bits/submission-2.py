class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            count=count+int(n) %2
            n=n/2
        return count