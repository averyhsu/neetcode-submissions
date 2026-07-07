class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #cases:
        #1. take cur
        #2. don't take and stay
        #3. don't take and move
        self.target = target
        self.ans = []
        path = []
        self.nums =nums
        self.length = len(nums)
        self.backtrack(0, path.copy())
        return self.ans
    def backtrack(self, idx, path):
        #remove when overshoot
        cur_sum = sum(path)
        if cur_sum>self.target:
            return
        #sum less than target
        if idx>=(self.length): 
            if cur_sum==self.target:
                self.ans.append(path)
            return
        #take cur and stay
        path.append(self.nums[idx])
        self.backtrack(idx, path.copy())
  
        #don't take and move
        path.pop()
        self.backtrack(idx+1, path.copy())
       

        
        



