# 백준 6367 Color Me Less

import sys
input = sys.stdin.readline

arr = list()


def calc(list1):
    value = int(1e9)
    return_list = list()

    for temp in arr:
        temp_value = 0
        for i in range(3):
            temp_value += (list1[i]-temp[i])**2
        temp_value = temp_value **0.5
        if value > temp_value:
            return_list = temp
            value = temp_value

    return return_list


for _ in range(16):
    temp_list = list(map(int,input().split()))
    arr.append(temp_list)

while True:
    temp_list = list(map(int,input().split()))
    if temp_list == [-1,-1,-1]:
        break

    target = calc(temp_list)
    print(f"({temp_list[0]},{temp_list[1]},{temp_list[2]}) maps to ({target[0]},{target[1]},{target[2]})")
