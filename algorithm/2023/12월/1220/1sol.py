# 백준 14002 가장 긴 증가하는 부분수열4

from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))
max_l = 1
answer = list()
idx_dict = defaultdict(list)
dp = [1]*n

for i in range(n):
    idx_dict[i] = [arr[i]]

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j] and dp[j] < dp[i]+1:
            dp[j] = dp[i]+1
            idx_dict[j] = idx_dict[i] + [arr[j]]
            if dp[j] > max_l:
                answer = idx_dict[j]
                max_l = dp[j]

if not answer:
    for i in range(n):
        if dp[i] == max_l:
            answer = idx_dict[i]

print(max(dp))
print(*answer)

"""
13
3 4 5 6 2 3 1 7 4 3 5 6 7
"""