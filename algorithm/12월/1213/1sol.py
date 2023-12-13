# 백준 10021 Watering the Fields

import sys
import heapq as hq
input = sys.stdin.readline

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return False
    parent[root2] = root1
    return True


n,c = map(int,input().split())

farm = list()
for _ in range(n):
    x,y = map(int,input().split())
    farm.append((x,y))

heap = list()
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        x1,y1 = farm[i]
        x2,y2 = farm[j]
        cost = (x1-x2)**2 + (y1-y2)**2
        if cost >= c:
            hq.heappush(heap,(cost,i,j))

leaf_cnt = 0
answer = 0
while heap:
    now_cost, node1, node2 = hq.heappop(heap)
    if union(node1, node2):
        answer += now_cost
        leaf_cnt += 1
        if leaf_cnt == n-1:
            break

if leaf_cnt == n-1:
    print(answer)
else:
    print(-1)