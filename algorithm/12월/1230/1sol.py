# 백준 21921 블로그

n,x = map(int,input().split())
arr = list(map(int,input().split()))
l = 0
r = 1
answer = 0
value = arr[0]
day = 0
while r < n:
    if r - l == x-1:
        value += arr[r]
        if answer < value:
            answer = value
            day = 1
        elif answer == value:
            day += 1
        r += 1
    elif r - l < x-1:
        value += arr[r]
        r += 1
    elif r - l > x-1:
        value -= arr[l]
        l += 1

    if l == r:
        r += 1

if answer:
    print(answer)
    print(day)
else:
    print("SAD")