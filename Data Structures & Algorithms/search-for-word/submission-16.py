class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #stop out at length of Cat
        #at every step compare with word idx
        #if reaches idx of len(word) that means they're equal. Return True
        n = len(word)
        row = len(board)
        col = len(board[0])
        been = [[False for _ in range(col)] for _ in range(row)]
        #only comes in with equal char
        def dfs(idx, r,c):
            
            if idx==n:
                # print("hello")
                return True
            #guard edges
            if r>=row or c>=col or r<0 or c<0:
                return False
            #idx!=n, inside
            # print(been)
            # print(r,c,board[r][c],idx)
            if board[r][c]== word[idx]:
                if been[r][c]:
                    return False
                been[r][c]=True
                top = dfs(idx+1, r+1,c)
                # if r+1<row and c<col and r+1>=0 and c>=0:
                #     been[r+1][c]=False
                bottom =  dfs(idx+1, r-1,c )
                # if r-1<row and c<col and r-1>=0 and c>=0:
                #     been[r-1][c]=False
                right = dfs(idx+1, r,c+1 )
                # if r<row and c+1<col and r>=0 and c+1>=0:
                #     been[r][c+1]=False
                left = dfs(idx+1, r,c-1 )
                # if r<row and c-1<col and r>=0 and c-1>=0:
                #     been[r][c-1]=False
                been[r][c]=False
                return top or bottom or right or left
            else:
                return False
            
        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0]:
                    if dfs(0,r,c):
                        return True
                    been[r][c]=False

        return False

          #0,1,2,3
       #0 #a,b,c,e
       #1 #s,f,e,s
       #2 #a,d,e,e


