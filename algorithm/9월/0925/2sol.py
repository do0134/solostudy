# 조합뽑기

def perm(per,idx):
    if idx == m:
        per.sort()
        if per not in answer :
            answer.append(per)
        return
    else:
        for i in range(n):
            if not v[i]:
                v[i] = 1
                perm(per+[arr[i]],idx+1)
                v[i] = 0
            pass


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
v = [0]*n
answer = list()
perm([],0)

for i in answer:
    print(*i)
