class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.ans.add(tuple([]))
        path = []
        self.nums =nums
        self.length = len(nums)
        for i in range(len(nums)):
            self.backtrack(i, path.copy())
        return [list(x) for x in self.ans]
    
    def backtrack(self, idx, path):
        if idx>=self.length: 
            self.ans.add(tuple(path))
            return
        path.append(self.nums[idx])
        self.backtrack(idx+1, path.copy())
        
        path.pop()
        self.backtrack(idx+1, path.copy())
        
        

