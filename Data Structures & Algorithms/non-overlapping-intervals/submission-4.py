class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #   12 14 24 
        intervals.sort()
        best_end = intervals[0][1]
        ans = 0
        for interval in intervals[1:]:
            # overlap
            if interval[0]<best_end:
                best_end = min(best_end, interval[1])
                ans+=1
                # print(interval)
            else:
                best_end = interval[1]
            # print(best_end)
        
        return ans
            
            #no overlap


