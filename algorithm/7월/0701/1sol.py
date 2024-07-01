# 백준 21600 계단

n = int(input())
arr = list(map(int,input().split()))

answer = 0
now = 0
for i in arr:
    if i >= now+1:
        now += 1
    else:
        now = i

    answer = max(answer, now)

print(answer)
