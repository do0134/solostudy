# 백준 1744 수 묶기

from collections import deque


n = int(input())
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
arr = deque(arr)
answer = 0

while arr and arr[0] > 1:
    value1 = arr.popleft()
    if not arr:
        answer += value1
        break
    elif arr:
        if arr[0] > 1:
            value2 = arr.popleft()
            answer += value1*value2
            continue
        elif arr[0] == 1:
            value2 = arr.popleft()
            answer += value1+value2
        else:
            answer += value1
            break

while arr and arr[-1] < 0:
    value1 = arr.pop()
    if not arr:
        answer += value1
        break
    elif arr:
        if arr[-1] < 0:
            value2 = arr.pop()
            answer += value1*value2
        elif not arr[-1]:
            value2 = arr.pop()
            answer += 0
        else:
            answer += value1
            break

if arr:
    answer += sum(arr)

print(answer)
