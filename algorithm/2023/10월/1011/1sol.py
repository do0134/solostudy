# 백준 22233 가희와 키워드

from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
keywords = defaultdict(bool)
answer = n

for _ in range(n):
    s = input().rstrip()
    keywords[s] = True

for _ in range(m):
    memo = input().rstrip().split(',')
    for key in memo:
        if keywords[key]:
            answer -= 1
            keywords[key] = False

    print(answer)