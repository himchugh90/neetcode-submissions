"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # print(intervals[1].start)
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x: x.start)
        merged = [intervals[0]]
        # print(merged)
        for i in range(1, len(intervals)):
            if intervals[i].start < merged[-1].end:
                return False
            else:
                merged.append(intervals[i])
        return True

      






        # # print(intervals[0].end)
        # if len(intervals) == 0:
        #     return True
        # intervals.sort(key=lambda x: x.start)
        # merged = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if merged[-1].end > intervals[i].start:
        #         return False
        #     else:
        #         merged.append(intervals[i])
        # return True
            
 
        