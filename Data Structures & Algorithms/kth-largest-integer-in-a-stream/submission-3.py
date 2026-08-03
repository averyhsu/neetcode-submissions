class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = [-x for x in nums]
        heapq.heapify(nums)
        self.top_k = []
        for i in range(min(k, len(nums))):
            self.top_k.append(-1*heapq.heappop(nums))
        #min heap of top k element
        heapq.heapify(self.top_k)

    def add(self, val: int) -> int:
        if (len(self.top_k)<self.k):
            heapq.heappush(self.top_k, val)
        elif val>self.top_k[0]:#top k
            heapq.heapreplace(self.top_k, val)
        return self.top_k[0]

