class Solution(object):
    def merge(self,intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        m=[intervals[0]]
        for i in range(1,len(intervals)):
            if m[-1][1]>=intervals[i][0]:
                m[-1][1]=max(m[-1][1],intervals[i][1])
            else:
                m.append(intervals[i])
        return m
