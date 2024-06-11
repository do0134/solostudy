n = int(input())

arr = list(map(int,input().split()))
max_v = 0


def check(idx):
    global max_v
    temp = 0
    for i in range(idx+1, n):
        if arr[i] > arr[idx]:
            break
        elif arr[i] == arr[idx]:
            temp += 1
            break
        else:
            x = i - idx
            y = arr[idx]
            if x == 1:
                temp += 1
                continue
            a = (arr[i] - arr[idx]) / x
            temp_v = calc(x,y,a)

            for j in range(idx+1, i):
                if calc(j-idx, y, a) > temp_v:
                    break
            else:
                temp += 1
    
    for i in range(idx, -1, -1):
        if arr[i] > arr[idx]:
            break
        elif arr[i] == arr[idx]:
            temp += 1
            break
        else:
            x = i - idx
            y = arr[idx]
            if x == 1:
                temp += 1
                continue
            a = (arr[i] - arr[idx]) / x
            temp_v = calc(x,y,a)

            for j in range(idx+1, i):
                if calc(j-idx, y, a) > temp_v:
                    break
            else:
                temp += 1


    max_v = max(temp, max_v)


def calc(x,y,a):
    return a*x + y
        

for i in arr:
    check(i)

print(max_v)