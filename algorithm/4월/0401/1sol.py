# 백준 10816 숫자 카드 2

from collections import defaultdict

my_dict = defaultdict(int)


def int_input():
    return int(input())


def list_input():
    return list(map(int,input().split()))


n = int_input()
arr1 = list_input()

for i in arr1:
    my_dict[i] += 1

m = int_input()
arr2 = list_input()

answer = list()

for i in arr2:
    answer.append(my_dict[i])

print(*answer)
