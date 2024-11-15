from collections import Counter as c
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = c(s)
        st = ""
        for i in order:
            if i in s:
                st+=i*d[i]
        for i in s:
            if i not in st:
                st+=i*d[i]
        return st
            
            
        