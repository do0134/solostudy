# 백준 2512 예산

n = int(input())
arr = sorted(list(map(int,input().split())))
maximum = int(input())

l = 0
r = max(arr)

while l <= r:
    mid = (l+r) // 2
    now = 0

    for i in arr:
        if i >= mid:
            now += mid
        else:
            now += i

    if now > maximum:
        r = mid - 1
    elif now == maximum:
        r = mid
        break
    else:
        l = mid + 1

print(r)