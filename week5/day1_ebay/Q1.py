# Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_start, year_end = 1950, 2050
        years = [0] * (year_end - year_start + 1)

        logs.sort()
        
        for log in logs:
            birth, death = log
            years[birth - year_start] += 1
            years[death - year_start] -= 1

        max_population = years[0]
        for idx in range(1, len(years)):
            years[idx] += years[idx - 1]
            max_population = max(max_population, years[idx])
        
        for idx in range(len(years)):
            if years[idx] == max_population: #return earliest
                return idx + year_start
        
        return -1 #return year_start

'''
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_start, year_end = 1950, 2050
        max_population, res = 0, None
        
        for year in range(year_start, year_end + 1):
            alive_count = 0
            for birth, death in logs:
                if birth <= year < death:
                    alive_count += 1
            
            if alive_count > max_population:
                max_population = alive_count
                res = year
        
        return res
'''
