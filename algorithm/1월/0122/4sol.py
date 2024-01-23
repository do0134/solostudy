import sys
input = sys.stdin.readline


def solve(arr):
    stack = list()
    now_max = 0
    max_v = 0
    min_h = int(1e9)

    for i in range(len(arr)):
        if not stack:
            min_h = arr[i]
            now_max = arr[i]
            stack.append(i)
        else:
            stack.append(i)
            min_h = min(min_h, arr[i])
            if now_max < arr[i]:
                while stack and now_max > min_h*(i-stack[-1]):
                    value = stack.pop()

                    if arr[value] == min_h:
                        min_h = min(stack)

            if not stack:
                now_max = arr[i]
                stack.append(i)
            else:
                now_max = arr[stack[-1]] * (i-stack[-1])
        print(i, now_max, max_v)
        max_v = max(now_max, max_v)

    return max_v


while True:
    arr = list(map(int,input().split()))
    if len(arr) == 1 and not arr[0]:
        break

    print(solve(arr))