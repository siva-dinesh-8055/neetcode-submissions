class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums) 

        sett = set(nums) 

        ans = float('-inf')

        for num in nums:
            if num - 1 not in sett:
                lenn = 1 
                start = num 
                while start + 1 in sett:
                    lenn += 1 
                    start += 1 

                ans = max(ans, lenn) 

        return ans if ans != float('-inf') else 0 