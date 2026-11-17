class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        r = n - 1
        last = m + n - 1

        while l >= 0 and r >= 0  and last >= 0:
            if nums2[r] > nums1[l]:
                nums1[last] = nums2[r]
                r = r - 1
            else:
                nums1[last] = nums1[l]
                nums1[l] = 0
                l = l - 1
            
            last = last - 1
        
        while r >= 0 and last >= 0:
            nums1[last] = nums2[r]
            last = last - 1
            r = r - 1
        
        