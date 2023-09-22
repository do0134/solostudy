# 백준 1138 한 줄로 서기

n = int(input())
arr = list(map(int,input().split()))

answer = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and not answer[j]:
            answer[j] = i+1
            break
        elif not answer[j]:
            cnt += 1

print(*answer)