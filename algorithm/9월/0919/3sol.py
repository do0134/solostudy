# 프로그래머스 의상

from collections import defaultdict


def solution(clothes):
    my_dict = defaultdict(list)
    for i, j in clothes:
        my_dict[j].append(i)

    answer = 1
    for i in my_dict.keys():
        answer *= len(my_dict[i]) + 1

    return answer - 1