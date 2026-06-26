class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while(l<=r):
            mid = (l+r)//2
            if(matrix[mid][0]==target): 
                return True
            elif (matrix[mid][0]>target): 
                r = mid-1
            else :
                l = mid+1
        if r<0 :return False
        L = 0
        R = len(matrix[r])-1
        while(L<=R):
            Mid = (L+R)//2
            if(matrix[r][Mid]==target): 
                return True
            elif (matrix[r][Mid]>target): 
                R= Mid-1
            else :
                L = Mid+1
        return False



