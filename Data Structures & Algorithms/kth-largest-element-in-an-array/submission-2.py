class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        count= 0
        for i in nums:
            if count>=k: #heap full
                if min_heap[0] < i:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, i)
            else: #heap empty
                heapq.heappush(min_heap,i)
                count+=1
        return min_heap[0]
