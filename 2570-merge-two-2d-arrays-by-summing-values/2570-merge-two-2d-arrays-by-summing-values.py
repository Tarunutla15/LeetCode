class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = nums1+nums2
        d={}
        for item in nums:
            if item[0] not in d:
                d[item[0]]=item[1]
            else:
                d[item[0]]+=item[1]
        l=[]
        for i,j in d.items():
            l.append([i,j])
            
        l.sort(key=lambda x:x[0])
        return l