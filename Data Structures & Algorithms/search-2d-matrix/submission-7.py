class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        n = len(matrix[0])
        r = len(matrix)*n-1
        while(l<=r):
            mid = (l+r)//2
            x=mid//n
            y = mid%n
            if(matrix[x][y]==target): return True
            elif(matrix[x][y]>target) : r= mid-1
            else : l = mid+1

        return False



