class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = [intervals[0]]
        for sublist in intervals[1:]:
            last_in_list = results[-1]
            if sublist[0] <= last_in_list[1]:
                last_in_list[1] = max(last_in_list[1], sublist[1])
            else:
                results.append(sublist)
        return results
