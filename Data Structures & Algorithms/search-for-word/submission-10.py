class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #stop out at length of Cat
        #at every step compare with word idx
        #if reaches idx of len(word) that means they're equal. Return True
        n = len(word)
        row = len(board)
        col = len(board[0])
        been = set()
        #only comes in with equal char
        def dfs(idx, r,c,been):

            if idx==n:
                return True
            #guard edges
            if r>=row or c>=col or r<0 or c<0:
                return False
            #idx!=n, inside
            print(r,c,board[r][c], idx)

            if board[r][c]== word[idx]:
                if (r,c) in been:
                    return False
                been.add((r,c))
                return dfs(idx+1, r+1,c,been.copy()) or dfs(idx+1, r-1,c,been.copy()) or dfs(idx+1, r,c+1,been.copy())or dfs(idx+1, r,c-1,been.copy())
            else:
                return False
            
        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0]:
                    been = set()
                    if dfs(0,r,c, been):
                        return True

        return False

          #0,1,2,3
       #0 #a,b,c,e
       #1 #s,f,e,s
       #2 #a,d,e,e


