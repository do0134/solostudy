# 백준 11399 ATM

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

sum_v = 0
answer = 0

for i in arr:
    sum_v += i
    answer += sum_v

print(answer)