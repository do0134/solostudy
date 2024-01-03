# 백준 1094 막대기

X = int(input())
answer = 0
for i in range(5,-1,-1):
    if 2 << i <= X:
        X -= 2 << i
        answer += 1
    if not X:
        break

if X:
    answer += 1

print(answer)