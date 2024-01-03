# 백준 1543 문서검색
# https://www.acmicpc.net/problem/1543

s1 = input()
s2 = input()
answer = 0

l1 = len(s1)
l2 = len(s2)

idx = 0

while idx < l1:
    if idx+l2 > l1:
        break
    elif s1[idx:idx+l2] == s2:
        answer += 1
        idx = idx+l2
    elif s1[idx:idx+l2] != s2:
        idx += 1

print(answer)