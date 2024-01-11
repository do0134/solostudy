# 백준 9095 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

from collections import deque

n = int(input())


def bfs(target_num: int) -> int:
    q = deque()
    answer = 0

    for i in range(1,4):
        if i < target_num:
            q.append(i)
        elif i == target_num:
            answer += 1

    while q:
        now = q.popleft()

        for i in range(1,4):
            if now+i < target_num:
                q.append(now+i)
            elif now+i == target_num:
                answer += 1

    return answer


for _ in range(n):
    target = int(input())
    print(bfs(target))