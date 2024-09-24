class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=[]
        for i in range(0,len(s),k):
            l.append(s[i:i+k])
        for i in range(len(l)):
            if i%2==0:
                l[i]=l[i][::-1]
        return "".join(l)