class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        l=[]
        for item in items1:
            if item[0] not in d:
                d[item[0]]=item[1]
            else:
                d[item[0]]+=item[1]
        for item in items2:
            if item[0] not in d:
                d[item[0]]=item[1]
            else:
                d[item[0]]+=item[1]
        for i,j in d.items():
            l.append([i,j])
        print(l)
        l.sort(key=lambda x:x[0])
        return l