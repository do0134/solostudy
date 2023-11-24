# 백준 2473 세 용액

def solve():
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    if n == 3:
        return arr
    cnt = 3000000001

    answer = []

    for i in range(n-2):
        l = i+1
        r = len(arr)-1
        while l < r:
            value = arr[i] + arr[l] + arr[r]

            if cnt > abs(value):
                cnt = abs(value)
                answer = [arr[i], arr[l], arr[r]]

            if value > 0:
                r -= 1
            elif value < 0:
                l += 1
            elif not value:
                return [arr[i], arr[l], arr[r]]

    return answer


print(*solve())