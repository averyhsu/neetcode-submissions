class Solution:
    def findMin(self, nums: List[int]) -> int:
        #l, m, r: case on them, 5 cases:
        #1,2,3,4
        #l<m<r: return l
        #2,3,4,1.   3,4,1,2
        #r<l<m: l=m, r=r
        #4,1,2,3
        #m<r<l: l =l, r = m
        l = 0
        r = len(nums)-1
        count=0
        while True:
            count+=1
            m = (l+r)//2
            if nums[l]<=nums[m]<=nums[r]:
                return nums[l]
            if nums[r]<=nums[l]<=nums[m]:
                l = m+1
            if nums[m]<=nums[r]<=nums[l]:
                r = m
            print(l,m,r)

        # lmr
        # rlm
        # mrl

        #lrm not possible
        # rml not possible for middle to smaller than left 
        # mlr not possible for ordered