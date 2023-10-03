# 프로그래머스 여행경로

from collections import defaultdict


def dfs(now, v, trip, use_ticket):
    global airlines, l, answer
    if len(trip) == l+1:
        answer.append(trip)
        return

    for i in airlines[now]:
        if v[i] and use_ticket[(now,i)]:
            v[i] -= 1
            use_ticket[(now,i)] -= 1
            dfs(i,v,trip+[i], use_ticket)
            use_ticket[(now,i)] += 1
            v[i] += 1


def solution(tickets):
    global airlines, l, answer

    l = len(tickets)
    airlines = defaultdict(set)
    visit = defaultdict(int)
    used_ticket = defaultdict(int)

    for s,e in tickets:
        airlines[s].add(e)
        visit[e] += 1
        used_ticket[(s,e)] += 1

    answer = []
    dfs("ICN", visit, ["ICN"], used_ticket)
    answer.sort()
    return answer[0]