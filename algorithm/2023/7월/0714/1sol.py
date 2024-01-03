# 백준 2036 수열의 점수
# https://www.acmicpc.net/problem/2036

n = int(input())
a = list()
b = list()
c = list()
for _ in range(n):
    temp = int(input())
    if temp < 0:
        b.append(temp)
    elif not temp:
        c.append(temp)
    else:
        a.append(temp)

answer = 0
a.sort(reverse=True)
b.sort()
c_idx = 0

for i in range(0, len(a), 2):
    if i < len(a)-1 and a[i+1] > 1:
        answer += a[i]*a[i+1]
    else:
        for j in range(i, len(a)):
            answer += a[j]
        break

for i in range(0, len(b), 2):
    if i < len(b)-1:
        answer += b[i]*b[i+1]
    else:
        for j in range(i,len(b)):
            value = b[j]
            if c and len(c)-1 >= c_idx:
                value *= 0
                c_idx += 1
            answer += value
        break

print(answer)