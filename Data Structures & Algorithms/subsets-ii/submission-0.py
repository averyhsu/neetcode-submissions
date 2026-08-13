class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Observation: if I build subset with the same number, they will create identical list of subsets
        #123
        #1,12,13,123
        #2,23
        #3
        
        #121
        #1,12,11,121
        #2,21,
        #1

        #112
        #1,11,12,112
        #2
        n= len(nums)
        ans =[]
        nums.sort()
        def dfs(idx,path):
            if idx==n:
                ans.append(path.copy())
                return
            path.append(nums[idx])
            dfs(idx+1, path)
            path.pop()
            while((idx+1)<n and nums[idx]==nums[idx+1]):
                idx+=1
            dfs(idx+1,path)

        dfs(0,[])
        return ans
