# 백준 2138 전구와 스위치

from copy import deepcopy


def solve(arr,cnt):
    for i in range(1,n):
        if arr[i-1] != target[i-1]:
            cnt += 1
            arr[i-1] = (arr[i-1]+1)%2
            arr[i] = (arr[i]+1)%2
            if i < n-1:
                arr[i+1] = (arr[i+1]+1)%2
    if check(arr):
        return cnt
    else:
        return int(1e9)


def check(arr):
    for i in range(n):
        if arr[i] != target[i]:
            return False
    return True


n = int(input())
arr1 = list(map(int,input()))
arr2 = deepcopy(arr1)
target = list(map(int,input()))
answer = 0

arr2[0] = (arr2[0]+1)%2
arr2[1] = (arr2[1]+1)%2

answer = solve(arr1,0)
answer = min(solve(arr2,1),answer)

if answer == int(1e9):
    print(-1)
else:
    print(answer)
