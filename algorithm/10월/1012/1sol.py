n,k = map(int,input().split())
arr = [i for i in range(k+1)]
pn = []
for i in range(2,len(arr)):
    if arr[i]:
        for j in range(arr[i]*2,len(arr),arr[i]):
            arr[j] = 0
        if n <= arr[i] <= k+1:
            print(arr[i])
        arr[i] = 0



