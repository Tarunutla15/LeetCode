class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = list(set(nums1))
        # nums2 = list(set(nums2))
        # l=[]
        # for i in nums1:
        #     if i in nums2:
        #         l.append(i)
        return list(set(nums1)&set(nums2))
        