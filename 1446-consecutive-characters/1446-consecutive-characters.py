class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        maxval=1
        k=1
        i=0
        while k!=(len(s)):
            if s[i]==s[k]:
                c+=1
                k+=1
                i+=1
                maxval=max(maxval,c)
            else:
                k+=1
                c=1
                i=k-1
        print(maxval)
                
        return maxval
            
            
        