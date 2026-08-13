from itertools import combinations
class Solution(object):
    def largestTriangleArea(self, points):
        max_area = 0.0
    
        for a, b, c in combinations(points, 3):
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c
        
        
            area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
        
            max_area = max(max_area, area)
    
        return max_area