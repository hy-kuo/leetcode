# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from operator import itemgetter

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals = sorted(intervals, key=lambda interval: interval.start)
        if len(intervals) <= 1:
            return intervals
        idx = 0
        while idx < len(intervals)-1:
            a = intervals[idx]
            b = intervals[idx+1]
            if  a.end < b.start:
                idx+=1
            else:
                new_i = Interval(s=min(a.start, b.start), e=max(a.end, b.end))
                intervals[idx+1] = new_i
                del intervals[idx]
        return intervals
                
            
