# 걍 0부터 1000까지 다 훑으면 안되나?

n = int(input())
arr = list(map(int,input().split()))

def solve(n):
    if n == 1 :
        return 1
    else:
        max_cnt = 0
        for i in range(n):
            l = i
            r = i+1
            cnt = 0
            dp = [arr[i]]
            while r < n :
                if arr[l] < arr[r]:
                    cnt += 1
                    l = r
                    r += 1
                else:
                    r += 1
            if cnt != 0 :
                cnt += 1
            max_cnt = max(cnt,max_cnt)
        return max_cnt
print(solve(n))
