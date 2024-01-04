# Leetcode 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.appendleft(x)

    def pop(self) -> int:
        if not self.q1:
            return None

        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if self.q1:
            return False
        return True