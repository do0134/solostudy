# 프로그래머스 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq as hq


def solution(jobs):
    answer = 0
    n = len(jobs)
    hq.heapify(jobs)
    time = 0
    heap = list()

    while jobs:
        s, e = hq.heappop(jobs)
        if s > time:
            if heap:
                hq.heappush(jobs, [s, e])

            else:
                time = s
                hq.heappush(heap, [e, s])

            next_t, next_s = hq.heappop(heap)
            time += next_t
            answer += time - next_s
            continue
        else:
            hq.heappush(heap, [e, s])

    while heap:
        e, s = hq.heappop(heap)
        time += e
        answer += time - s

    return answer // n