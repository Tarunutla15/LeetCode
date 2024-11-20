class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        s1=''
        curval=0
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        
        while i<len(s) and j<len(s):
            if s[j] not in s1:
                s1+=s[j]
                j+=1
            else:  
                i+=1
                j=i
                curval=max(curval,len(s1))
                s1=''
        return max(curval,len(s1))
                
            
            
            

        