def solve(target):
    global t,h
    ad = 0
    sub = 0
    for i in arr:
        for j in i:
            if j > target:
                sub += j - target
            elif j < target:
                ad += target - j
        if t < ad+sub*2:
            return
    else:
        if t >= ad+sub*2 and sub+b-ad >=0:
            t = ad+sub*2
            h = target


n,m,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
temp = 0

t = int(1e9)
h = int(1e9)
for i in arr:
    temp += sum(i)

h1 = temp // (n*m)
h2 = (temp+b)//(n*m)

for target in range(h1-1,h2+1):
    solve(target)
print(t,h)



