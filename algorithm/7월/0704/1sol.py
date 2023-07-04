# 백준 4256 트리
# https://www.acmicpc.net/problem/4256

def postorder(pre, ino):
    if len(pre) == 0:
        return []

    root = pre[0]
    root_idx = ino.index(root)

    left_ino = ino[:root_idx]
    right_ino = ino[root_idx+1:]

    left_pre = pre[1:1+len(left_ino)]
    right_pre = pre[1+len(left_ino):]

    left_post = postorder(left_pre, left_ino)
    right_post = postorder(right_pre, right_ino)

    return left_post+right_post+[root]


t = int(input())

for _ in range(t):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    print(*postorder(preorder,inorder))