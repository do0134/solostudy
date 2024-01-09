# 백준 2493 탑

n = int(input())
arr = list(map(int,input().split()))
answer = [0]*n
stack = list()


for i in range(n-1,-1,-1):
    if stack and stack[-1][0] < arr[i]:
        while stack and stack[-1][0] < arr[i]:
            height, idx = stack.pop()
            answer[idx] = i+1

    stack.append((arr[i],i))

print(*answer)