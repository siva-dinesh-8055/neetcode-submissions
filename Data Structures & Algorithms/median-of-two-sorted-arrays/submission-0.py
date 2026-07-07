class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) 
        m = len(nums2) 

        total = n + m 
        
        mid_ele = None  
        mid_ele_prev = None 

        mid_ele_ind = total // 2 

        l = r = 0 
        curr = -1 
        while l < n and r < m:

            if nums1[l] <= nums2[r]:
                curr += 1 
                if curr == mid_ele_ind - 1:
                    mid_ele_prev = nums1[l] 

                elif curr == mid_ele_ind:
                    mid_ele = nums1[l] 
                    break 

                l += 1 

            else:
                curr += 1 

                if curr == mid_ele_ind - 1:
                    mid_ele_prev = nums2[r] 

                elif curr == mid_ele_ind:
                    mid_ele = nums2[r] 
                    break 
                r += 1 

        while l < n:
            curr += 1 
            if curr == mid_ele_ind - 1:
                mid_ele_prev = nums1[l] 

            elif curr == mid_ele_ind:
                mid_ele = nums1[l] 
                break 

            l += 1 

        while r < m:
            curr += 1 

            if curr == mid_ele_ind - 1:
                mid_ele_prev = nums2[r] 

            elif curr == mid_ele_ind:
                mid_ele = nums2[r] 
                break 
            r += 1 

        if total & 1 == 1:
            return float(mid_ele) 

        else:
            return (mid_ele + mid_ele_prev) / 2  