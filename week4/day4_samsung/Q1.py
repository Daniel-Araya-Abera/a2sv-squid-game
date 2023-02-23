# Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        pt1_x1, pt1_y1, pt1_x2, pt1_y2 = rec1
        pt2_x1, pt2_y1, pt2_x2, pt2_y2 = rec2
        
        x_start = max(pt1_x1, pt2_x1)
        x_end = min(pt1_x2, pt2_x2)
        
        y_start = max(pt1_y1, pt2_y1)
        y_end = min(pt1_y2, pt2_y2)
        
        return x_start < x_end and y_start < y_end
