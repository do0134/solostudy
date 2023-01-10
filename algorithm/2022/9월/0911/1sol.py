import sys
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int,input().split()))
last = list(map(int,input().split()))
pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i

def pre(i_l, i_r, l_l,l_r):
    if(i_l > i_r) or (l_l > l_r):
        return
    p = last[l_r]
    print(p, end = " ")

    left = pos[p] -i_l
    right = i_r - pos[p]
    pre(i_l,i_l+left-1,l_l,l_l+left-1)
    pre(i_r-right+1,i_r,l_r-right,l_r-1)

pre(0,n-1,0,n-1)