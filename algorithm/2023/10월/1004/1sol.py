# 백준 2512 예산

n = int(input())
arr = list(map(int,input().split()))
maximum = int(input())

l,r = 0, max(arr)

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
    else:
        l = mid + 1


print(r)