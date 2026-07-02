from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = dict() 
        n = len(s1) 
        m = len(s2) 
        l = r = 0 
        c1 = Counter(s1)

        while r < m:

            mapp[s2[r]] = mapp.get(s2[r], 0) + 1 

            while r - l + 1 > n:
                mapp[s2[l]] -= 1 
                if mapp.get(s2[l], 0) == 0:
                    mapp.pop(s2[l]) 

                l += 1 

            if mapp == c1:
                return True 

            r += 1 

        return False 