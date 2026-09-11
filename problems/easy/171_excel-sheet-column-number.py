class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            digit = ord(char) - ord('A') + 1
            result = result * 26 + digit
        return result