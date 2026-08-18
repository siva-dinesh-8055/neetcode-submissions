class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [] 

        def fun(ind, res, nums, n):
            if ind == n:
                res.append(list(nums)) 
                return 

            for i in range(ind, n):
                nums[ind], nums[i] = nums[i], nums[ind] 
                fun(ind + 1, res, nums, n)
                nums[ind], nums[i] = nums[i], nums[ind] 

        fun(0, ans, nums, len(nums)) 

        return ans