class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _transfer_if_needed(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())