class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def fun(ind, ds, n, res, nums):
            if ind == n:
                res.append(list(ds))
                return 

            ds.append(nums[ind])
            fun(ind + 1, ds, n, res, nums) 
            ds.pop() 
            fun(ind + 1, ds, n, res, nums)

        ans = [] 
        fun(0, [], len(nums), ans, nums) 
        return ans