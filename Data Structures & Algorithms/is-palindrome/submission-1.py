class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        l = 0 
        r = len(s) - 1 

        while l < r:

            if ((97 <= ord(s[l]) <= 122) or (65 <= ord(s[l]) <= 90) or (48 <= ord(s[l]) <= 57)) and ((97 <= ord(s[r]) <= 122) or (65 <= ord(s[r]) <= 90) or (48 <= ord(s[r]) <= 57)):
                if s[l] == s[r]:
                    l += 1 
                    r -= 1 

                else:
                    return False 

            elif not ((97 <= ord(s[l]) <= 122) or (65 <= ord(s[l]) <= 90) or (48 <= ord(s[l]) <= 57)):
                l += 1 

            elif not ((97 <= ord(s[r]) <= 122) or (65 <= ord(s[r]) <= 90) or (48 <= ord(s[r]) <= 57)):
                r -= 1 
        
        return True 