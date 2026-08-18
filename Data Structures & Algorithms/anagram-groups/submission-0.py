class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = collections.defaultdict(list) 

        for word in strs:
            lis = []
            for ch in word:
                lis.append(ord(ch)) 
            lis.sort()
            mapp[tuple(lis)].append(word) 

        res = [] 
        for k, v in mapp.items():
            res.append(v) 

        return res 