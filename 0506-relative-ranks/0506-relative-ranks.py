class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = score.copy()
        c=0
        while len(temp)!=0:
            val = max(temp)
            ind = score.index(val)
            temp.remove(val)
            c+=1
            if c==1:
                score[ind]="Gold Medal"
            elif c==2:
                score[ind]="Silver Medal"
            elif c==3:
                score[ind]="Bronze Medal"
            else:
                score[ind]=str(c)
        return score