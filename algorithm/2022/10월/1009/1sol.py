t = int(input())

for _ in range(t):
    n,s = input().split()
    n = int(n)
    answer = ''
    for i in s:
        answer += i*n
    print(answer)

