# 프로그래머스 시소 짝꿍

from collections import defaultdict


def solution(weights):
    answer = 0

    person = defaultdict(int)

    for weight in weights:
        person[weight] += 1

    for key in person.keys():
        value = person[key]
        if value > 1:
            answer += value*(value-1) // 2
        a = key*2/3
        b = key/2
        c = key*3/4
        if a in weights:
            answer += person[a] * value
        if b in weights:
            answer += person[b] * value
        if c in weights:
            answer += person[c] * value


    return answer