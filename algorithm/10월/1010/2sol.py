n,l,w,h = map(int,input().split())
s = 0
e = min(l,w,h)


for _ in range(1000):
    mid = (s+e)/2
    if (l//mid) * (w//mid) * (h//mid) >= n:
        s = mid
    else:
        e = mid
print(e)
