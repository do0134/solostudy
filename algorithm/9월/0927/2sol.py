a,b = map(int,input().split())

num = str(a)
min_v = int(1e9)
def solve(n,idx):
    global min_v
    if int(n) >= b:
        if int(n)== b and min_v > idx :
            min_v = idx
        return
    else:
        solve(n+'1',idx+1)
        next = int(n)*2
        solve(str(next),idx+1)

solve(num,1)
if min_v == int(1e9):
    print(-1)
else:
    print(min_v)