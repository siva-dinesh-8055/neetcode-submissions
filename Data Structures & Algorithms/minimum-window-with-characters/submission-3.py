class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s) 
        m = len(t) 
        mapp = dict() 

        for ch in t:
            mapp[ch] = mapp.get(ch, 0) + 1 

        l = r = 0 
        c = 0 
        minLen = n 
        startInd = -1 

        while r < n:

            if mapp.get(s[r], 0) > 0:
                c += 1 

            mapp[s[r]] = mapp.get(s[r], 0) - 1 

            while c == m:
                if r - l + 1 <= minLen:
                    minLen = r - l + 1 
                    startInd = l 

                mapp[s[l]] += 1 
                if mapp[s[l]] > 0:
                    c -= 1 

                l += 1 

            r += 1 

        return s[startInd: startInd + minLen] if startInd != -1 else ""