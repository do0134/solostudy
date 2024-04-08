# 백준 조용히하라고!!

import sys
input = sys.stdin.readline

n,m,k,t,p = map(int,input().split())

mosq = list()

for _ in range(k):
    mosq.append(list(map(int,input().split())))

woo = 0
arum = 0


def woojeong(r,c,cnt,hp,v):
    global woo
    woo = max(woo, cnt)
    if woo == k:
        return

    for i in range(k):
        if not v[i]:
            nr, nc, nm = mosq[i]
            needed = abs(nr-r)+abs(nc-c)
            if needed <= hp:
                v[i] = 1
                woojeong(nr,nc,cnt+1,hp-needed,v)
                v[i] = 0


def areum():
    global arum

    for i in range(1,n+1):
        for j in range(1,m+1):
            temp = 0
            for q in range(k):
                nr,nc,nm = mosq[q]
                if nr == i and nc == j:
                    temp += 1
                else:
                    power = abs(i-nr)+abs(i-nc)
                    if power >= nm:
                        temp += 1
            arum = max(temp, arum)


visit = [0]*(k+1)
areum()
for i in range(k):
    cr, cc, cm = mosq[i]
    visit[i] = 1
    woojeong(cr,cc,1,t,visit)
    visit[i] = 0

print(woo, arum)