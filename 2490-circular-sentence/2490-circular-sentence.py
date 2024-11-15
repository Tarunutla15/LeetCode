class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s=sentence.split()
        val = False
        for i in range(len(s)):
            if i==0 and i==len(s)-1:
                if ord(s[0][0])==ord(s[0][-1]):
                    val = True
                else:
                    val = False
            elif i==len(s)-1:
                if ord(s[i][-1])==ord(s[0][0]):
                    val = True
                else:
                    val=False
            else:
                if ord(s[i][-1])==ord(s[i+1][0]):
                    val = True
                else:
                    return False
        return val