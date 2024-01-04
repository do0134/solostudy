# Leetcode 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues

class MyStack:
    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return bool(not self.stack)