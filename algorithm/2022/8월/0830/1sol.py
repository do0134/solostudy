def dfs(s,arr):
    for e, d in adj[s]:
        if arr[e] == 0:
            arr[e] = arr[s] + d
            dfs(e,arr)
    pass

v = int(input())

graph = []
for _ in range(v):
    graph.append(list(map(int,input().split())))

adj = [[] for _ in range(v+1)]

for i in graph :
    idx = -1
    for j in range(len(i)):

        if i[j] == -1 :
            break
        elif j == 0:
            idx = i[j]
        elif j%2:
            adj[idx].append((i[j],i[j+1]))
        elif j%2 == 0 :
            continue

result = [0]*(v+1)
dfs(1,result)
result[1] = 0
temp = max(result)
max_idx = result.index(temp)
answer = [0]*(v+1)
dfs(max_idx, answer)
answer[max_idx] = 0

print(max(answer))