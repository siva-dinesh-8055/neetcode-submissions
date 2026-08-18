class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq, math 
        heap = [] 

        for x2, y2 in points:
            dis = math.sqrt((0 - x2) ** 2 + (0 - y2) ** 2) 

            heapq.heappush(heap, (-dis, [x2, y2])) 

            if len(heap) > k:
                heapq.heappop(heap) 

        res = [] 
        while heap:
            dis, pair = heapq.heappop(heap) 
            res.append(pair) 

        return res 