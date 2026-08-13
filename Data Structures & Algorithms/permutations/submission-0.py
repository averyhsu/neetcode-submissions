class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = [False]*n
        ans = []
        def dfs(idx, path):
            if idx==n:
                ans.append(path.copy())
                # print(path)
                return
            
            for j in range(n):
                if seen[j]:
                    pass
                else:
                    path.append(nums[j])
                    seen[j] = True
                    print(path)
                    dfs(idx+1,path)
                    path.pop()
                    seen[j]=False

    
        dfs(0,[])
        return ans
