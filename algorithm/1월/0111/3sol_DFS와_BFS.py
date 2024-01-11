# 백준 1260 DFS와 BFS

from collections import deque


n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,n+1):
    graph[i].sort()


def bfs(arr):
    q = deque()
    visit = [0]*(n+1)
    answer = list()

    q.append(v)
    visit[v] = 1

    while q:
        now = q.popleft()
        answer.append(now)
        for next_node in arr[now]:
            if not visit[next_node]:
                visit[next_node] = 1
                q.append(next_node)

    return answer


d_answer = list()
d_visit = [0]*(n+1)
d_visit[v] = 1


def dfs(arr,now):
    d_answer.append(now)

    for next_node in arr[now]:
        if not d_visit[next_node]:
            d_visit[next_node] = 1
            dfs(arr,next_node)


dfs(graph,v)
print(*d_answer)
print(*bfs(graph))
