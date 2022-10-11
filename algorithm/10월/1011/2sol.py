n,k = map(int,input().split())

arr = [i for i in range(n+1)]
pn = []
flag = False
for i in range(2,n+1):
    if arr[i]:
        pn.append(arr[i])
        k -= 1
        if k == 0:
            print(arr[i])
            break
        for j in range(arr[i]*2,n+1,arr[i]):
            if arr[j]:
                k -= 1
                if k == 0:
                    print(arr[j])
                    flag = True
                    break
                arr[j] = 0

        if flag:
            break



