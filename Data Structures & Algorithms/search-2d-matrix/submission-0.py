class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat) 
        m = len(mat[0]) 

        l = 0 
        r = (n * m) - 1 

        while l <= r:
            mid = l + (r - l // 2) 

            r = mid // m 
            c = mid % m 

            if mat[r][c] == target:
                return True 

            elif mat[r][c] < target:
                l = mid + 1 

            else:
                r = mid - 1 

        return False 