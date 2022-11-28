n = int(input())
soldier = list(map(int,input().split()))
subs = [1 for i in range(n+1)]

for i in range(1,n):
    for j in range(0,i):
        if soldier[j] > soldier[i] :
            subs[i] = max(subs[j]+1,subs[i])
print(n-max(subs))