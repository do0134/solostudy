# 백준 2212 센서

n = int(input())
k = int(input())
arr = list(map(int,input().split()))

arr.sort()
answer = list()

for i in range(1,n):
    answer.append(arr[i]-arr[i-1])

answer.sort(reverse= True)
print(sum(answer[k-1:]))