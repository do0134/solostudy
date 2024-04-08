# 백준 31378 매우 어려운 문제

n,m = map(int,input().split())
answer = 1

if m > n:
    for i in range(2, n + 1):
        answer = answer*i%m

    print(answer)
else:
    print(0)
