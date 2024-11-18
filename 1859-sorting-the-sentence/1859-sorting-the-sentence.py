class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        s1=''
        for word in s.split():
            d[int(word[-1])]=word[:-1]
        sent = " ".join([d[i+1] for i in range(len(s.split()))])
        print(sent)
        return sent