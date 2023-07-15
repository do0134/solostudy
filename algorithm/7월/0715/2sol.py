# 백준 1132 합
# https://www.acmicpc.net/problem/1132

from collections import defaultdict
import sys

n = int(input())
cnt = defaultdict(int)
number = defaultdict(int)
arr = list()
first = list()

for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    arr.append(temp)
    temp_len = len(temp)
    for i in range(temp_len):
        cnt[temp[i]] += 10**(temp_len-1-i)
        if not i:
            first.append(temp[i])

i = 9
flag = True
while i >= 0 and flag:
    max_v = 0
    max_value = list()
    for char in cnt.keys():
        if cnt[char]*i > max_v and cnt[char]:
            max_v = cnt[char]*i
            max_value = [char]
        elif cnt[char]*i == max_v and cnt[char]:
            max_value.append(char)

    if len(max_value) > 1:
        best = list()
        for value in max_value:
            if value in first:
                best.append(value)

        for best_value in best:
            if not cnt[best_value]:
                continue
            cnt[best_value] = 0
            number[best_value] = i
            i -= 1

        for value in max_value:
            if value not in best and cnt[value]:
                cnt[value] = 0
                number[value] = i
                i -= 1
    elif len(max_value) == 1:
        best_value = max_value[0]
        cnt[best_value] = 0
        number[best_value] = i
        i -= 1
    for key in cnt.keys():
        if cnt[key]:
            break
    else:
        flag = False

for i in first:
    min_v = 10
    change = ""
    if not number[i]:
        for key in cnt.keys():
            if key not in first and min_v > number[key]:
                min_v = number[key]
                change = key
        for key in cnt.keys():
            if number[key] < number[change]:
                number[key] += 1
        number[change] = 0

answer = 0

for i in arr:
    temp = ""
    for c in i:
        temp += str(number[c])
    answer += int(temp)

print(answer)

# def find_best(arr1, idx):
#     if len(arr1) == 1:
#         return arr1
#     if not idx:
#         value = list()
#         for i in arr1:
#             if i not in first:
#                 value.append(i)
#         for i in arr1:
#             if i not in value:
#                 value.append(i)
#         return value
#
#     value = list()
#
#     while arr1:
#         min_v = 51
#         min_value = list()
#         for i in arr1:
#             if cnt[i][idx] < min_v:
#                 min_v = cnt[i][idx]
#                 min_value = [i]
#             elif cnt[i][idx] == min_v:
#                 min_value.append(i)
#
#         if len(min_value) >= 1:
#             value += find_best(min_value,idx-1)
#             for i in value:
#                 if i in arr1:
#                     arr1.remove(i)
#
#     return value




# for _ in range(n):
#     temp = list(sys.stdin.readline().rstrip())
#     arr.append(temp)
#     temp_len = len(temp)
#     for i in range(temp_len):
#         if not cnt[temp[i]]:
#             cnt[temp[i]] = [0]*12
#             cnt[temp[i]][temp_len-i-1] = 1
#         else:
#             cnt[temp[i]][temp_len-i-1] += 1
#         if not i:
#             first.append(temp[i])
#
# num = 9
#
# for char in cnt.keys():
#     number[char] = -1
#
# for i in range(11,-1,-1):
#     exist = list()
#     for char in cnt.keys():
#         if cnt[char][i] and number[char] == -1:
#             max_v = cnt[char][i]
#             exist.append(char)
#
#     if not exist:
#         continue
#     else:
#         sub = find_best(exist,i)
#         sub = sub[::-1]
#         for i in range(len(sub)):
#             number[sub[i]] = num
#             num -= 1
#
# answer = 0
#
# for i in arr:
#     temp = ""
#     for c in i:
#         temp += str(number[c])
#     answer += int(temp)
#
# print(answer)






"""
5
AAA
BAD
CDA
DDD
FCD
"""