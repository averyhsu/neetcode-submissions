class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        # seen = set()
        def dfs(idx, path, total):
            # print(idx,path, total)
            if total>target:
                return
            if idx ==n:
                if total == target:
                    copy = path.copy()
                    ans.append(copy)
                    # print(ans)
                return
            #take
            path.append(candidates[idx])
            dfs(idx+1,path, total+candidates[idx])
            path.pop()
            cur = candidates[idx]
            while idx<n and candidates[idx]== cur :
                idx+=1
            dfs(idx,path, total)

        dfs(0,[],0)
        return ans


           