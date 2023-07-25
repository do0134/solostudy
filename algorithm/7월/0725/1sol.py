# 백준 1099 알 수 없는 문장
# https://www.acmicpc.net/problem/1099

import sys
from collections import defaultdict


#  바꿀 수 있는 문자열인지 확인하는 함수
def check(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    return sorted(s1) == sorted(s2)


# 점수 만들어주는 함수
def make_point(s1,s2):
    value = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            value += 1
    return value


target = input()
n = int(input())
words = defaultdict(list)

for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    words[len(temp)].append(temp)

# dp[i][j]는 target[i:j]가 점수 + target[:i]점수 즉, target[:j]의 점수 최솟값
# dp[i][0]는 target[:i]의 최솟값을 갱신
dp = [[int(1e9)]*(len(target)+1) for i in range(len(target)+1)]
dp[0][0] = 0

for i in range(len(target)+1):
    # dp[i][0]가 바뀐적 없으면, target[i:j]가 성립하지 않음
    # i인덱스까지 만든 적이 없으므로, 인덱스 i번부터 시작하는 단어를 확인할 필요 없음
    if dp[i][0] == int(1e9):
        continue
    # 만들 수 있는 단어 길이까지 반복문
    for j in range(1, len(target)-i+1):
        for word in words[j]:
            if check(target[i:i+j], word):
                point = make_point(target[i:i+j], word)
                # target[i:j]의 점수와 target[:i]점수 최솟값을 합쳐서 갱신
                dp[i][i+j] = min(dp[i][i+j], dp[i][0]+point)
                # target[:j]의 최솟값을 갱신
                dp[i+j][0] = min(dp[i+j][0],dp[i][i+j])


if dp[-1][0] == int(1e9):
    print(-1)
else:
    print(dp[-1][0])