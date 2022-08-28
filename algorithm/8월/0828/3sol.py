from collections import deque

def check(shuffle):
    if shuffle == sorted(card) or shuffle == sorted(card)[::-1]:
        return True
    else :
        return False

def mix(x,card):
    temp = []
    if x < n//2:
        l = deque(card[:n//2])
        r = deque(card[n//2:])
        num = n//2 -x
    else:
        l = deque(card[n//2 :])
        r = deque(card[:n//2])
        num = x-(n//2)+1
    for _ in range(num):
        temp.append(l.popleft())
    while len(r) > num :
        temp.append(r.popleft())
        temp.append(l.popleft())
    while r :
        temp.append(r.popleft())
    return temp

def solve(idx,shuffle):
    global answer
    if idx >= answer or idx > 5:
        return
    if check(shuffle):
        answer = min(answer,idx)
    for i in range(1,n):
        solve(idx+1,mix(i,shuffle))
    pass

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    card = list(map(int,input().split()))
    answer = int(1e9)
    solve(0,card)
    if answer == int(1e9):
        answer = -1
    print(f'#{tc} {answer}')