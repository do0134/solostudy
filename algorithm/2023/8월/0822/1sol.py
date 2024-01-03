# 백준 20055 컨베이어 벨트 위의 로봇

from collections import deque


def rotate():
    global arr, v
    temp = arr.pop()
    arr.appendleft(temp)
    v.pop()
    v.appendleft(0)
    v[n-1] = 0


def move():
    global arr, v, cnt
    for i in range(n-2,-1,-1):
        if v[i]:
            if arr[i+1] and not v[i+1]:
                arr[i+1] -= 1
                v[i] = 0
                if i+1 != n-1:
                    v[i+1] = 1
                if not arr[i+1]:
                    cnt += 1


def up():
    global cnt, v, arr
    if arr[0] > 0:
        arr[0] -= 1
        v[0] = 1
        if not arr[0]:
            cnt += 1


n, k = map(int,input().split())
arr = deque(list(map(int,input().split())))
v = deque([0]*n)
cnt = arr.count(0)
answer = 0

while cnt < k:
    answer += 1
    rotate()
    move()
    up()

print(answer)
