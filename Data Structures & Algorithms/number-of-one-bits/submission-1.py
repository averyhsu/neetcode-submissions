class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            if int(n) %2  ==1:
                count=count+1
            n=n/2
        return count