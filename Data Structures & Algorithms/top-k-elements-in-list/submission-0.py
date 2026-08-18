class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 

        heap = [] 
        freq = collections.Counter(nums) 

        for ke, v in freq.items():
            heapq.heappush(heap, (-v, ke)) 

        res = []
        while k > 0:
            f, ele = heapq.heappop(heap) 
            res.append(ele) 
            k -= 1 

        return res 