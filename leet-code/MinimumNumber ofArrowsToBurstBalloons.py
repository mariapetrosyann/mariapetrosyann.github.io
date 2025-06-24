class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrow = 1
        current_end = points[0][1]
        for xstart, xend in points[1:]:
            if xstart > current_end:
                arrow += 1
                current_end = xend
            else:
                current_end = min(current_end, xend)
        return arrow
