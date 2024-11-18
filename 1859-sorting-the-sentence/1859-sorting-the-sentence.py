class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        s1=''
        for word in s.split():
            d[int(word[-1])]=word[:-1]
        for i in range(1,len(s.split())+1):
            s1+=d[i]+' '
        print(s1)
        return s1[:-1]
        