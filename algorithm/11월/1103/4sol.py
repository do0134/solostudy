# 백준 2110 공유기 설치

n, c = map(int,input().split())
home = [int(input()) for _ in range(n)]
home.sort()

l = 1
r = home[n-1] - home[0]
answer = 0
if c == 2:
    answer = r
else:
    while l < r:
        mid = (l+r)//2
        idx = home[0]
        cnt = 1
        for i in range(1,n):
            if home[i] >= idx + mid:
                idx = home[i]
                cnt += 1
        if cnt >= c:
            l = mid+1
            answer = mid
        else:
            r = mid

print(answer)