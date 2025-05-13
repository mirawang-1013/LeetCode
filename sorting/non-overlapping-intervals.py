class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Step 1: sort by the end of the intervals
        intervals.sort(key=lambda x: x[1])

        #Step 2
        remove_count = 0
        prev_end = float('-inf')

        #Step 3
        for start, end in intervals:
            if start>=prev_end:
                prev_end = end
            else:
                remove_count+=1
        return remove_count

        