class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums = list(set(nums1)).copy()
        nums2 = list(set(nums2))
        for i in nums1:
            if i in nums2:
                continue
            else:
                nums.remove(i)
        return nums
        