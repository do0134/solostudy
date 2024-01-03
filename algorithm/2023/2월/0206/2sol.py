from collections import deque

n,d,k,c = map(int,input().split())
answer = 0
eat = deque()
v = [0] * (d+1)
coupon = False

for _ in range(n) :
    sushi = int(input())

    if sushi == c :
        coupon = True

    if v[sushi] :
        while v[sushi] :
            temp = eat.popleft()
            v[temp] = 0
            if temp == c and sushi != c:
                coupon = False
        eat.append(sushi)
        v[sushi] = 1
    elif len(eat) == k :
        if coupon :
            answer = k+1
            break
        else :
            temp = eat.popleft()
            v[temp] = 0
            if temp == c :
                coupon = False
            eat.append(sushi)
            v[sushi] = 1

    elif len(eat) < k :
        eat.append(sushi)
        v[sushi] = 1

    if answer < len(eat) :
        if coupon :
            answer = len(eat)
        elif not coupon :
            answer = len(eat) + 1


print(answer)