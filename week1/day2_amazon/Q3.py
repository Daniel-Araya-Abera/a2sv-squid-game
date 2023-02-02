# Reorder Data in Log Files
# /https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append([log])
        
        for i, curr_letter in enumerate(letters):
            letter_log = curr_letter[0]
            initial_len = len(letter_log.split()[0])
            sorting_param = letter_log[initial_len + 1: ] #or initial_len + 1, including space
            letters[i].append(sorting_param)
        
        letters.sort(key = lambda x: (x[1], x[0])) #by sorting param, then by identifier
        res = []
        for item in letters:
            res.append(item[0])
        for item in digits:
            res.append(item)
        return res
