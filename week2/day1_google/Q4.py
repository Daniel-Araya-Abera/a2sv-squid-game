# Race Car
# https://leetcode.com/problems/race-car/
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set([(0,1)])
        
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            
            accelerate_pos, accelerate_speed = pos + speed, speed * 2
            reverse_pos, reverse_speed = pos, 1
            if speed > 0:
                reverse_speed = -1
            
            if (accelerate_pos, accelerate_speed) not in visited:
                queue.append((accelerate_pos, accelerate_speed, steps + 1))
                visited.add((accelerate_pos, accelerate_speed))
            
            if (reverse_pos, reverse_speed) not in visited:
                queue.append((reverse_pos, reverse_speed, steps + 1))
                visited.add((reverse_pos, reverse_speed))
        
        return -1
