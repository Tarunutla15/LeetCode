class Solution:
    def check(self, nums: List[int]) -> bool:
        l1,l2=[],[]
        ind=0
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                l1.append(nums[i])
                ind+=1
            else:
                l1.append(nums[i])
                break
        for i in range(ind+1,len(nums)):
            l2.append(nums[i])
        print(l1,l2)
        if len(l2)==0:
                return True
        for i in range(len(l2)-1):
            if l2[i+1]>=l2[i]:
                continue
            else:
                return False
        for i in l1:
            
            if l2[-1]>i:
                return False
        return True
                
            
            
        