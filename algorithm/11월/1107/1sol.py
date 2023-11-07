# 프로그래머스 두 원 사이의 정수쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187

import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        x1 = math.sqrt((r2 ** 2 - i ** 2))
        if r1 >= i:
            x2 = math.sqrt((r1 ** 2 - i ** 2))
        else:
            x2 = 0
        value = math.floor(x1) - math.ceil(x2)
        if value >= 0:
            answer += value + 1

    answer *= 4

    return answer