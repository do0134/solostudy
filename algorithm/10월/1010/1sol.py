min_v = int(1e9)
x,y = map(int,input().split())
z = (y*100)/x
if z >= 99:
    print(-1)
else:
    l = 1
    r = 1000000000
    answer = 0
    while l <= r:
        mid = (l+r)//2
        if ((y+mid)*100)//(x+mid) > z:
            r = mid-1
            answer = mid
        else:
            l = mid+1

    print(answer)






