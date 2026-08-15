class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":["a","b","c"], "3":["d","e","f"],"4":["g","h","i"], "5":["j","k","l"], "6":          ["m","n","o"],"7":["p","q","r", "s"],"8":["t","u","v"], "9":["w","x","y", "z"]}
        ans = []
        def dfs(idx, cur):
            if idx>=len(digits):
                res = ''.join(cur)
                ans.append(res)
                return
            options = mapping[digits[idx]]
            for char in options:
                cur.append(char)
                dfs(idx+1, cur)
                cur.pop()
        if len(digits)==0:
            return ans
        dfs(0,[])

        return ans