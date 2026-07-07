class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) 

        l = 0 
        r = n - 1 
        res = float('inf')

        while l <= r:
            mid = l + (r - l // 2) 

            if nums[mid] < res:
                res = nums[mid] 

            if nums[mid] >= nums[l]:
                res = min(res, nums[l]) 
                l = mid + 1 

            else:
                res = min(res, nums[r]) 
                r = mid - 1 

        return res 