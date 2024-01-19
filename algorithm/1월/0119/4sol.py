# 백준 2805 나무 자르기

n,m = map(int,input().split())
tree = list(map(int,input().split()))

l = 0
r = max(tree)
sum_v = sum(tree)

while l <= r:
    mid = (l+r) // 2
    now = 0

    for t in tree:
        if t >= mid:
            now += mid
        else:
            now += t

    if sum_v - now > m:
        l = mid+1
    elif sum_v - now == m:
        r = mid
        break
    elif sum_v - now < m:
        r = mid-1

print(r)