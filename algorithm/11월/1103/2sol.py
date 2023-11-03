# 백준 2891 카약과 강풍

n,s,r = map(int,input().split())
bk = list(map(int,input().split()))
left = list(map(int,input().split()))
bk.sort();left.sort()
answer = s

for i in range(s):
    if bk[i] in left:
        answer -= 1
        left[left.index(bk[i])] = -1
        bk[i] = -100

for i in range(s):
    if bk[i]-1 in left:
        answer -= 1
        left[left.index(bk[i]-1)] = -1
    elif bk[i]+1 in left:
        answer -= 1
        left[left.index(bk[i]+1)] = -1

print(answer)