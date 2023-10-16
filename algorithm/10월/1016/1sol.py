# 백준 15903 카드합체놀이

import heapq as hq

n,m = map(int,input().split())
num = list(map(int,input().split()))

hq.heapify(num)

for _ in range(m):
    a = hq.heappop(num)
    b = hq.heappop(num)
    value = a + b
    hq.heappush(num, value)
    hq.heappush(num, value)

print(sum(num))