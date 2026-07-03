class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            d = math.sqrt(x*x+y*y)
            heapq.heappush(min_heap,(d, i))
       
        ans = []
        for j in range(k):
            dist, loc = heapq.heappop(min_heap)
            element = points[loc]
            ans.append(element)
        return ans
