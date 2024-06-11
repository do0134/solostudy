# 백준 1027 고층건물

n = int(input())
arr = list(map(int, input().split()))
max_v = 0

def check(idx):
    global max_v
    temp = 0
    
    # 오른쪽 탐색
    max_slope = float('-inf')
    for i in range(idx + 1, n):
        slope = (arr[i] - arr[idx]) / (i - idx)
        if slope > max_slope:
            max_slope = slope
            temp += 1
    
    # 왼쪽 탐색
    max_slope = float('-inf')
    for i in range(idx - 1, -1, -1):
        slope = (arr[i] - arr[idx]) / (idx - i)
        if slope > max_slope:
            max_slope = slope
            temp += 1

    max_v = max(temp, max_v)

for i in range(n):
    check(i)

print(max_v)
