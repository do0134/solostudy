# 백준 24416 알고리즘 수업 - 피보나치 수1

n = int(input())
arr1 = [0]*(n+1)
arr1[1] = 1

for i in range(2,n+1):
    arr1[i] = arr1[i-1] + arr1[i-2]


print(arr1[n], n-2)