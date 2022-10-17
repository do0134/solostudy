import heapq as h
import sys


t = int(input())

for _ in range(t):
    n = int(input())

    maxq = list()
    minq = list()
    v = [0]*1000001
    cnt = 0
    for i in range(n):
        fun,num= sys.stdin.readline().split()
        if fun == "I":
            h.heappush(maxq, (int(num),i))
            h.heappush(minq,(-int(num),i))
            v[i] = 1
            cnt += 1
        else :
            if cnt == 0 :
                maxq = list()
                minq = list()
            else:
                if num == "1":
                    while minq and not v[minq[0][1]]:
                        h.heappop(minq)
                    if minq:
                        cnt -= 1
                        v[minq[0][1]] = 0
                        h.heappop(minq)
                else:
                    while maxq and not v[maxq[0][1]]:
                        h.heappop(maxq)
                    if maxq:
                        cnt -= 1
                        v[maxq[0][1]] = 0
                        h.heappop(maxq)




    if cnt == 0:
        print("EMPTY")
    else:
        while maxq and not v[maxq[0][1]]:
            h.heappop(maxq)
        while minq and not v[minq[0][1]]:
            h.heappop(minq)
        print(-minq[0][0],maxq[0][0])
