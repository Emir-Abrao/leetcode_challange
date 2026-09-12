import re

class Solution:
    def validPhoneNumbers(self) -> None:
        pattern = re.compile(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$')
        with open('file.txt', 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                if pattern.match(line):
                    print(line)