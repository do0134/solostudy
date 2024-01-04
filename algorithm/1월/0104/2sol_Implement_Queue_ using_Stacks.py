# Leetcode 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.stack = list()
        self.temp_stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack)-1):
            self.temp_stack.append(self.stack.pop())
        val = self.stack.pop()
        for _ in range(len(self.temp_stack)):
            self.stack.append(self.temp_stack.pop())
        return val

    def peek(self) -> int:
        return self.stack[0] if self.stack else None

    def empty(self) -> bool:
        return bool(not self.stack)