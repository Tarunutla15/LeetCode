class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s1=''
        s.sort(key=lambda x:x[-1])
        val = "123456789"
        s=" ".join(s)
        for i in s:
            if i in val:
                continue
            else:
                s1+=i
        print(s1)
        return s1
        