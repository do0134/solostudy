# 백준 2212 센서
# https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())
arr = list(set(map(int,input().split())))
arr.sort()


answer = list()
for i in range(len(arr)-1):
    answer.append(arr[i+1]-arr[i])

answer.sort(reverse=True)

print(sum(answer[k-1:]))