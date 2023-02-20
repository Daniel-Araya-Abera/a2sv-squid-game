# Validate IP Address
# https://leetcode.com/problems/validate-ip-address/
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        validIPv4 = self.isValidIPv4(queryIP)
        if validIPv4:
            return "IPv4"
        
        validIPv6 = self.isValidIPv6(queryIP)
        if validIPv6:
            return "IPv6"
        
        return "Neither"
    
    def isValidIPv4(self, queryIP):
        values = queryIP.split(".")
        if len(values) != 4:
            return False
        
        for curr_item in values:
            if not(curr_item.isdigit() and 0 <= int(curr_item) <= 255 and curr_item == str(int(curr_item))):
                return False
        
        return True
    
    def isValidIPv6(self, queryIP):
        values = queryIP.split(":")
        if len(values) != 8:
            return False
        
        for curr_item in values:
            if not(1 <= len(curr_item) <= 4):
                return False
            for char_item in curr_item:
                if not(ord('a') <= ord(char_item) <= ord('f') or ord('A') <= ord(char_item) <= ord('F') or char_item.isdigit()):
                    return False
        
        return True
