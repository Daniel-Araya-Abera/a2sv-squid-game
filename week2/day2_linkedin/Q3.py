# Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr_direction = (0,1)
        curr_pos = (0,0)
        rotation_left = {(1,0): (0,1), (0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0)}
        rotation_right = {(1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1), (0,1): (1,0)}
        
        for i, command in enumerate(instructions):
            if command == "G":
                curr_pos = self.moveForward(curr_direction, curr_pos)
            elif command == "L":
                curr_direction = self.rotate(curr_direction, rotation_left)
            elif command == "R":
                curr_direction = self.rotate(curr_direction, rotation_right)
            
        return curr_direction != (0,1) or curr_pos == (0,0) #
    
    def moveForward(self, curr_direction, curr_pos):
        return (curr_pos[0] + curr_direction[0], curr_pos[1] + curr_direction[1])
    
    def rotate(self, curr_direction, rotation_matrix):
        return rotation_matrix[curr_direction]
