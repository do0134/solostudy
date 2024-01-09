# 백준 4949 균형잡힌 세상

import sys
input = sys.stdin.readline


def solve(s):
    stack = list()

    for i in range(len(s)-1,-1,-1):
        if s[i] == ")" or s[i] == "]":
            stack.append(s[i])

        elif s[i] == "[":
            if not stack or stack[-1] != "]":
                return False
            else:
                stack.pop()

        elif s[i] == "(":
            if not stack or stack[-1] != ")":
                return False
            else:
                stack.pop()
    if stack:
        return False

    return True


while True:
    s = input().rstrip()
    if s == ".":
        break

    if solve(s):
        print("yes")
    else:
        print("no")
