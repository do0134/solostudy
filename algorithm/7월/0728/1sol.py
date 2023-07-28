# 백준 1041 주사위
# https://www.acmicpc.net/problem/1041

n = int(input())
num = list(map(int,input().split()))
dice = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

min_v1 = min(num)
min_v2 = int(1e9)
min_v3 = int(1e9)


s = "ABCDEF"
for i in range(6):
    for j in range(6):
        if i != j and j != dice[s[i]]:
            min_v2 = min(min_v2,num[i]+num[j])

for i in range(6):
    for j in range(6):
        if i != j and i != dice[s[j]]:
            for k in range(6):
                if i != k and j != k and i != dice[s[k]] and j != dice[s[k]]:
                    min_v3 = min(min_v3, num[i]+num[j]+num[k])

if n == 1:
    print(sum(num)-max(num))
else:
    print(min_v3*4+min_v2*((n-1)*4)+min_v2*((n-2)*4)+min_v1*((n-1)*(n-2)*4)+min_v1*(n-2)**2)