class Solution:
    def sortSentence(self, s: str) -> str:
        d=['']*len(s.split())
        for word in s.split():
            pos = int(word[-1])-1
            d[pos]=word[:-1]
        return " ".join(d)