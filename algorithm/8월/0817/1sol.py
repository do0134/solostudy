# 백준 1135 뉴스 전하기
# https://www.acmicpc.net/problem/1135

from collections import defaultdict

n = int(input())
companies = list(map(int,input().split()))
call = defaultdict(list)
dp = [i for i in range(n)]


for i in range(n):
    call[companies[i]].append(i)


def make_dp(company):
    if not call[company]:
        dp[company] = 0
        return

    time = list()
    for next_company in call[company]:
        make_dp(next_company)
        time.append(dp[next_company])

    time.sort(reverse=True)
    max_time = 0
    for i in range(1,len(time)+1):
        max_time = max(max_time,i+time[i-1])

    dp[company] = max_time


make_dp(0)
print(dp[0])