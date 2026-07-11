class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operation = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if char in '+-*/' or i == len(s) - 1:
                if i == len(s) - 1 or char != ' ':
                    if operation == '+':
                        stack.append(num)
                    elif operation == '-':
                        stack.append(-num)
                    elif operation == '*':
                        stack.append(stack.pop() * num)
                    elif operation == '/':
                        stack.append(int(stack.pop() / num))
                    
                    if char in '+-*/':
                        operation = char
                    num = 0
        
        return sum(stack)