class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculatehours(arr, k):
            ans = 0 
            for i in range(len(arr)):
                ans += math.ceil(arr[i]/k)
            return ans 
        l = 1 
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2 
            time_taken = calculatehours(piles, mid)
            if time_taken <= h:
                r = mid - 1 
            else:
                l = mid + 1 
        return l 
