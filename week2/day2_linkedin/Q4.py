# Text Justification
# https://leetcode.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        lines = []
        
        curr_width = word_idx = 0
        while word_idx < n:
            lines.append([words[word_idx]]) #add first word
            curr_width = len(words[word_idx])
            word_idx += 1
            
            while word_idx < n and curr_width + 1 + len(words[word_idx]) <= maxWidth:
                curr_word = words[word_idx]
                lines[-1].append(curr_word)
                curr_width += 1 + len(curr_word)
                word_idx += 1
            
            isLastLine = False if word_idx < n else True
            lines[-1] = self.justifyLine(lines[-1], isLastLine, curr_width, maxWidth)
        
        return lines
    
    def justifyLine(self, curr_line, isLastLine, curr_width, max_width):
        remaining = max_width - curr_width
        words_len = len(curr_line)
        
        if isLastLine:
            return " ".join(curr_line) + " " * remaining
        
        space_input_areas = words_len - 1
        added_spaces = 0
        curr_res = []
        if space_input_areas > 0:
            curr_res.append(curr_line[0])
            extras = remaining % space_input_areas
            equal_share = remaining // space_input_areas
            for i in range(1, len(curr_line)):
                curr_spaces = equal_share + 1 if i <= extras else equal_share
                curr_res.append(" " * (curr_spaces + 1))
                added_spaces += curr_spaces
                curr_res.append(curr_line[i])
        else:
            curr_res = list(" ".join(curr_line))
        
        right_side_remaining = remaining - added_spaces
        curr_res.append(" " * right_side_remaining)
        return "".join(curr_res)    
