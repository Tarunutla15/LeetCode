class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sum(list(map(ord,s)))
        t = sum(list(map(ord,t)))
        return chr(t-s)
        
        