k = int(input())
answer = 0
value = 1

while value < k:
    value *= 2

answer = value
cnt = 0

while k > 0:
    if k >= value:
        k -= value
    else:
        value //= 2
        cnt += 1

print(answer, cnt)