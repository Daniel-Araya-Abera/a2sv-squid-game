# Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        plants = []
        for i in range(n):
            plants.append((plantTime[i], growTime[i]))
        
        plants.sort(key=lambda x: -x[1]) #by growTime decreasing
        
        end = 0
        start_plant = 0
        
        for curr_plant_time, curr_grow_time in plants:
            bloom_size = curr_plant_time + curr_grow_time #including bloom
            curr_end = start_plant + (bloom_size)
            end = max(end, curr_end)
            start_plant += curr_plant_time
        
        return end
