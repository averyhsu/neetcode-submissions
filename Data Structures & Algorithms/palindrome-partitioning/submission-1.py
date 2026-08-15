class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(str, l, r):
            if l>=r:
                return True
            if str[l]==str[r]:
                return is_pal(str, l+1, r-1)
            else:
                return False
        
        ans = []
        def dfs(l,r, cur):
            #at the end:
            if r>=len(s):
                return
            #is a palindrone
            if is_pal(s,l,r):
               
                #take right now as substring, start at next
                cur.append(s[l:r+1])
                if r ==len(s)-1:
                    ans.append(cur.copy())
                    cur.pop()
                    return
                new_l = r+1
                new_r = new_l
                dfs(new_l, new_r, cur)
                cur.pop()
                dfs(l, r+1,cur)
            else:
                dfs(l, r+1,cur)


        dfs(0,0,[])
        return ans
