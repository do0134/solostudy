# 백준 14003 가장 긴 증가하는 부분 수열 5

import bisect, sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

answer = list()
bigger = []
max_l = []

for num in arr:
    idx = bisect.bisect_left(bigger, num)
    if idx == len(bigger):
        bigger.append(num)
        max_l.append(len(bigger)-1)
    else:
        bigger[idx] = num
        max_l.append(idx)

arr_len = len(bigger)
c_idx = len(arr) - 1

for i in range(len(max_l)-1,-1,-1):
    if max_l[i] == arr_len-1:
        answer.append(arr[c_idx])
        arr_len -= 1
    c_idx -= 1

answer.reverse()

print(len(answer))
print(*answer)
