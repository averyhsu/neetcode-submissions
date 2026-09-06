class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #find all zeros,
        #check if the numbers in between each zeroes can jump over zeroes
        # [3,3,3,0,3,2,0,1]
        #start from back. goal = n-1, check n-2 can reach n-1, if yes goal =n-2. The invariant is that if my goal is n-i, n-i can reach the end it can reach either the end or any >n-1 that can reach the end. So if you can't reach goal you can't reach the end
        end = len(nums)-1
        goal = end
        for i in range(end-1,-1,-1):
            
            dist = goal-i
            # print(i, dist, goal)
            if nums[i]>=dist:
                goal = i
                # print("yes")
            
        return goal==0
