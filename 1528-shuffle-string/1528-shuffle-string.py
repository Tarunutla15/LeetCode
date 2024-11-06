class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d={}
        s1=''
        for i,j in zip(indices,s):
            d[i]=j
        for i in sorted(d):
            s1+=d[i]
        return s1