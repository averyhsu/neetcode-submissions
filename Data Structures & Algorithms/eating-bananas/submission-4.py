class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sol_min = float('inf')
        maxi = max(piles) #max speed
        mini = math.ceil(sum(piles)/h) #min speed
        # nums = list(range(mini, maxi + 1))
     
        while(mini<=maxi):
            mid = (maxi+mini)//2
            # total = sum(x / k for x in nums)
            if(sum(math.ceil(x/mid) for x in piles)<=h): 
                sol_min = min(mid, sol_min)
                maxi = mid-1
            else :
                mini = mid+1
        return sol_min