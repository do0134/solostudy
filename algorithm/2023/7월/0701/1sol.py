# 백준 1459 걷기
# https://www.acmicpc.net/problem/1459

x,y,w,s = map(int,input().split())
time1 = (x+y)*w
time2 = 0

if (x+y)%2:
    time2 = (max(x,y)-1)*s+w
else:
    time2 = max(x,y)*s

time3 = min(x,y)*s + (max(x,y)-min(x,y))*w

print(min(time1,time2,time3))