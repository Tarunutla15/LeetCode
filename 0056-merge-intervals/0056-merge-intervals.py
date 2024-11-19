class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        cur = 0
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[len(res)-1][1] >= intervals[i][0]:
                res[len(res)-1][1]=max(res[len(res)-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        print(res)
        return res
            
        