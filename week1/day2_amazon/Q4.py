# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
class Solution:
    def numberToWords(self, num: int) -> str:
        placevalues = {3: " Billion", 2: " Million", 1: " Thousand", 0: ""}
        tens = {0: "", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        tens_alternate = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
        ones = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

        if num == 0:
            return "Zero"

        num = str(num)
        n = len(num)
        initial_input = []
        i = n - 1
        while i >= 0:
            initial_input.append(num[max(0, i - 2): i + 1])
            i -= 3
        initial_input.reverse()
        res = []

        for i, curr_slice in enumerate(initial_input):
            place_value_idx = len(initial_input) - i - 1
            curr_res = self.helper(None, curr_slice, placevalues, tens, tens_alternate, ones)
            if curr_res != "":
                res.append(curr_res + placevalues[place_value_idx])
            else:
                res.append(curr_res)
        
        final = " ".join(res)
        return " ".join(final.split())

    def helper(self,  place_value_idx, curr_slice, placevalues, tens, tens_alternate, ones):
        if len(curr_slice) < 3:
            remaining = 3 - len(curr_slice)
            curr_slice = "0" * remaining + curr_slice
        
        curr_res = []
        for i, digit in enumerate(curr_slice):
            curr_digit = int(digit)
            if i == 0:
                if curr_digit > 0:
                    curr_item = ones[int(digit)]
                    if curr_item != "":
                        curr_res.append(curr_item + " " + "Hundred")
            elif i == 1:
                if curr_digit == 1:
                    curr_item = tens_alternate[int(curr_slice[2])]
                    if (curr_item != ""):
                        curr_res.append(curr_item)
                    break
                curr_item = tens[int(curr_slice[1])]
                if curr_item != "":
                    curr_res.append(curr_item)
            else:
                curr_item = ones[int(digit)]
                if curr_item != "":
                    curr_res.append(curr_item)

        return " ".join(curr_res) if len(curr_res) > 0 else "" 
