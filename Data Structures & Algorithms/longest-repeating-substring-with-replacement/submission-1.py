class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) 
        maxiFreq = 0 
        mapp = dict() 

        l = r = 0 
        longest = 0 

        while r < n:
            mapp[s[r]] = mapp.get(s[r], 0) + 1 
            maxiFreq = max(mapp.values()) 

            while r - l + 1 - maxiFreq > k:
                mapp[s[l]] -= 1 
                maxiFreq = max(mapp.values()) 
                l += 1 

            longest = max(longest, r - l + 1) 

            r += 1 
            
        return longest 