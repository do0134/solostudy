t = int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a,b,c = map(int,input().split())
        arr.append((a,b,c))


    mapp = [[0]*31 for _ in range(31)]