import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for x in stones:
            heapq.heappush(max_heap, -1*x)
        while len(max_heap)>1:
            x=heapq.heappop(max_heap)
            y=heapq.heappop(max_heap)
            d = abs(x-y)
            if d>0:
                heapq.heappush(max_heap, -1*d)
        if len(max_heap)==0: return 0
        else: return -heapq.heappop(max_heap)




