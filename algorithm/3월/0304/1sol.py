# 백준 1662 압축

s = list(input())
answer = 0
stack = list()
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        cnt += 1
        stack.append("(")
    elif s[i] == ")":
        temp = 0
        while stack:
            now = stack.pop()
            if now == "(":
                temp *= int(stack.pop())
                break
            elif type(now) == int:
                temp += now
            else:
                temp += 1
        if not temp:
            continue
        stack.append(temp)
    else:
        stack.append(s[i])

for i in stack:
    if type(i) == int:
        answer += i
    else:
        answer += 1

print(answer)