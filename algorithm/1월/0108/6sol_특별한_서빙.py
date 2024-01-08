# 백준 27896 특별한 서빙
# https://www.acmicpc.net/problem/27896

import heapq as hq

n,m = map(int,input().split())
foods = list(map(int,input().split()))
heap = list()


def solve(h, f):
    answer = 0
    bad = 0

    for food in f:
        bad += food
        hq.heappush(h, -food)
        while bad >= m:
            a = hq.heappop(h)
            bad -= -(a*2)
            answer += 1

    return answer


print(solve(heap, foods))