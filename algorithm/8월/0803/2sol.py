# 못풀었다 다시 풀어보자 S, T에서 target을 가는 거를 우선적으로 
# 그리고 target이 S->T 가는 길 사이에 있는지 T->S 가는 길 사이에 있는지를 봐야됨
# 그래서 개인적으론 재귀를 계속 돌리면서 T를 갈 수 있다면 True 없다면 False를 주는게 좋지 않을까 싶은데
# 그러면 시간이..? maxrecursion도 고려해야 하는데 dfs를 돌릴 때, 10**9가 넘는 케이스가 존재하는 거 같았음
# 근데 인터넷에 떠도는 정답들 다 틀린 거 같은데

from collections import defaultdict, deque


def bfs(start, end, visit, node):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        idx = q.popleft()
        if idx == end:
            continue
        for next_idx in node[idx]:
            if not visit[next_idx]:
                q.append(next_idx)
                visit[next_idx] = 1


n,m = map(int,input().split())
node1 = defaultdict(list)
node2 = defaultdict(list)
for i in range(m):
    s,e = map(int,input().split())
    node1[s].append(e)
    node2[e].append(s)

S, T = map(int,input().split())
v1 = [0]*(n+1)
v2 = [0]*(n+1)
v3 = [0]*(n+1)
v4 = [0]*(n+1)

bfs(S,T,v1,node1)
bfs(T,S,v2,node1)
bfs(S,T,v3,node2)
bfs(T,S,v4,node2)

answer = 0
for i in range(1,n+1):
    if i == S or i == T:
        continue
    elif v1[i] and v2[i] and v3[i] and v4[i]:
        answer += 1

print(answer)