class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maxCount=0
        for i in nums:
            if i==1:
                c+=1
            elif i==0:
                maxCount=max(maxCount,c)
                c=0
        return max(maxCount,c)
            