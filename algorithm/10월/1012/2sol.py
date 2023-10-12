# 백준 2012 등수 매기기

n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

arr.sort()
idx = 1
answer = 0

for i in range(n):
    if idx != arr[i]:
        answer += abs(idx - arr[i])
    idx += 1
print(answer)