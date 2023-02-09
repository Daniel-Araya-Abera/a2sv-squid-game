# Reformat Date
# https://leetcode.com/problems/reformat-date/
class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        day_data, month_data, year_data = date.split()
        
        day = day_data[:2] if len(day_data) == 4 else "0" + day_data[:1]
        month = months.index(month_data) + 1
        month_res = str(month) if month >= 10 else "0" + str(month)
        return year_data + "-" + month_res + "-" + day
