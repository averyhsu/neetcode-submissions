class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = 0
        closed = 0
        ans = []
        #if close = n: append to solution then return
        #else < n:
            #if opene=0: can only open
            #elif open =n: can only close:
            #else: backtrack open or close

        def dfs(opened, closed, string):
            if closed ==n:
                ans.append(string)
                return
            if opened ==n:
                string+=')'
                dfs(opened,closed+1, string)
            else:
                diff = opened-closed #how many oepn parathensis
                #can only open
                if diff ==0:
                    string+='('
                    dfs(opened+1,closed, string)
                #diff positive: more open than close
                else:
                    string+='('
                    dfs(opened+1,closed, string)
                    string = string[:-1]
                    string+=')'
                    dfs(opened,closed+1, string)

        dfs(0,0,"")
        return ans
            # if opened ==0:
            #     string+='('
            #     dfs(opened+1,closed, string)
            # elif opened==n:
            #     string+=
