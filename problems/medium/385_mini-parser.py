class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
            self._integer = None
        else:
            self._integer = value
            self._list = None
    
    def isInteger(self):
        return self._integer is not None
    
    def add(self, elem):
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)
    
    def setInteger(self, value):
        self._integer = value
        self._list = None
    
    def getInteger(self):
        return self._integer
    
    def getList(self):
        return self._list

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        current = None
        root = None
        i = 0
        
        while i < len(s):
            char = s[i]
            
            if char == '[':
                new_nested = NestedInteger()
                if current is not None:
                    current.add(new_nested)
                stack.append(new_nested)
                current = new_nested
                if root is None:
                    root = new_nested
                i += 1
            elif char == ']':
                stack.pop()
                current = stack[-1] if stack else None
                i += 1
            elif char == ',':
                i += 1
            else:
                j = i
                if s[j] == '-':
                    j += 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                current.add(NestedInteger(num))
                i = j
        
        return root