# from collections import
class TimeMap:

    def __init__(self):
        self.mapp = dict() 

    def set(self, key: str, value: str, timestamp: int) -> None:
        available = self.mapp.get(key, None) 

        if not available:
            self.mapp[key] = []

        self.mapp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        times_val = self.mapp.get(key, []) 

        n = len(times_val) 
        l = 0 
        r = n - 1 
        ans = ""

        while l <= r:
            mid = l + (r - l // 2) 
            if times_val[mid][0] <= timestamp:
                ans = times_val[mid][1]
                l = mid + 1 

            else:
                r = mid - 1 
        
        return ans 