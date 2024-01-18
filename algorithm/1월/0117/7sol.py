n = int(input())

tree = [list() for _ in range(n+1)]

for _ in range(n-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

v = [0]*(n+1)
target = list(map(int,input().split()))

idx = 1
v[target[0]] = 1


def dfs(node):
    global idx
    v[node] = 1
    print(node, idx)
    if idx == n:
        return True
    cnt = 0
    w_cnt = 0
    while cnt < len(tree[node]):
        for i in range(len(tree[node])):
            value = tree[node][i]
            if v[value]:
                if not w_cnt:
                    cnt += 1
                continue
            if target[idx] == value:
                tree[node][i] = int(1e9)
                idx += 1
                cnt += 1
                dfs(value)
        else:
            return False

    return True

dfs(target[0])
v.pop(0)

if 0 in v:
    print(0)
else:
    print(1)