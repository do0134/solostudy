# codeforces Guess the Maximum

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    l = 0
    r = 1
    
    min_v = int(1e9)
    max_v = max(arr[l],arr[r])

    while r < n and l < r:
        min_v = min(min_v, max_v)
        if arr[r] < max_v:
            l = r
            r = r+1
            if r < n:
                max_v = max(arr[l],arr[r])
        else:
            max_v = max(max_v, arr[r])
            r+=1

    print(min_v-1)