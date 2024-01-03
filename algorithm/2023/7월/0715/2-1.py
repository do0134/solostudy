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

num = 9
# 가중치 대로 정렬
keys = sorted(cnt.keys(), key=lambda x : cnt[x], reverse=True)
# 나중을 위해서 가장 큰 자릿 수가 아닌 숫자를 뒤로 미룬다.
for i in range(len(keys)-1):
    if keys[i] == keys[i+1] and i not in first:
        keys[i], keys[i+1] = keys[i+1], keys[i]

#가중치 순서대로 숫자를 할당
for key in keys:
    number[key] = num
    num -= 1

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