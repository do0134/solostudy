# 백준 1263 시간관리

n = int(input())
arr = list()

for i in range(1,n+1):
    t, s = map(int, input().split())
    arr.append((s,t))

min_v = int(1e9)
value = 0
arr.sort()

for i in range(n):
    value += arr[i][1]
    if value > arr[i][0]:
        min_v = -1
        break
    min_v = min(min_v, arr[i][0] - value)

print(min_v)