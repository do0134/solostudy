# 백준 1956 운동

V,E = map(int,input().split())
graph = [[int(1e9)]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u][v] = w

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1,V+1):
            if graph[j][i] + graph[i][k] < graph[j][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

answer = int(1e9)

for i in range(1,V+1):
    answer = min(answer, graph[i][i])

if answer == int(1e9):
    print(-1)
else:
    print(answer)