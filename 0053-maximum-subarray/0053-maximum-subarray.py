class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval = nums[0]
        cs = 0
        for i in nums:
            if cs<0:
                cs=0
            cs+=i
            maxval = max(maxval,cs)
        return maxval
                    