class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        while word*(c+1) in sequence:
            c+=1
        return c