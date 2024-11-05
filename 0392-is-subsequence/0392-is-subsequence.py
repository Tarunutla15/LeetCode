class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in t:
            if index < len(s) and char == s[index]:
                index += 1 
            if index == len(s):
                return True
        return index == len(s)
