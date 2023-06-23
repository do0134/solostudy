# 백준 28245 배고파(HARD)
# https://www.acmicpc.net/problem/28245

n = int(input())
for _ in range(n):
    m = int(input())
    answer = list()
    max_v = 10**18+1
    target = 0

    for i in range(60):
        if 2**i > m:
            break
        for j in range(i,60):
            temp = 2**i + 2**j
            if abs(temp-m) < max_v:
                target = temp
                max_v = abs(temp-m)
                answer = [i,j]
            elif abs(temp-m) == max_v:
                if temp < target:
                    target = temp
            if temp >= m:
                break

    print(*answer)