class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        current_arrow = points[0][1]
        arrow = 1
        for point in points[1:]:
            if current_arrow >= point[0]:
                continue
            
            current_arrow = point[1]
            arrow += 1
        return arrow
        