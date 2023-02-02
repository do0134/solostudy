# 프로그래머스 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    if n > s:
        return [-1]

    answer = [s // n] * n
    idx = len(answer) - 1

    for i in range(s % n):
        answer[idx] += 1
        idx -= 1
        if idx == -1:
            idx = len(answer) - 1

    return answer