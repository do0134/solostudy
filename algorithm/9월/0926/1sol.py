import sys
input = sys.stdin.readline


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for _ in range(m):
    cr,cc,nr,nc = map(int,input().split())
    cr,cc,nr,nc = cr-1,cc-1,nr-1,nc-1

