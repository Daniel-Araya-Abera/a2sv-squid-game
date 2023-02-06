# Detect Squares
# https://leetcode.com/problems/detect-squares/
class DetectSquares:

    def __init__(self):
        self.all_points = collections.defaultdict(int) #all_pts_freq
        self.cols = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.all_points[point] += 1
        self.cols[point[1]].add(point)
        
    def count(self, point: List[int]) -> int:
        point = tuple(point)
        res = 0
        seen = set()
        
        row, col = point
        for possible_pt in self.cols[col]:
            x = possible_pt[0] - point[0]
            if x > 0:
                res += self.checkPossible1(point, x, seen)
                res += self.checkPossible2(point, x, seen)
            elif x < 0:
                res += self.checkPossible3(point, -x, seen)
                res += self.checkPossible4(point, -x, seen)        
        return res
       
    def checkPossible1(self, point, x, seen):
        a, b = point
        pt1 = a + x, b
        pt2 = a, b - x
        pt3 = a + x, b - x
        return self.getCurrRes(point, pt1, pt2, pt3, seen)

    def checkPossible2(self, point, x, seen):
        a, b = point
        pt1 = a + x, b + x
        pt2 = a, b + x
        pt3 = a + x, b
        return self.getCurrRes(point, pt1, pt2, pt3, seen)
    
    def checkPossible3(self, point, x, seen):
        a, b = point
        pt1 = a, b + x
        pt2 = a - x, b + x
        pt3 = a - x, b
        return self.getCurrRes(point, pt1, pt2, pt3, seen)
    
    def checkPossible4(self, point, x, seen):
        a, b = point
        pt1 = a - x, b
        pt2 = a - x, b - x
        pt3 = a, b - x
        return self.getCurrRes(point, pt1, pt2, pt3, seen)
        
    def getCurrRes(self, point, pt1, pt2, pt3, seen):
        coordinates = tuple(sorted([point, pt1, pt2, pt3]))
        if coordinates not in seen:
            seen.add(coordinates)
            return self.all_points[pt1] * self.all_points[pt2] * self.all_points[pt3]
        return 0


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


'''
1 ------ 4
  |    |
  |    |
2 ------ 3


'''
