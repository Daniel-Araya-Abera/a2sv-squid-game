# Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution:
    def convertToTitle(self, column_number: int) -> str:
        res = []
        char_size = 26
        while column_number > 0:
            curr_amount = (column_number - 1) % char_size #curr_amount is [0,25] -> [A,Z] #
            column_number = (column_number - 1 ) // char_size #
            res.append(self.getChar(curr_amount))
        
        return "".join(res[::-1])
    
    def getChar(self, idx):
        return chr(idx + ord('A'))
