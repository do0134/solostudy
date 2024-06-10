# 백준 30824 피보나치 더하기

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

fibo = [1,2]


while fibo[-1] <= 10**16:
    fibo.append(fibo[-1]+fibo[-2])


fibo2 = list()
fibo3 = list()

for combi in combinations_with_replacement(fibo,2):
    fibo2.append(sum(combi))

for combi in combinations_with_replacement(fibo,3):
    fibo3.append(sum(combi))


t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    answer = "NO"
    if n == 1:
        if k in fibo:
            answer = "YES"
    elif n == 2:
        if k in fibo2:
            answer = "YES"
    elif n == 3:
        if k in fibo3:
            answer = "YES"

    print(answer)