from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) 
        l = r = 0 
        mapp = defaultdict(int) 
        longest = 0 

        while r < n:
            mapp[s[r]] += 1 

            while mapp[s[r]] > 1:
                mapp[s[l]] -= 1 
                
                if mapp[s[l]] == 0:
                    mapp.pop(s[l]) 

                l += 1 

            longest = max(longest, r - l + 1) 

            r += 1 

        return longest