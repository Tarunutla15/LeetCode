from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            d[key].append(s)
        l=[]
        for i in d.values():
            l.append(i)
        return l