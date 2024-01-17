# 백준 2108 통계학

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

sum_v = 0
cnt = defaultdict(int)
cnt_value = [0,0]
max_v = -4001
min_v = 4001
arr = list()

for _ in range(n):
    num = int(input())
    cnt[num] += 1
    arr.append(num)
    min_v = min(num, min_v)
    max_v = max(num, max_v)
    sum_v += num
    if cnt[num] > cnt_value[0]:
        cnt_value = [cnt[num], num]
    elif cnt[num] == cnt_value[0]:
        cnt_value.append(num)

arr.sort()
cnt_value[0] = int(1e9)
cnt_value.sort()

print(round(sum_v/n))
print(arr[n//2])
if len(cnt_value) > 2:
    print(cnt_value[1])
else:
    print(cnt_value[0])

print(max_v-min_v)