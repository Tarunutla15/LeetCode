class Solution:
    def sortSentence(self, s: str) -> str:
        w=s.split()
        w.sort(key=lambda x:x[-1])
        sent = " ".join([word[:-1] for word in w])
        return sent
        