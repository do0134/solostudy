# codeforces Earning on Bets

import sys
import math

input = sys.stdin.readline


def make_lcm(a,b):
    return (a*b) // math.gcd(a,b)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    result = arr[0]

    for i in range(1,len(arr)):
        result = make_lcm(result, arr[i])

    sum_v = 0

    for i in arr:
        sum_v += result // i

    if sum_v >= result:
        print(-1)
        continue

    answer = list()

    for i in range(n):
        answer.append(result // arr[i])

    print(" ".join(map(str,answer)))