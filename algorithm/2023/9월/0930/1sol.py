# 백준 11501 주식
def solve(arr: list) -> int:
    answer = 0
    max_v = arr[-1]
    for i in range(n-2,-1,-1):
        if max_v > arr[i]:
            answer += max_v - arr[i]
        else:
            max_v = arr[i]

    return answer


t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int,input().split()))
    print(solve(stock))
