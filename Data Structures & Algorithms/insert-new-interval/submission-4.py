class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #non overlapping, no starts & no ends are the same,
        #end must be in ascending order too

        # [-10,0][1,3][4,6][10,15]. [2,9]
        #find smallest end thats bigger than new start
        #find biggest start that's smaller than new end

        #at every interval there are three cases:
        #1, no intersection: 
        #2 new is encapsulated
        #3 new encapsulates 
        #4 intersect left or right
        n = len(intervals)
        i = 0
        ans =[]
        #no overlapps
        # print(intervals[i][1]<newInterval[0])
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            # print(1,i)
            i+=1
        #overlaps starts, as interval end larger than  new interval start
        #new interval eitehr encapsulates or intersect partially
        merge_start = newInterval[0]
        merge_end = newInterval[1]
        while i<n and intervals[i][0]<=newInterval[1]:
            merge_start = min(merge_start,intervals[i][0])
            merge_end = max(merge_end,intervals[i][1])
            # print(merge_start, merge_end)
            i+=1
        ans.append([merge_start, merge_end])
        while i<n:
            ans.append(intervals[i])
            i+=1

        return ans

