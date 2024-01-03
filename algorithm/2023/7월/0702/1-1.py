n = int(input())
arr = [0]+list(map(int,input().split()))
v = [int(1e9)]*(n+1)
v[1]= 0

for i in range(1,n+1):
    for j in range(i+1,min(i+arr[i]+1,n+1)):
        if v[j] > v[i]+1:
            v[j] = v[i]+1

if v[-1] == int(1e9):
    v[-1] = -1
print(v[-1])