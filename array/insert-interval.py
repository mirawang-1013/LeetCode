class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False

        for interval in intervals:
            #在newInterval的左边
            if interval[1]<newInterval[0]:
                result.append(interval)
            #在newInterval的右边
            elif interval[0]>newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
        
            #重叠了合并
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not inserted:
            result.append(newInterval)

        return result
        