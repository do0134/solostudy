# 백준 2002 추월

from collections import deque

n = int(input())

enter = deque()
end = deque()

check = dict()

for i in range(n):
    num = input()
    enter.append(num)

for i in range(n):
    num = input()
    end.append(num)
    check[num] = False

answer = 0

while end:
    if end[0] == enter[0]:
        check[enter[0]] = True
        end.popleft()
        enter.popleft()

    elif end[0] != enter[0]:
        check[end[0]] = True
        end.popleft()
        answer += 1

    while enter and check[enter[0]]:
        enter.popleft()

print(answer)