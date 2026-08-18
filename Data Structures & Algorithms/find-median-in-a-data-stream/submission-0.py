class MedianFinder:

    def __init__(self):
        self.left = [] 
        self.right = [] 
        # n = len(arr)
        # res = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num) 
            
        heapq.heappush(self.right, -heapq.heappop(self.left)) 
        
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right)) 

    def findMedian(self) -> float:
        if len(self.left) != len(self.right):
            res = float(-self.left[0]) 
            
        else:
            res = (-self.left[0] + self.right[0]) / 2.0 

        return res 