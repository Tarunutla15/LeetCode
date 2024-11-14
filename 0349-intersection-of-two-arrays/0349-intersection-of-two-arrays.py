class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        l=[]
        for i in list(set(nums1)):
            if i in list(set(nums2)):
                l.append(i)
        return l
        