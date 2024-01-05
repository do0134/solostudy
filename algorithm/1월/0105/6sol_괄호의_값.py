# 백준 2504 괄호의 값

s = input()


def solve(char: str) -> int:
    stack = list()
    answer = 0
    value = 1

    for i in range(len(char)):
        if char[i] == "(":
            value *= 2
            stack.append("(")
        elif char[i] == "[":
            value *= 3
            stack.append("[")
        elif char[i] == ")":
            if not stack or stack[-1] == "[":
                return 0
            if char[i-1] == "(":
                answer += value
            stack.pop()
            value //= 2
        else:
            if not stack or stack[-1] == "(":
                return 0
            if char[i-1] == "[":
                answer += value
            stack.pop()
            value //= 3
    if stack:
        return 0

    return answer


print(solve(s))