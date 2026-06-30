class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "" 
        for word in strs:
            s = s + str(len(word) + 199) + "/:" + word 
            
        return s  

    def decode(self, s: str) -> List[str]:
        ind = 0 
        n = len(s) 
        inds = []
        
        while ind < n:
            if s[ind].isdigit():
                word_lenn = int(s[ind: ind + 3]) - 199
                inds.append((ind + 5, word_lenn))
                # inds.append((ind + 3, int(s[ind]))) 
                ind = ind + 5 + word_lenn
                
        # print(inds) 
        return [s[st: st+e] for st, e in inds]