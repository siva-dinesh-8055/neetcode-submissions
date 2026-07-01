class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        l, r = 0, n - 1 
        lmax = float('-inf') 
        rmax = float('-inf') 
        res = 0 
        while l < r:
            lmax = max(lmax, height[l]) 
            rmax = max(rmax, height[r]) 
            if lmax < rmax:
                res += lmax - height[l] 
                l += 1 

            else:
                res += rmax - height[r] 
                r -= 1 

        return res 