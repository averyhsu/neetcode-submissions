class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #                   2,-3,4,-2,2,1,-1,4
       # Left hand sum: 2,-1,3, 1,3,4, 3,7
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = max(cur_sum+i, i) #checks if it's beneficial to drop prev
            max_sum = max(cur_sum, max_sum)

        return max_sum
