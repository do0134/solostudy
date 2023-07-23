# 백준 2003 수들의 합2
#

n, m = map(int,input().split())
arr = list(map(int,input().split()))

l = r = 0
answer = 0
value = 0

while l <= r < n:
    if l == r:
        if arr[l] == m:
            answer += 1
        value = arr[l]
        r += 1
    else:
        value += arr[r]

        if value == m:
            answer += 1
            r += 1
        elif value > m:
            value -= arr[l]
            l += 1
            value -= arr[r]
        elif value < m:
            r += 1

print(answer)