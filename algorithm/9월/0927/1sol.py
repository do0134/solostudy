def perm(per,idx,s):
    if idx == m:
        per.sort()
        if per not in answer:
            answer.append(per)
        return
    else:
        for i in range(s,n):
            if v[i] < n :
                v[i] += 1
                perm(per+[arr[i]],idx+1,i)
                v[i] -=1




n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
v = [0]*n
answer = list()
perm([],0,0)

for i in answer:
    print(*i)

