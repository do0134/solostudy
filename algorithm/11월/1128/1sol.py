# 백준 14890 경사로

def find_r(r, c, arr, n, l):
    road = list()

    cache = [arr[r][c],r]
    r += 1

    while r < n:
        if arr[r][c] != arr[r-1][c]:
            if abs(arr[r][c] - arr[r-1][c]) != 1:
                return False
            elif arr[r][c] > arr[r-1][c]:
                if r - cache[1] < l:
                    return False
                elif r - l < 0:
                    return False
                elif road and r-l-1 < road[-1]:
                    return False
                else:
                    road = [r-l]
                    cache = [arr[r][c], r]
                    r += 1
            elif arr[r][c] < arr[r-1][c]:
                if r + l > n:
                    return False
                elif road and r-l+1 < road[-1]:
                    return False
                else:
                    temp = r
                    for i in range(1,l):
                        r += 1
                        if arr[r][c] != arr[r-1][c]:
                            return False
                    else:
                        cache = [arr[r][c], temp]
                        road = [r]
                        r += 1
        else:
            r += 1
    return True


def find_c(r, c, arr, n, l):
    road = list()

    cache = [arr[r][c], c]
    c += 1

    while c < n:
        if arr[r][c] != arr[r][c-1]:
            if abs(arr[r][c] - arr[r][c-1]) != 1:
                return False
            elif arr[r][c] > arr[r][c-1]:
                if c - cache[1] < l:
                    return False
                elif c - l < 0:
                    return False
                elif road and c-l-1 < road[-1]:
                    return False
                else:
                    road = [c-l]
                    cache = [arr[r][c], c]
                    c += 1
            elif arr[r][c] < arr[r][c-1]:
                if c + l > n:
                    return False
                elif road and c-l+1 < road[-1]:
                    return False
                else:
                    temp = c
                    for i in range(1,l):
                        c += 1
                        if arr[r][c] != arr[r][c-1]:
                            return False
                    else:
                        cache = [arr[r][c], temp]
                        road = [c]
                        c += 1
        else:
            c += 1
    return True


n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    if find_r(0,i,arr,n,m):
        answer += 1
    if find_c(i,0,arr,n,m):
        answer += 1
print(answer)