# 프로그래머스 후보키

from itertools import combinations


def solution(relation):
    minimality = list()

    def check_key(idx):
        check_list = list()
        for r in relation:
            temp = list()
            for i in idx:
                temp.append(r[i])
            if temp in check_list:
                return False

            check_list.append(temp)

        return check_min(idx)

    def check_min(idx):
        for mini in minimality:
            cnt = 0
            for i in idx:
                if i in mini:
                    cnt += 1
                if cnt == len(mini):
                    return False

        minimality.append(idx)
        return True

    answer = 0
    v = [i for i in range(len(relation[0]))]

    for j in range(len(relation[0]) + 1):
        for i in combinations(v, j):
            if check_key(i):
                answer += 1

    return answer