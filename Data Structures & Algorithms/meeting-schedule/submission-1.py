"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        min_time = 100000
        max_time = 0
        sum_time = 0
        for meeting in intervals:
            if meeting.start < min_time:
                min_time = meeting.start
            if meeting.end > max_time:
                max_time = meeting.end
            sum_time += meeting.end - meeting.start
        if sum_time > max_time-min_time:
            return False
        return True