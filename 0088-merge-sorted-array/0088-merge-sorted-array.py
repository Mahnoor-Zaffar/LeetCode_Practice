class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Start at the very end of nums1 (the empty space)
        last = m + n - 1
        
        # Pointers for the end of the "actual" numbers in nums1 and nums2
        i = m - 1
        j = n - 1
        
        # Compare numbers from the back and move the larger one to the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
            
        # If there are any numbers left in nums2, fill them in
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
        