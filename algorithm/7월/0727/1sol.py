# 백준 14719 빗물
# https://www.acmicpc.net/problem/14719

h,w = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

for i in range(1,w-1):
    l = max(arr[:i])
    r = max(arr[i+1:])
    max_h = min(l,r)
    if arr[i] < max_h:
        answer += max_h - arr[i]

print(answer)