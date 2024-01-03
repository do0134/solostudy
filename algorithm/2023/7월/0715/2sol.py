# 백준 1132 합
# https://www.acmicpc.net/problem/1132

from collections import defaultdict
import sys

n = int(input())
# cnt 딕셔너리에 10**해당 자리수를 더할거임! 이 자리 수 더한 값이 가중치가 될 예정
cnt = defaultdict(int)
# 알파벳이 무슨 숫자인지 나타내는 딕셔너리
number = defaultdict(int)
arr = list()
# 첫 자리인지 확인하기
first = list()

for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    arr.append(temp)
    temp_len = len(temp)
    for i in range(temp_len):
        # temp[i] 키에 자리 수만큼 더한다.
        cnt[temp[i]] += 10**(temp_len-1-i)
        if not i:
            first.append(temp[i])

i = 9
flag = True
# i는 알파벳에 할당할 숫자
# 모든 숫자를 할당했다면 flag를 True로 한다.(모든 예제가 0까지 할당하지 않음!)
while i >= 0 and flag:
    # 가장 가중치가 높은 것들
    max_v = 0
    max_value = list()
    # 가중치 높은 거 골라내기
    for char in cnt.keys():
        if cnt[char]*i > max_v and cnt[char]:
            max_v = cnt[char]*i
            max_value = [char]
        elif cnt[char]*i == max_v and cnt[char]:
            max_value.append(char)
    # 가중치가 같을 수도 있다.
    if len(max_value) > 1:
        best = list()
        # 가중치가 높다면 0으로 시작하지 않는 것을 우선순위로 둔다.
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
    # 가중치가 높은게 하나 뿐이라면 뭐...
    elif len(max_value) == 1:
        best_value = max_value[0]
        cnt[best_value] = 0
        number[best_value] = i
        i -= 1
    # 만약 0까지 할당 안 해도 끝난다면
    for key in cnt.keys():
        if cnt[key]:
            break
    else:
        flag = False

# 만약 첫 번째 자리가 0이라면 첫 번째 자리가 0이 아닌 알파벳 중 가장 수가 작은 것을 찾아 0으로 만들고 그 수 보다 작은 수들을 +1 한다.
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