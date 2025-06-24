class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]
        for current in intervals[1:]:
            last = results[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                results.append(current)

        return results
