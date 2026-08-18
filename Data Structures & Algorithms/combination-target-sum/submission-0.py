class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def fun(ind, tar, ds, nums, n, res):
            if ind == n:
                if tar == 0:
                    res.append(list(ds)) 
                return 

            if nums[ind] <= tar:
                ds.append(nums[ind]) 
                fun(ind, tar - nums[ind], ds, nums, n, res) 
                ds.pop() 

            fun(ind + 1, tar, ds, nums, n, res) 

        ans = [] 
        fun(0, target, [], nums, len(nums), ans) 

        return ans 