"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort
        #convert start/end to open/close parenthesis
        #count max open parenthesis
        # intervals.sort(key = lambda x :x.start)
        start = []
        end = []
        for x in intervals:
            start.append(x.start)
            end.append(x.end)
        start.sort()
        end.sort()
        start_ptr=0
        end_ptr = 0
        count = 0
        ans = 0
        while start_ptr <len(start):
            #strictly less: overlapps don't count
            if start[start_ptr]<end[end_ptr]:
                count+=1
                start_ptr+=1
            else:
                count-=1
                end_ptr+=1
            ans = max(ans, count)

        #0,5,15
        #10,20,40
        return ans