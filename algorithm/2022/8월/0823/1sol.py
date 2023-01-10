from collections import defaultdict,deque
def bfs(start):
    global max_v, far_v
    q = deque()
    v = [0]*10001
    q.append((start,0))
    v[start] = 1
    while q :
        cs,cw = q.popleft()
        for ns,nw in tree[cs]:
            if not v[ns]:
                v[ns] = 1
                dist = nw+cw
                if dist > max_v :
                    max_v = dist
                    far_v = ns
                q.append((ns,dist))


tree = defaultdict(list)
edges = []
while True:
    try :
        s,e,w = map(int,input().split())
        tree[s].append((e,w))
        tree[e].append((s,w))
    except :
        break

max_v = far_v = 0
if tree :
    bfs(1)
    bfs(far_v)
    print(max_v)
else:
    print(0)