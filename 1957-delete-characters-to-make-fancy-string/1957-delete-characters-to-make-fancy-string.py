class Solution:
    def makeFancyString(self, s: str) -> str:
        l = []
        for i in s:
            if len(l)>=2 and l[-1]==i and l[-2]==i:
                continue
            l.append(i)
        return "".join(l)
            