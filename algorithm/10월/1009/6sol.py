n = int(input())
arr = list(map(int,input().split()))
max_v = max(arr)
answer = 0
for i in arr:
    answer  += (i/max_v)*100

print(answer/n)