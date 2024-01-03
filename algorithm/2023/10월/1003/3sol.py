# 프로그래머스 섬 연결하기

import heapq as hq


def solution(n, costs):
    tree = [[] for _ in range(n)]
    v = [0] * n

    for s, e, w in costs:
        tree[s].append((e, w))
        tree[e].append((s, w))

    heap = list()

    for end, weight in tree[0]:
        hq.heappush(heap, (weight, 0, end))

    answer = 0

    while heap:
        w, s, e = hq.heappop(heap)

        if not v[s] or not v[e]:
            v[s] = 1
            v[e] = 1

            answer += w

            for next_e, next_w in tree[e]:
                if not v[next_e]:
                    hq.heappush(heap, (next_w, e, next_e))

    return answer