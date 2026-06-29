class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front = [1 for i in range(n)] 

        for i in range(1, n):
            front[i] = nums[i - 1] * front[i - 1] 


        # back = [1 for i in range(n)] 
        post = 1 

        for i in range(n - 1, -1, -1):
            # back[i] = nums[i + 1] * back[i + 1]
            front[i] *= post 
            post *= nums[i]  


        # back = [front[i] * back[i] for i in range(n)] 
        return front 