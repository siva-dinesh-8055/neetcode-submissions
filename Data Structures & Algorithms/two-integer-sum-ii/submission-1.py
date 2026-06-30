class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0 
        r = n - 1 

        while l < r:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1] 

            elif nums[l] + nums[r] > target:
                r -= 1 

            else:
                l += 1 
